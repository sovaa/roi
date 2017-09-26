#!/usr/bin/env python

from setuptools import setup, find_packages


version = '0.0.1'

setup(
    name='roi',
    version=version,
    description="Return on Investment",
    long_description="""Manage return on investments from the command line""",
    classifiers=[],
    keywords='roi',
    author='Oscar Eriksson',
    author_email='oscar.eriks@gmail.com',
    url='https://github.com/sovaa/roi',
    license='LICENSE',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'zope.interface',   # interfaces
        'pyyaml',            # configuration files
        'redis',           # redis client
        'psycopg2',
        'sqlalchemy',
        'mysqlclient',
        'fakeredis',
        'nose',
        'python-dateutil',
        'psycogreen',
        'gitpython',
        'cement',
    ])
