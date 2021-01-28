#!/bin/env python3
"""
This is the setup script for the pdfCrab
Reads the README.md for the long description for the application
Reads the requirements.txt to install all proper modules for the app
TO INSTALL:
    FULL INSTALL TO PATH: python3 setup.py install
    DEV INSTALL ADD SYM LINK: python3 setup.py develop
"""
from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

with open("requirements.txt", 'r') as d:
    requirements = d.read().splitlines()

setup(
    name='pdfCrab',
    version='0.1',
    author='TrueSonOfaGun',
    author_email='idonthaveone@fake.email',
    description='Used to grab pdf file from a domain',
    long_description=long_description,
    url="https://github.com/truesonofagun/pdfCrab",
    install_requires=requirements,
    scripts=['bin/pdfCrab']
)
