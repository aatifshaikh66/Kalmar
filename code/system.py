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
from     header     import *
from     variable   import SystemConfigPara
from     variable   import _ERROR, _RESET, _SET
from     mqttsub    import FnMQTTManagment
from     serials    import FnSerialInit
from     threads    import FnThreadStart
import   json
from os import system

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
--------------------------------------defines--------------------------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

#enable/ disable the debugg
SYSTEM_DEBUGG_PRINT = _SET

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
------------------------------start of the code--------------------------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
######################################################################
def FnSystemGetConfig( ):

    #system("echo %cd%") #for windows
    try: 
        with open(ConfigFileLocation,"r") as JsonConfig:
            JsonConfig = json.load(JsonConfig)

            SystemConfigPara["SystemIMEI"]         = JsonConfig["IMEI"]
            SystemConfigPara["SystemHTTPURL"]      = JsonConfig["SER HTTP URL"]
            SystemConfigPara["SystemGPSMQTTURL"]   = JsonConfig["GPS MQTT URL"]
            SystemConfigPara["SystemGPSMQTTPORT"]  = JsonConfig["GPS MQTT PORT"]
            SystemConfigPara["SystemGPSMQTTTOPIC"] = JsonConfig["GPS MQTT TOPIC"]
            SystemConfigPara["SystemREBOOTNOCON"]  = JsonConfig["SYS REBOOT NOCON"]
            SystemConfigPara["SystemREBOOTTIME"]   = JsonConfig["SYS REBOOT TIME"]

    except Exception as error:
        if SYSTEM_DEBUGG_PRINT == _SET:        
            print("SYSTEM: "+str(error))

######################################################################
def FnSystemInit( ):
    if SYSTEM_DEBUGG_PRINT == _SET:        
        print("SYSTEM: System init process started!")

    #open the file and read all the configuration
    FnSystemGetConfig( )

    #serial ports init
    FnSerialInit( )

    #init the tread / serail receive function
    FnThreadStart( )

    #initiate the MQTT connect
    FnMQTTManagment( )

    if SYSTEM_DEBUGG_PRINT == _SET:        
        print("SYSTEM: System init process Completed!")

