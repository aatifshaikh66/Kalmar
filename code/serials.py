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

from header   import *
from variable import _ERROR, _RESET, _SET
from gps      import FnGPSFrameParse
import serial
import time

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
--------------------------------------defines--------------------------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
GPSSerialFileStream  = _RESET
RFIDSerialFileStream = _RESET
MQTTSerialFileStream = _RESET


#enable/ disable the debugg
SERIAL_DEBUGG_PRINT = _SET

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
---------------------------------Function definition---------------------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
######################################################################
def FnSerialInit( ):

    global GPSSerialFileStream
    global RFIDSerialFileStream
    global MQTTSerialFileStream
    
    try:
        #open the serial port
        GPSSerialFileStream = serial.Serial(
        port    =configGPSComPort[0],\
        baudrate=configGPSComPort[1],\
        parity  =configGPSComPort[2],\
        stopbits=configGPSComPort[3],\
        bytesize=configGPSComPort[4],\
        timeout =configGPSComPort[5])
        #flush and clean the input and out buffer
        GPSSerialFileStream.reset_input_buffer( )
        GPSSerialFileStream.reset_output_buffer( )        
        if SERIAL_DEBUGG_PRINT == _SET:
            print("SERIAL: GPS serial init!\r")
    except:
        GPSSerialFileStream = _ERROR
        if SERIAL_DEBUGG_PRINT == _SET:
            print("SERIAL: GPS serial unable to open!\r")

    try:
        #open the serial port
        RFIDSerialFileStream = serial.Serial(
        port    =configRFIDComPort[0],\
        baudrate=configRFIDComPort[1],\
        parity  =configRFIDComPort[2],\
        stopbits=configRFIDComPort[3],\
        bytesize=configRFIDComPort[4],\
        timeout =configRFIDComPort[5])
        #flush and clean the input and out buffer
        RFIDSerialFileStream.reset_input_buffer( )
        RFIDSerialFileStream.reset_output_buffer( )        
        if SERIAL_DEBUGG_PRINT == _SET:
            print("SERIAL: RFID serial init!\r")
    except:
        RFIDSerialFileStream = _ERROR
        if SERIAL_DEBUGG_PRINT == _SET:
            print("SERIAL: RFID serial unable to open!\r")

    try:
        #open the serial port
        MQTTSerialFileStream = serial.Serial(
        port    =configMQTTComPort[0],\
        baudrate=configMQTTComPort[1],\
        parity  =configMQTTComPort[2],\
        stopbits=configMQTTComPort[3],\
        bytesize=configMQTTComPort[4],\
        timeout =configMQTTComPort[5])
        #flush and clean the input and out buffer
        MQTTSerialFileStream.reset_input_buffer( )
        MQTTSerialFileStream.reset_output_buffer( )        
        MQTTSerialFileStream.write()
        if SERIAL_DEBUGG_PRINT == _SET:
            print("SERIAL: MQTT serial init!\r")
    except:
        MQTTSerialFileStream = _ERROR
        if SERIAL_DEBUGG_PRINT == _SET:
            print("SERIAL: MQTT serial unable to open!\r")


######################################################################
def FnSerialGPSCheck(GPSString):
    #remove the new line and carrier return
    GPSString.replace('\n','')
    GPSString.replace('\r','')
    if GPSString.find('$') != _ERROR and GPSString.find('*') != _ERROR:
        return _SET
    else:
        return _RESET    

######################################################################
def FnSerialReceive( ):
    global GPSSerialFileStream
    while _SET:
        #--------------------------------------------------------
        if GPSSerialFileStream != _ERROR:
            while  GPSSerialFileStream.in_waiting:  # Or: while ser.inWaiting():
                   GPSString = GPSSerialFileStream.readline( ).decode("utf-8")
                   #check if the frame is not broken!
                   if FnSerialGPSCheck(GPSString) == _SET:                
                       FnGPSFrameParse(GPSString)                 
                   #if SERIAL_DEBUGG_PRINT == _SET:
                   #    print(str(GPSString) + str('\r'))

        #--------------------------------------------------------
        if RFIDSerialFileStream != _ERROR:
            while  RFIDSerialFileStream.in_waiting:  # Or: while ser.inWaiting():
                   RFIDString = RFIDSerialFileStream.readline( ).decode("utf-8")

        #--------------------------------------------------------                       
        time.sleep(0.01)            

######################################################################
def FnSerialGSPWrite(data):
    global MQTTSerialFileStream
    
    #--------------------------------------------------------
    if MQTTSerialFileStream != _ERROR:    
        MQTTSerialFileStream.write(data)
        MQTTSerialFileStream.flush()
