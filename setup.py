# -*- coding: utf-8 -*-
"""setup.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/103GOn6F-5HlXIXvMyeMsYq_39HdLMn0I
"""

from setuptools import setup, find_packages
setup(
    name = 'Topsis-Saksham-102017191',         # How you named your package folder
    packages = ['Topsis-Saksham-102017191'],   # Choose the same name as "name" defined above
    version = '0.0.1',      # Start with a small number and increase it with every change you make
    license='MIT', # Choose a license from here: https://help.github.com/articles/licensing-a-repository      
    description = 'A python package that helps you run TOPSIS (technique for order performance by similarity to ideal solution) for multi-criteria decision making',   # Give a short description about your library
    long_description = open('readme.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    long_description_content_type = "text/markdown",  
    author = 'Saksham Sood',                   # Type in your name
    author_email = 'ssood2_be20@thapar.edu',      # Type in your E-Mail
    url = 'https://github.com/sakshamsood3/Topsis-Saksham-102017191',   # Provide either the link to your github or to your website
    keywords = ['Topsis', 'TIET', 'UCS654','Thapar','implement topsis'],   # Keywords that define your package best
    packages = find_packages(),
    include_package_data = True,
    install_requires = ['pandas', 'tabulate'],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3' 
    ]
)