#!/usr/bin/env python
from pyclue.appSettings import VERSION, AUTHOR, AUTHOR_EMAIL, SOFTWARE_NAME, LICENCE
from setuptools import setup, find_packages


version = VERSION
author = AUTHOR
author_email = AUTHOR_EMAIL
mainteiner = AUTHOR
mainteiner_email = AUTHOR_EMAIL
licence = LICENCE




APP = ['pyclue/main.py']
DATA_FILES =[('resources',['pyclue/resources/img']),
             ('resources/keys',['pyclue/resources/keys/']),
             ('resources/main',['pyclue/resources/main/']),
             ('resources/settings',['pyclue/resources/settings/']),
    ]
OPTIONS = {
    'iconfile':'pyclue/resources/img/icon.icns',
    'argv_emulation': True,
    'includes': ['sip', 'PyQt4']
}


setup(
    app = APP,
    options = {'py2app': OPTIONS},
    data_files = DATA_FILES,
    setup_requires = ['py2app'],
    name=SOFTWARE_NAME,
    version=version,
    description='Open Source Password Manager which simplifies the task of grouping secret information in one place.',
    long_description=open('README.md').read(),
    license=licence,
    author=author,
    author_email=author_email,
    maintainer=mainteiner,
    maintainer_email=mainteiner_email,
    url='http://pyclue.org',
    download_url='http://pyclue.org',
    #packages=find_packages(),
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
            ],
    )