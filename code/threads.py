'''_____________________________________________________________________________________
@file name    : threads.py
@description  : This file contains all the required definition
@started building on: 1.11.2022
@last modification: 1.11.2022
@author: Aatif Shaikh (v16he8m2@gmail.com)
________________________________________________________________________________________'''

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
---------------------------------imports--------------------------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
from header   import *
from variable import *
from serials  import *


'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
--------------------------------------defines--------------------------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
_ERROR = -1
_RESET =  0
_SET   =  1

#enable/ disable the debugg
_THREAD_DEBUGG_PRINT = _SET

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
---------------------------------Function definition---------------------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

def FnThreadStart( ):
    try:
        ThreadObj= Thread(target=FnSerialReceive)
        ThreadObj.start()
        if _THREAD_DEBUGG_PRINT == _SET: 
            print ("Thread started successfully\n\r")      
    except:
        if _THREAD_DEBUGG_PRINT == _SET: 
            print ("Error: unable to start thread\n\r")
