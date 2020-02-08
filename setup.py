#!/usr/bin/env python
from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

setup(
    name='Flask-WXApp',
    version='0.1.3',
    description='Flask Extension for WeChat App.',
    long_description=readme,
    author='codeif',
    author_email='me@codeif.com',
    url='https://github.com/codeif/Flask-WXApp',
    license='MIT',
    install_requires=['requests', 'pycryptodome'],
    packages=find_packages(),
)
