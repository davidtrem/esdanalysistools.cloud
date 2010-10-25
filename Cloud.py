# -*- coding:utf-8 -*-
"""
Created on Aug 31, 2010

@author: linten

Definition of an open ESD file format

To be defined

A cloud is a collection of ESD Data that is opened in Satellite
All data is store in a large table with easy access

"""


from tables import *

import numpy as np


def dumpCloud(Filename):

    filename = Filename
    print "Creating file:", filename
    #filter = tables.Filters()
    h5file = openFile(filename+'.oef',
         mode = "w", title = "Open ESD File Format",
    #    filters=filter
        )
    print '=' * 30
    print h5file
    print '=' * 30
    root = h5file.createGroup(h5file.root, "ESD device 1", "ESD device")
    Userdata = h5file.createGroup(root, "UserData", "User Data")

    
    UserDefinedData = h5file.createGroup(root, "UserDefinedData", "User Defined Data")
    TesterData = h5file.createGroup(root, "TesterData", "Tester Data")
    CalibrationInputData = h5file.createGroup(root, "CalibrationInputData", "Calibration Input Data")
    Data = h5file.createGroup(root, "Data", "Raw Data")
    CalibratedData = h5file.createGroup(root, "CalibratedData", "Calibrated Data")
    ExtractedData = h5file.createGroup(root, "ExtractedData", "Extracted Data")
    UserComments = h5file.createGroup(root, "UserComments", "User Defined Comments")
    
    print h5file

    h5file.close()
    
    
if __name__ == '__main__':
    
    a='test'
    dumpCloud("Test")