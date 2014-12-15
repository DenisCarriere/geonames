#!/usr/bin/python
# coding: utf8

"""
geonames library
~~~~~~~~~~~~~~~~

Geonames data parser into simple OGR Shapefile.

Geonames is an Apache2 Licensed Geocoding library, written in Python.

    $ geonames CF.txt
    <Geonames - Central African Republic [15373]>

"""

__title__ = 'geonames'
__version__ = '0.1.1'
__author__ = 'Denis Carriere'
__copyright__ = 'Copyright 2014 Denis Carriere'

from .geonames import Geonames