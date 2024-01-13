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
from     variable   import SystemConfigPara, HttpCurrentData
from     variable   import _ERROR, _RESET, _SET
from     mqttsub    import FnMQTTManagment
from     serials    import FnSerialInit
from     threads    import FnThreadStart
from     storage    import FnFileGetFrameNumber
import   json


'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
--------------------------------------defines--------------------------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''


'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
------------------------------start of the code--------------------------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
######################################################################
def FnSystemGetConfig( ):

    #system("echo %cd%") #for windows
    try: 
        with open(ConfigFileLocation,"r") as JsonConfig:
            JsonConfig = json.load(JsonConfig)
            SystemConfigPara["SystemVehicle"]      = JsonConfig["VEHICLE NUMBER"]
            SystemConfigPara["SystemIMEI"]         = JsonConfig["IMEI"]
            SystemConfigPara["SystemHTTPURL"]      = JsonConfig["SER HTTP URL"]
            SystemConfigPara["SystemGPSMQTTURL"]   = JsonConfig["GPS MQTT URL"]
            SystemConfigPara["SystemGPSMQTTPORT"]  = JsonConfig["GPS MQTT PORT"]
            SystemConfigPara["SystemGPSMQTTTOPIC"] = JsonConfig["GPS MQTT TOPIC"]
            SystemConfigPara["SystemREBOOTNOCON"]  = JsonConfig["SYS REBOOT NOCON"]
            SystemConfigPara["SystemREBOOTTIME"]   = JsonConfig["SYS REBOOT TIME"]
            SystemConfigPara["SystemHealthPacket"] = JsonConfig["HEALTH TIME"]
            
    except Exception as error:
        if SystemDebugEnable == 1:        
            print("SYSTEM: "+str(error))


######################################################################
def FnSystemInit( ):
	
    if SystemDebugEnable == _SET:        
        print("SYSTEM: System init process started!")

    #open the file and read all the configuration
    FnSystemGetConfig( )
    HttpCurrentData["FRAME_NUMBER"] = FnFileGetFrameNumber( )

    #serial ports init
    FnSerialInit( )

    #init the tread / serail receive function
    FnThreadStart( )

    #initiate the MQTT connect
    FnMQTTManagment( )

    if SystemDebugEnable == _SET:        
        print("SYSTEM: System init process Completed!")


