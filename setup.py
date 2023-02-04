# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from setuptools import setup, find_packages
import re, ast

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')
	
# get version from __version__ variable in mrp/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')
version = '1.0.0'

setup(
    name='fleet',
    version=version,
    description='Fleet Management Application',
    author='Revant Nandgaonkar',
    author_email='revant.one@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
