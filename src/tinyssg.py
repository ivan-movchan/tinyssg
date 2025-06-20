#!/usr/bin/python3

VERSION = '1.01'

import os, sys, datetime

def die(message, code=0):
    print(message)
    exit(code)

if __name__ != '__main__':
    die('You are doing it wrong.', 42)
else:
    print(f'TinySSG {VERSION}\nCopyright (c) 2025 Ivan Movchan\nhttps://github.com/ivan-movchan/tinyssg')
    
    try:
        from config import *
    except:
        die('Failed to import configuration module ("config.py").', 1)
    
    for directory in directories:
        source_dir, target_dir = directory, directories[directory]
        source_files = []
        
        if not os.path.isdir(source_dir):
            die(f'"{source_dir}" does not exist or is not a directory.', 2)
        
        template_file_name = template_files[source_dir]
        try:
            template_file = open(template_file_name, 'r', encoding=file_encoding)
            template_text = template_file.read()
            template_file.close()
        except:
            die(f'Failed to read "{template_file_name}" file.', 2)
        
        if not os.path.exists(source_dir):
            print(f'"{source_dir}" does not exist.')
        else:
            for file in os.listdir(source_dir):
                if file.endswith(f'.{source_file_extension}'):
                    source_files.append(file)
    
        for file in source_files:
            if not template_file_name.endswith(file):
                source_file_name = f'{source_dir}/{file}'
                target_file_name = f'{target_dir}/{file}'.replace(f'.{source_file_extension}', '.html')
                
                if os.path.isfile(target_file_name) and not overwrite_webpages:
                    print(f'"{target_file_name}" already exists. Skipping...')
                    continue
                
                try:
                    os.makedirs(target_dir, exist_ok=True)
                except:
                    die(f'Failed to create a target directories ("{target_dir}").', 2)
                
                print(f'Generating "{target_file_name}" from "{source_file_name}"...')
                
                source_file = open(source_file_name, 'r', encoding=file_encoding)
                source_file_content = source_file.read().split('\n')
                source_file.close()
                
                if len(source_file_content) < 3:
                    print(f'"{source_file_name}" contains less than 3 lines of text. Skipping...')
                    continue
                
                page_title = source_file_content[0]
                page_text = template_text.replace('{title}', page_title)
                
                page_content = '\n'.join(source_file_content[2:])
                try:
                    import markdown
                    page_content = markdown.markdown(page_content)
                except:
                    print('Failed to convert text from Markdown to HTML. Is "markdown" module installed?')
                page_text = page_text.replace('{content}', page_content)
                
                page_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S (UTC)')
                try:
                    page_datetime = datetime.datetime.now().astimezone(datetime_zone).strftime(datetime_format)
                except:
                    print(f'Failed to get date/time in "{datetime_zone}" time zone. Reverted to UTC.')
                page_text = page_text.replace('{datetime}', page_datetime)
                
                for var in text_variables:
                    page_text = page_text.replace(('{' + var + '}'), text_variables[var])
                
                try:
                    target_file = open(target_file_name, 'w', encoding=file_encoding)
                    target_file.write(page_text)
                    target_file.close()
                except:
                    die(f'Failed to write "{target_file_name}" file.', 2)