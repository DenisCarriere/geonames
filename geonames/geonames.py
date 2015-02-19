#!/usr/bin/python
# coding: utf8

import os
import sys
import csv
import unicodecsv
from lookup_table import feature_code, country_code
import fiona


# Increasing file size limit will prevent the error:
# _csv.Error: field larger than field limit (131072)
csv.field_size_limit(100000)


class Geonames(object):
    def __init__(self, path):
        self.container = []
        self.load(path)

    def __repr__(self):
        return self.label

    @property
    def label(self):
        return '<Geonames - {0} [{1}]>'.format(self.country, self.count)

    @property
    def country(self):
        if self.container:
            return self.container[0].get('properties').get('country')

    @property
    def count(self):
        return len(self.container)

    def load(self, path):
        file_name = os.path.basename(path)
        with open(path) as f:
            fieldnames = [
                'geonameid',
                'name',
                'asciiname',
                'alternate',
                'y',
                'x',
                'feature_class',
                'feature_code',
                'country_code',
                'cc2',
                'admin1_code',
                'admin2_code',
                'admin3_code',
                'admin4_code',
                'population',
                'elevation',
                'dem',
                'timezone',
                'modification_date'
            ]

            reader = unicodecsv.DictReader(f, fieldnames=fieldnames,
                                           dialect='excel-tab',
                                           encoding='utf-8')

            for row in reader:
                # Main Lookup
                lookup_f_code = feature_code.get(row['feature_code'])
                lookup_country = country_code.get(row['country_code'])

                # Derived Fields
                # Feature Class Lookup
                if lookup_f_code:
                    f_class = lookup_f_code.get('class')
                    f_code = lookup_f_code.get('name')
                    f_code_id = lookup_f_code.get('code')
                    summary = lookup_f_code.get('description')
                else:
                    f_class = ''
                    f_code = ''
                    f_code_id = ''
                    summary = ''

                # Country lookup
                if lookup_country:
                    continent = lookup_country.get('Continent')
                    country = lookup_country.get('Country')
                else:
                    continent = ''
                    country = ''

                # Shorten Characters to less than 80
                name = row['name'][0:80]
                summary = summary[0:80]
                alternate = row['alternate'][0:80]
                asciiname = row['asciiname'][0:80]

                # Convert to Numbers
                try:
                    x = float(row['x'])
                    y = float(row['y'])
                except:
                    x, y = 0.0, 0.0

                # Make Numbers
                try:
                    geonameid = int(row['geonameid'])
                except:
                    geonameid = 0
                try:
                    population = int(row['population'])
                except:
                    population = 0
                try:
                    elevation = int(row['elevation'])
                except:
                    elevation = 0
                try:
                    dem = int(row['dem'])
                except:
                    dem = 0

                # Create GeoJSON Feature
                geometry = {
                    'type': 'Point',
                    'coordinates': [x, y]
                }
                properties = {
                    'geonameid': geonameid,
                    'name': name,
                    'asciiname': asciiname,
                    'alternate': alternate,
                    'f_class': f_class,
                    'f_code': f_code,
                    'f_code_id': f_code_id,
                    'summary': summary,
                    'country': country,
                    'continent': continent,
                    'population': population,
                    'elevation': elevation,
                    'dem': dem,
                }
                feature = {
                    'geometry': geometry,
                    'properties': properties,
                }
                # Add the feature to retrieve later on when exporting
                self.container.append(feature)

    def make_folder(self, folder):
        if folder:
            if not os.path.exists(folder):
                os.mkdir(folder)

    def export_csv(self, path):
        path = path + '_place.csv'
        folder, file_name = os.path.split(path)
        self.make_folder(folder)
        fieldnames = [
            'name',
            'place',
            'population',
            'admin_level',
            'x',
            'y',
            'geonames:id',
            'geonames:feature_code',
        ]
        lookup_place = {
            'PPLX': 'suburb',
            'PPL': 'village',
            'PPLA': 'town',
            'PPLA2': 'town',
            'PPLA3': 'city',
            'PPLC': 'capital',
        }
        lookup_admin_level = {
            'PPLX': 9,
            'PPL': 8,
            'PPLA': 8,
            'PPLA2': 8,
            'PPLA3': 8,
            'PPLC': 6,
        }
        with open(path, 'wb') as f:
            writer = unicodecsv.DictWriter(f, fieldnames=fieldnames,
                                           extrasaction='ignore',
                                           encoding='utf-8')
            writer.writeheader()
            for feature in self.container:
                f_code_id = feature['properties']['f_code_id']
                place = lookup_place.get(f_code_id)
                name = feature['properties']['name']
                osm_feature = {
                    'place': place,
                    'admin_level': lookup_admin_level.get(f_code_id),
                    'x': feature['geometry']['coordinates'][0],
                    'y': feature['geometry']['coordinates'][1],
                    'name': name,
                    'geonames:feature_code': f_code_id,
                    'geonames:id': feature['properties']['geonameid']
                }
                population = feature['properties']['population']
                if population:
                    osm_feature['population'] = population

                if osm_feature['place']:
                    # Convert places according to population count
                    if bool(population > 10000 and place == 'village'):
                        osm_feature['place'] = 'town'
                    if bool(population > 100000 and not place in ['suburb', 'capital']):
                        osm_feature['place'] = 'city'
                    writer.writerow(osm_feature)

    def export_shp(self, path):
        path = path + '.shp'
        folder, file_name = os.path.split(path)
        self.make_folder(folder)

        encoding = 'utf-8'
        crs = {'init': 'epsg:4326'}
        driver = 'ESRI Shapefile'
        properties = [
            ('geonameid', 'int'),
            ('name', 'str'),
            ('asciiname', 'str'),
            ('alternate', 'str'),
            ('f_class', 'str'),
            ('f_code', 'str'),
            ('f_code_id', 'str'),
            ('summary', 'str'),
            ('country', 'str'),
            ('continent', 'str'),
            ('population', 'int'),
            ('elevation', 'int'),
            ('dem', 'int'),
        ]
        schema = {
            'geometry': 'Point',
            'properties': properties
        }

        with fiona.open(path, 'w',
                        driver=driver,
                        schema=schema,
                        crs=crs,
                        encoding=encoding) as sink:
            for feature in self.container:
                sink.write(feature)

if __name__ == '__main__':
    geonames = Geonames('C:\Users\GEO_Admin\Downloads\JM\JM.txt')
    geonames.export_csv('C:\Users\GEO_Admin\Downloads\JM\JM')
    print geonames

