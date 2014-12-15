#Geonames

The Geonames library parses **Geonames.org** datasets into clean & simple OGR shapefile format.

##How to Use

This very simple Command Line Interface (CLI) converts the text file into a shapefile with a single line of code.

```
$ geonames CF.txt
<Geonames - Central African Republic [15373]>
```

## Install

How to install **Fiona**

```bash
$ sudo apt-get install python-software-properties
$ sudo add-apt-repository ppa:ubuntugis/ppa
$ sudo apt-get update
$ sudo apt-get install libgdal-dev
$ pip install fiona
```

Install Geonames using **PyPi**

```bash
$ sudo pip install geonames
```

## Documentation

Download Geonames data using from [geonames.org](http://geonames.org/export/dump/)

```bash
$ wget http://download.geonames.org/export/dump/PH.zip
$ unzip PH.zip
```

Export the dataset using the Geoname's CLI

```bash
$ geonames PH.txt
<Geonames - Philippines [75003]>
```
