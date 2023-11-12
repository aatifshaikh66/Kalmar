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
from time     import   sleep
from variable import  _SET,_RESET,_ERROR
from variable import   varDeviceStatus, SystemConfigPara, HttpCurrentData
from mqttsub  import   FnMQTTManagment
from htppsclient import FnHTTPDataSend
from datetime import   datetime


'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
--------------------------------------defines--------------------------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

TimerCount100   = _RESET
TimerCountSec   = _RESET
TimerCountMin   = _RESET
TimerCountHour  = _RESET

TimerFlagSec    = _RESET
TimerFlagMin    = _RESET
TimerFlagHour   = _RESET

TimerMQTTConnect  = 35
TimerMQTTCount    = _RESET

TimerHealthPacket = 0


'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
---------------------------------Function definition---------------------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
######################################################################
def FnTimerInterrupt( ):
    global TimerCount100, TimerCountSec, TimerCountMin, TimerCountHour
    global TimerFlagSec,  TimerFlagMin,  TimerFlagHour 

    while True:
        sleep(0.1)
        TimerCount100 += 1
        if  TimerCount100  == 9: #lag in timer
                TimerCount100   =  _RESET
                TimerFlagSec    =  _SET
                TimerCountSec  +=  1            
        if  TimerCountSec  == 60:
                TimerCountSec   =  _RESET
                TimerFlagMin    =  _SET
                TimerCountMin  +=  1                         
        if  TimerCountMin  == 60:
                TimerCountMin   =  _RESET
                TimerFlagHour   =  _SET
                TimerCountHour +=  1             
        if  TimerCountHour  == 24:
                TimerCountSec = TimerCountMin = TimerFlagHour = _RESET

######################################################################
def FnTimerGetDateAndTime( ):

        # datetime object containing current date and time
        now = datetime.now( )
        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        return dt_string
        

######################################################################
def FnTimerOperation( ):
    global TimerCount100, TimerCountSec, TimerCountMin, TimerCountHour
    global TimerFlagSec,  TimerFlagMin,  TimerFlagHour 
    global TimerMQTTConnect, TimerMQTTCount
    global TimerHealthPacket    

    if TimerFlagSec == 1:
        TimerFlagSec  = _RESET
        timerStr = "T-"+str(TimerCountHour)+":"+str(TimerCountMin)+":"+str(TimerCountSec) 
        print(timerStr + " M-"+ str(varDeviceStatus["MQTTStatus"]))

        if varDeviceStatus["MQTTStatus"] == _RESET:
                TimerMQTTCount += 1
                print(TimerMQTTCount)
                if TimerMQTTCount == TimerMQTTConnect:
                        TimerMQTTCount = _RESET
                        FnMQTTManagment( )
                else:
                        TimerMQTTCount = _RESET

        if varDeviceStatus["HTTPStatus"] == _RESET:
                TimerHealthPacket += 1
                if int(SystemConfigPara["SystemHealthPacket"]) == TimerHealthPacket:
                        TimerHealthPacket = _RESET
                        HttpCurrentData["FRAME_NUMBER"] = str(int(HttpCurrentData["FRAME_NUMBER"]) + 1)
                        FnHTTPDataSend(HttpCurrentData)
        else:
               TimerHealthPacket = _RESET
               