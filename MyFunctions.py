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

def get_file_addresses():
    """
    Open a dialog for the user to select one or multiple files.
    """
    tkinter.Tk().withdraw() # Prevent root winow from appearing.
    FileAddresses = filedialog.askopenfilenames()
    return(FileAddresses)

def get_txt_addresses():
    """
    Open a dialog for the user to select one or multiple .txt files only.
    """
    tkinter.Tk().withdraw() # Prevent root winow from appearing.
    TxtAddresses = filedialog.askopenfilenames(filetypes=(('text files', 'txt'),))
    return(TxtAddresses)

def read_txt_files_to_lists(FileAddresses):
    """
    Read ascii data from a tuple of file addresses and output a list of lists.
    Data format not important at this point, just getting all the data imported.
    """
    OutputList = [open(
            FileAddresses[FileNumber], 'r', errors='ignore') for FileNumber in range(
                len(FileAddresses))]
    return(OutputList)

def read_csvs_to_lists(FileAddresses, Delimiter, HeaderRows):
    """
    Read csv data from a tuple of file addresses and output a list of dataframes.
    """
    OutputList = [pd.read_csv(FileAddresses[FileNumber],
                              sep = Delimiter,
                              header = HeaderRows,
                              engine = 'python'
                              ) for FileNumber in range(len(FileAddresses))]
    return(OutputList)


def lists_to_matrices(OutputList, HeaderRows):
    """
    Separate out list of lists into separate matrices of numerical data.
    Where each item in the list corresponds to the contents of a different file.
    Can define the number of header rows to ignore.
    """    
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
def close_all_plots():
    """
    Close all matplotlib plots.
    """
    plt.close('all')
    plt.close()
    
# CLear the console window.
def clear_console():
    """
    Clear the console window.
    """
    clear = lambda: os.system('cls')
    clear()
