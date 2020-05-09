# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in veripro/__init__.py
from veripro import __version__ as version

setup(
	name='veripro',
	version=version,
	description='bck',
	author='suganya',
	author_email='suganya.b@groupteampro.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
