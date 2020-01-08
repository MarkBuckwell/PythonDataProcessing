#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 14:17:33 2020

@author: Mark Buckwell
"""

# A file to store functions that I'd like to use regularly.
#import os
import numpy as np
import tkinter # Used for GetFileAddresses, 
from tkinter import filedialog # Used for GetFileAddresses

# Get current working directory.
# Location = os.getcwd()

# Open a dialog for the user to select one or multiple files.
def GetFileAddresses():
    tkinter.Tk().withdraw() # Prevent root winow from appearing.
    FileAddresses = filedialog.askopenfilenames()
    return (FileAddresses)

# Read ascii data from a tuple of file addresses and output an array.
def ReadTxtDataFiles(FileAddresses):
    NumFiles = len(FileAddresses)
    DataArray = np.array(("TEXT",1,NumFiles))
    for FileNumber in range(NumFiles):
        CurrentFile = open(FileAddresses[FileNumber], 'r')
        DataArray[FileNumber] = CurrentFile.readlines()
    return (DataArray)
