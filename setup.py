#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'sqlparse>=0.2.1',
    'docopt',
]

setup(
    name='sqloose',
    version='0.1.0',
    description="sqloose is a less rigid SQL that allows ranges and negative indices.", 
    long_description=readme + '\n\n' + history,
    author="rdj",
    author_email='fumble.to.victory@gmail.com',
    url='https://github.com/oddacious/sqloose',
    packages=[
        'sqloose',
    ],
    package_dir={'sqloose':
                 'sqloose'},
    entry_points={
        'console_scripts': [
            'sqloose=sqloose.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='sqloose',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=requirements
)
