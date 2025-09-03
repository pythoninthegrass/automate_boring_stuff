#!/usr/bin/env python

import pathlib
from setuptools import setup

# cwd
HERE = pathlib.Path(__file__).parent

# text of README.md
README = (HERE / 'README.md').read_text()

# TODO: `error: package directory 'w' does not exist`
# `python setup.py sdist --formats=zip bdist_wheel`
# Where the magic happens
setup(
    name='webbrowser_abs',
    version='0.0.1',
    description='Open addresses in Google Maps',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/pythoninthegrass/automate_boring_stuff/tree/master/web_scraping',
    author='pythoninthegrass',
    author_email='',
    license='MIT',
    packages='webbrowser',
    include_package_data=True,
    install_requires=['pyperclip', 'sys', 'webbrowser'],
    entry_points={
        'console_scripts': [
            'webbrowser-abs=webbrowser:main'
        ]
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7"
    ]
)
