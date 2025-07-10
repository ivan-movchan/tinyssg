<div align="center">

![TinySSG](images/logo.png)

# TinySSG

[English](README.md) &bull; [Russian](README-RU.md)

</div>

**TinySSG** is a minimalistic static site generator written in Python 3, developed to be simple and easy to use, especially for users who do not wish to spend time and nerves on messing with more complex generators.

TinySSG has been written by me for my personal needs and for learning the basic principles of static site generator working. However, I will be happy if someone finds my work interesting and useful.

## Installation

Python 3.9+ and [Python-Markdown](https://pypi.org/project/Markdown/) module are required.

## Usage

Download TinySSG (clone the repository or [grab the latest release](https://github.com/ivan-movchan/tinyssg/releases/latest)), then edit `config.py` module and run `tinyssg.py` module.
Running `tinyssg.py` with `-v` or `--version` flag will display the version of the script.

The first line in every source file should contain the page title. The page content (Markdown-formatted text) should begin from the third line.

In `demo` folder you can find an example of a static site that can be generated using TinySSG.

> [!WARNING]
> Python-Markdown is an implementation of *John Gruber's Markdown*, not widely used *CommonMark*. You may need to edit source files for more correct transforming source files into HTML.

## Contributing

Do not hesitate to report bugs and suggest new ideas using ["Issues"](https://github.com/ivan-movchan/tinyssg/issues) page or by contacting the developer privately. You are free to fork the repository, improve the project and send a pull request.

## Credits

- Idea and development: [Ivan Movchan](https://github.com/ivan-movchan).

## License

[MIT License](LICENSE)