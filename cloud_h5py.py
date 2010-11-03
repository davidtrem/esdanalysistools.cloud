# -*- coding:utf-8 -*-
"""
Created on Nov 03, 2010

@author: David Trémouilles

Definition of an open ESD file format using h5py

A cloud is a collection of ESD Data that is opened in Satellite
All data is store in a large table with easy access
A measurement is called a droplet

"""

import h5py

def dump_cloud(filename):
    """ Create a dummy cloud with one droplet"""
    print ("Creating file: " + filename)
    h5file = h5py.File(filename, 'w')

    device1 = h5file.create_group("ESD device 1")
    device1.create_group("User Data")
    device1.create_group("User Defined")
    device1.create_group("Tester Data")
    device1.create_group("Calibration Input Data")
    device1.create_group("Raw Data")
    device1.create_group("Calibrated Data")
    device1.create_group("Extracted Data")
    device1.create_group("User Comments")

    h5file.close()

def show_cloud(filename):
    """Open an ESD data file and show one droplet"""
    print ("Openning file: " + filename)
    h5file = h5py.File(filename, 'r')

    device1 = h5file.keys()[0]
    print list(h5file)
    print ("Data in " + device1)
    print list(h5file[device1])

    h5file.close()


if __name__ == '__main__':
    dump_cloud("test2.oef")
    show_cloud("test2.oef")
