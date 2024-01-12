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

from paho.mqtt  import client as GPSMQTTClient
from variable   import SystemConfigPara, varDeviceStatus
from variable   import _ERROR, _RESET, _SET
from serials    import FnSerialGSPWrite
from time       import sleep


'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
--------------------------------------defines--------------------------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

#enable/ disable the debugg
MQTT_DEBUGG_PRINT = _SET

MQTTClient = GPSMQTTClient

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
---------------------------------Function definition---------------------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
######################################################################
def FnMQTTSubscribe(client: GPSMQTTClient):
    def on_message(client, userdata, msg):
        FnSerialGSPWrite(msg.payload)
        varDeviceStatus["MQTTByte"] = len(msg.payload)

    client.subscribe(SystemConfigPara["SystemGPSMQTTTOPIC"])
    client.on_message = on_message

######################################################################
def FnMQTTManagment( ) -> GPSMQTTClient:
    global MQTTClient
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            FnMQTTSubscribe(client)
            varDeviceStatus["MQTTStatus"] = _SET            
            if  MQTT_DEBUGG_PRINT == _SET:
                sleep(0.01)
                print("MQTT: Connected to MQTT Broker")
        else:
            varDeviceStatus["MQTTStatus"] = _RESET
            FnMQTTSubscribe(client)
            if  MQTT_DEBUGG_PRINT == _SET:
                print("Failed to connect, return code %d", rc)
    ######################################################################               
    def on_disconnect(client, userdata, rc):
        client.disconnect( )
        varDeviceStatus["MQTTStatus"] = _RESET
        if  MQTT_DEBUGG_PRINT == _SET:
            sleep(0.01)
            print("MQTT: Disconnected!")
    ######################################################################
    def FnMQTTConnect(client: GPSMQTTClient):
        try:
            client.connect(host=SystemConfigPara["SystemGPSMQTTURL"], 
                        port=int(SystemConfigPara["SystemGPSMQTTPORT"]))
            client.loop_start( )
        except:
            if  MQTT_DEBUGG_PRINT == _SET:
                print("MQTT: Unable to connect")

    # Set Connecting Client ID
    MQTTClient = GPSMQTTClient.Client(SystemConfigPara["SystemIMEI"])
    # client.username_pw_set(username, password)
    MQTTClient.on_connect    = on_connect
    MQTTClient.on_disconnect = on_disconnect
    FnMQTTConnect(MQTTClient)

