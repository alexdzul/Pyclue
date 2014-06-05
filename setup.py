#!/usr/bin/env python
from pyclue.appSettings import VERSION, AUTHOR, AUTHOR_EMAIL, SOFTWARE_NAME, LICENCE
from distutils.core import setup
import py2exe


version = VERSION
author = AUTHOR
author_email = AUTHOR_EMAIL
mainteiner = AUTHOR
mainteiner_email = AUTHOR_EMAIL
licence = LICENCE
setup(
    windows=['pyclue/main.py'],
    name=SOFTWARE_NAME,
    version=version,
    description='Open Source Password Manager which simplifies the task of grouping secret information in one place.',
    long_description=open('README.md').read(),
    license=licence,
    author=author,
    author_email=author_email,
    url='http://www.github.com/alexdzul/Pyclue/',
    packages=['pyclue','pyclue.apps','pyclue.ui','pyclue.resources'],
    classifiers=[
            "Development Status :: 2 - Pre-Alpha",
            "Environment :: X11 Applications :: Qt",
            "Intended Audience :: End Users/Desktop",
            "License :: OSI Approved :: GNU General Public License (GPL)",
            "Natural Language :: English",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Topic :: Security",
            ]
    )