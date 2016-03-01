# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='elastic-twitter',
    version='0.0.1',
    description='Python agent to pull twitter data into elasticsearch',
    long_description=readme,
    author='Parag Guruji',
    author_email='paragguruji@gmail.com',
    url='https://github.com/paragguruji/elastic-twitter',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
