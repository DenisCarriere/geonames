#!/usr/bin/python
# coding: utf8

import sys
import os
import geonames

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requires = ['unicodecsv>=0.9.4']

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist --formats=gztar upload')
    sys.exit()

with open('README.md') as f:
    readme = f.read()

setup(
    name='geonames',
    version=geonames.__version__,
    long_description=readme,
    description="Geonames data parser into Shapefile/KML",
    author='Denis Carriere',
    author_email='carriere.denis@gmail.com',
    url='http://addxy.com',
    download_url='https://github.com/DenisCarriere/geonames/tarball/master',
    packages=['geonames'],
    package_data={'': ['LICENSE', 'README.md']},
    package_dir={'geonames': 'geonames'},
    entry_points='''
        [console_scripts]
        geonames=geonames.cli:cli
    ''',
    include_package_data=True,
    install_requires=requires,
    zip_safe=False,
    keywords='geonames parser shapefile kml data',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ),
)
