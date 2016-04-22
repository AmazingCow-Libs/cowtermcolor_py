#!/usr/bin/python

## Imports ##
from distutils.core import setup

setup(
    name        = "cowtermcolor",
    description = "Smart color formating for output in terminal.",
    version = "0.2.1",
    license = "GPLv3",

    author       = "n2omatt - amazingcow",
    author_email = "n2omatt@gmail.com",

    url          = 'https://github.com/AmazingCow-Libs/cowtermcolor_py',
    download_url = "https://github.com/AmazingCow-Libs/cowtermcolor_py/tarball/v0.2.1",

    py_modules = ["cowtermcolor"],

    keywords="terminal ansi color console",
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Terminals"
    ]
)
