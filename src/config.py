#!/usr/bin/python3

import datetime

# Directories ('source': target').
directories = {
    '../demo/src': '../demo/build'
}

# Template files ('source': 'template_file').
template_files = {
    '../demo/src': '../demo/src/_template.html'
}

# File encoding (should be specified to avoid file read/write errors).
file_encoding = 'UTF-8'

# Source file extension.
source_file_extension = 'md'

# Overwrite existing webpages?
overwrite_webpages = False

# Date/time zone.
# datetime.timezone.utc = UTC, None = your local time zone.
# See https://docs.python.org/3/library/datetime.html#datetime.datetime.astimezone for details.
datetime_zone = datetime.timezone.utc

# Date/time string format.
# Default value is '%Y-%m-%d %H:%M:%S UTC'.
# See https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes for details.
datetime_format = '%Y-%m-%d %H:%M:%S UTC'

# Text variables ('name': 'value').
text_variables = {
    'name': '{author}\'s Blog',
    'copyright': 'Copyright &copy; 2025 {author}.',
    'author': 'John Doe',
    'powered_by': 'Powered by <a href="https://github.com/ivan-movchan/tinyssg" target="_blank">TinySSG</a>.'
}