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

import requests
from   variable   import SystemConfigPara,HttpCurrentData
from   variable   import _ERROR,_RESET,_SET
from   storage    import FnFileStoreHistor,FnFileUpdateFrameNumber

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
--------------------------------------defines--------------------------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

#enable/ disable the debugg
STORAGE_DEBUGG_PRINT = _RESET

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
---------------------------------Function definition---------------------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
######################################################################
def FnHTTPDataSend(SendData):
    try:
        print("Sending data")
        FnFileUpdateFrameNumber(HttpCurrentData["FRAME_NUMBER"])
        res = requests.post(SystemConfigPara["SystemHTTPURL"], data=SendData)   
        if res.ok != True:
            if STORAGE_DEBUGG_PRINT == _SET:
                print("HTTP: Unable to store")
    except:
        if STORAGE_DEBUGG_PRINT == _SET:
            print("HTTP: Unable to store")

