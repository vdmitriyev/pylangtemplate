from __future__ import with_statement

import os
from setuptools import setup

with open(os.path.join('pylangtemplate', 'pylangtemplate.py')) as f:
    for line in f:
        if line.startswith('__version__'):
            version = eval(line.split('=')[-1])
        if line.startswith('__description__'):
            description = eval(line.split('=')[-1])
        if line.startswith('__license__'):
            license = eval(line.split('=')[-1])
        if line.startswith('__author__'):
            author = eval(line.split('=')[-1])

setup(
    name='pylangtemplate',
    version=version,
    description=description,
    #long_description=open('README.md').read(),
    long_description=description,
    license=license,
    author=author,
    author_email='',
    classifiers=[
        'Intended Audience :: Developers',
        'Environment :: Console',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    keywords='pylangtemplate, language',
    package_dir={'': 'pylangtemplate'},
    py_modules=['pylangtemplate'],
    entry_points={
        'console_scripts': [
            'pylangtemplate = pylangtemplate:main'
        ],
    },
)
