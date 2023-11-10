'''_____________________________________________________________________________________
@file name    : 0header.py
@description  : This file contains all the required definition
@started building on: 1.11.2022
@last modification: 1.11.2022
@author: Aatif Shaikh (v16he8m2@gmail.com)
________________________________________________________________________________________'''

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
---------------------------------imports--------------------------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
from io import StringIO
import csv
import time
import os
import serial
import datetime
import locale
import serial

from threading import Thread 
from stat    import S_IWUSR
from stat    import S_IREAD, S_IRGRP, S_IROTH
from locale  import atof

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
---------------------------------imports--------------------------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
                    #port, baudrate, parity, stopbit, bytesize,timeout 
configGPSComPort   =["/dev/ttyS2",115200,'N',1,8,1]
configRFIDComPort  =["/dev/ttyS3",115200,'N',1,8,1]
configMQTTComPort  =["/dev/ttyS4",115200,'N',1,8,1]

#update later
ConfigFileLocation = "configuration/config.json"

