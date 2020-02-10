#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 14:17:33 2020

@author: Mark Buckwell
"""

# A file to store functions that I'd like to use regularly.
import os # To clear console and variables.
import numpy as np # Used for ConfigureColumns
import pandas as pd # Used for ReadCSVsToList.
import matplotlib.pyplot as plt # Used for CloseAllPlots.
import tkinter # Used for GetFileAddresses and GetTxtAddresses.
from tkinter import filedialog # Used for GetFileAddresses

# Open a dialog for the user to select one or multiple files.
def GetFileAddresses():
    tkinter.Tk().withdraw() # Prevent root winow from appearing.
    FileAddresses = filedialog.askopenfilenames()
    return(FileAddresses)

# Open a dialog for the user to select one or multiple .txt files only.
def GetTxtAddresses():
    tkinter.Tk().withdraw() # Prevent root winow from appearing.
    TxtAddresses = filedialog.askopenfilenames(filetypes=(('text files', 'txt'),))
    return(TxtAddresses)

# Read ascii data from a tuple of file addresses and output a list of lists.
# Data format not important at this point, just getting all the data imported.
def ReadTxtFilesToList(FileAddresses):
    OutputList = [open(
            FileAddresses[FileNumber], 'r', errors='ignore') for FileNumber in range(
                len(FileAddresses))]
    return(OutputList)

def ReadCSVsToList(FileAddresses, Delimiter, HeaderRows):
    OutputList = [pd.read_csv(FileAddresses[FileNumber],
                              sep = Delimiter,
                              header = HeaderRows,
                              engine = 'python'
                              ) for FileNumber in range(len(FileAddresses))]
    return(OutputList)

# Separate out list of lists into separate matrices of numerical data.
# Where each item in the list corresponds to the contents of a different file.
# Can define the number of header rows to ignore.
def ListsToMatrices(OutputList, HeaderRows):
    for FileNumber in range(len(OutputList)):
        TransferList = OutputList[FileNumber]  # Make a new list to transfer data.
        TransferArray = pd.DataFrame() # Array to handle data for each file.
        DataList = []
        HeaderRows = 0 
        for DataRow in range(len(TransferList) - HeaderRows):
            # Split out row from list item, making new row of strings.
            TransferRow = TransferList[DataRow + HeaderRows].split()
            for DataColumn in range(len(TransferRow)):
                TransferRow[DataColumn] = float(TransferRow[DataColumn])
            TransferArray = TransferArray.append(
                TransferRow, ignore_index = True)
        DataList[FileNumber] = TransferArray
    return()
            
# Close all plots.
def CloseAllPlots():
    plt.close('all')
    plt.close()
    
# CLear the console window.
def ClearConsole():
    clear = lambda: os.system('cls')
    clear()
     
# Get current working directory.
# Location = os.getcwd()
