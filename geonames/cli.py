#!/usr/bin/python
# coding: utf8

import click
from geonames import Geonames
import os

@click.argument('input')
@click.command()
def cli(input):
    basename = os.path.basename(input)
    file_name, ext = os.path.splitext(basename) 
    g = Geonames(input)
    g.export_shp(file_name)
    g.export_csv(file_name)
    click.echo(g.label)

if __name__ == '__main__':
    cli()
