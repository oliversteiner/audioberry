# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

# with open('LICENSE') as f:
#    license = f.read()

setup(
    name='audioberry',
    version='0.1.1',
    description='Webradio-Player for RasperryPi 3 with HifiBerry AMP 2',
    long_description=readme,
    author='Oliver Steiner',
    author_email='oliver@mollo.ch',
    url='https://github.com/oliversteiner/audioberry',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)