# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
  readme = f.read()

setup(
  name='scrabble_challenge',
  version='0.1.0',
  description='Scrabble coding challenge. Tells you the best Scrabble words given a particular Scrabble rack.',
  long_description=readme,
  author='Keith Johnson',
  author_email='kjohnson0451@gmail.com',
  url='https://github.com/kjohnson0451/scrabble-challenge',
  packages=find_packages(exclude=('tests', 'docs'))
)

