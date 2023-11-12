'''_____________________________________________________________________________________
@file name    : 1main.py
@description  : This file contains all the required definition
@started building on: 1.11.2022
@last modification: 05.11.2023
@author: Aatif Shaikh (v16he8m2@gmail.com)
________________________________________________________________________________________'''

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
---------------------------------imports--------------------------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
#header file which contains all imports, definition and variable link
from variable import _ERROR, _RESET, _SET
from system import FnSystemInit
from timers import FnTimerOperation

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
------------------------------start of the code--------------------------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
######################################################################
if __name__ == '__main__':
      #configure and init all the peripherals
      FnSystemInit ( )
      
      #infinite loop
      while _SET:
            #periodic time operation
            FnTimerOperation( )

