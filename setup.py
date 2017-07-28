from setuptools import setup, find_packages

from codecs import open
from os import path

with open(path.join('.', 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

name='psio_test'
version='0'
release='0.1.0'

setup(
    name='psio_test',
    version='0.1.0',

    description='Module to test psio, an easy access library for photon science data in different formats.', 
    long_description=long_description,

    url='https://github.com/syncope/psio_test',

    author='Ch.Rosemann',
    author_email='christoph.rosemann@desy.de',
    
    license='GPLv2',
    
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='photon science file input output test library',
    
    packages=['psio_test',],
    
    package_dir = { 'psio_test':'psio_test',},

    include_package_data=True,
)

