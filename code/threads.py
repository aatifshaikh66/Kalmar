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
from serials  import *
from variable import _ERROR, _RESET, _SET
from timers   import  FnTimerInterrupt

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
--------------------------------------defines--------------------------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
#enable/ disable the debugg
_THREAD_DEBUGG_PRINT = _SET

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
---------------------------------Function definition---------------------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

def FnThreadStart( ):
    try:
        ThreadObj1= Thread(target=FnSerialReceive)
        ThreadObj1.start()
        if _THREAD_DEBUGG_PRINT == _SET: 
            print ("Thread1 started successfully")      
    except:
        if _THREAD_DEBUGG_PRINT == _SET: 
            print ("Error: unable to start thread1")
    try:
        ThreadObj2= Thread(target=FnTimerInterrupt)
        ThreadObj2.start()
        if _THREAD_DEBUGG_PRINT == _SET: 
            print ("Thread2 started successfully")      
    except:
        if _THREAD_DEBUGG_PRINT == _SET: 
            print ("Error: unable to start thread2")            
