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

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
---------------------------------imports--------------------------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
                    #port, baudrate, parity, stopbit, bytesize,timeout 
configGPSComPort   =["/dev/ttyS2",115200,'N',1,8,1]
configRFIDComPort  =["/dev/ttyS3",115200,'N',1,8,1]
configMQTTComPort  =["/dev/ttyS1",115200,'N',1,8,1]

#update later
#Configuration file
ConfigFileLocation = "../configuration/config.json"

#History File
LogsHistorFileLocation = "../logs/history.txt"

#FrameNumber File
DeviceFrameNoFileLocation = "../devicestatus/framecount.txt" 

#Enable/ Disable 
TimerDebugEnable    = 0 
SystemDebugEnable   = 1

