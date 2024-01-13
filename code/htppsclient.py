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
from   header     import HttpDebugEnable

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
--------------------------------------defines--------------------------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
---------------------------------Function definition---------------------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
######################################################################
def FnHTTPDataSend(SendData):
    try:
        if HttpDebugEnable == _SET:        
            print("Sending Data: " + str(SendData))
        FnFileUpdateFrameNumber(HttpCurrentData["FRAME_NUMBER"])
        res = requests.post(SystemConfigPara["SystemHTTPURL"], data=SendData, timeout= 10)   
        if res.ok != True:
            if HttpDebugEnable == _SET:
                print("HTTP: Unable to Send")
        else:
            if HttpDebugEnable == _SET:
                print("HTTP: Data Successfully Send")            
    except:
        if HttpDebugEnable == _SET:
            print("HTTP: Unable to connect to connecct to server!")

