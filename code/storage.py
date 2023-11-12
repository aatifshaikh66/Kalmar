'''_____________________________________________________________________________________
@file name    : threads.py
@description  : This file contains all the required definition
@started building on: 1.11.2022
@last modification: 31.12.2022
@author: Aatif Shaikh (v16he8m2@gmail.com)
________________________________________________________________________________________'''

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
---------------------------------imports--------------------------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

from header     import  LogsHistorFileLocation, DeviceFrameNoFileLocation
from variable   import _ERROR, _RESET, _SET

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
--------------------------------------defines--------------------------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

#enable/ disable the debugg
STORAGE_DEBUGG_PRINT = _RESET

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
---------------------------------Function definition---------------------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
######################################################################
def FnFileStoreHistor(Data):
    
    try:
        FileHandler = open(LogsHistorFileLocation,"a")
        FileHandler.write(Data)
        FileHandler.close( )
    except:
        if STORAGE_DEBUGG_PRINT == _SET:
            print("Storage: Unable to update history")

######################################################################
def FnFileUpdateFrameNumber (Data):
    try:
        FileHandler = open(DeviceFrameNoFileLocation,"w")
        FileHandler.write(Data)
        FileHandler.close( )
    except:
        if STORAGE_DEBUGG_PRINT == _SET:
            print("Storage: Unable to update Frame Number")

######################################################################
def FnFileGetFrameNumber ( ):
    try:
        FileHandler = open(DeviceFrameNoFileLocation,"r")
        Data = FileHandler.read( )
        FileHandler.close( )
        if len(Data) == _RESET:
            FnFileUpdateFrameNumber('1')
            return '0'
        else:
            return Data
    except:
        if STORAGE_DEBUGG_PRINT == _SET:
            print("Storage: Unable to get Frame Number")

