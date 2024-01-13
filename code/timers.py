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
from variable import   varDeviceStatus, SystemConfigPara, HttpCurrentData, varlistgpsparameter
from mqttsub  import   FnMQTTManagment
from htppsclient import FnHTTPDataSend
from datetime import   datetime
from header   import   TimerDebugEnable

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
def FnBuildHealthFrame( ):
    if HttpCurrentData["FRAME_NUMBER"] is None: 
       HttpCurrentData["FRAME_NUMBER"] = 1

    HttpCurrentData["FRAME_TYPE"] = 0
    HttpCurrentData["GPS_STATUS"]  =  str(varlistgpsparameter[0]) #0 to 5
    HttpCurrentData["Date_Time"]   =  str(varlistgpsparameter[1]) +" "+ str(varlistgpsparameter[2]) #12-12-12 12:12:12 
    HttpCurrentData["LAT"]         =  str(varlistgpsparameter[3]) #12.23
    HttpCurrentData["LAT_DIR"]     =  str(varlistgpsparameter[4]) #NS
    HttpCurrentData["LON"]         =  str(varlistgpsparameter[5]) #12.23
    HttpCurrentData["LON_DIR"]     =  str(varlistgpsparameter[6]) #SW
    HttpCurrentData["Speed"]       =  str(varlistgpsparameter[7])
    HttpCurrentData["Altitude"]    =  str(varlistgpsparameter[8])
    HttpCurrentData["Satellite_count"] = str(varlistgpsparameter[9])    

    HttpCurrentData["FRAME_NUMBER"] = str(int(HttpCurrentData["FRAME_NUMBER"]) + 1)
    FnHTTPDataSend(HttpCurrentData)

######################################################################
def FnTimerOperation( ):
    global TimerCount100, TimerCountSec, TimerCountMin, TimerCountHour
    global TimerFlagSec,  TimerFlagMin,  TimerFlagHour 
    global TimerMQTTConnect, TimerMQTTCount
    global TimerHealthPacket    

    if TimerFlagSec == 1:
        TimerFlagSec  = _RESET

        #print status 
        if TimerDebugEnable == 1:
                timerStr = "T-" + str(TimerCountHour) + ":" + str(TimerCountMin) + ":" + str(TimerCountSec) 
                GPSStr	 = " G-" + str(varlistgpsparameter[0])
                MQTTStr  = " M-"+ str(varDeviceStatus["MQTTStatus"]) + " D-" + str(varDeviceStatus["MQTTByte"])
                print(timerStr + GPSStr + MQTTStr)

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
                        FnBuildHealthFrame( )
                        
                        
        else:
               TimerHealthPacket = _RESET
              