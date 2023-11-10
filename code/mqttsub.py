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
from variable   import SystemConfigPara, varMQTTStatus
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
def FnMQTTReconnect( ):
    global MQTTClient
    try:    
        MQTTClient.connect(host=SystemConfigPara["SystemGPSMQTTURL"], 
                      port=int(SystemConfigPara["SystemGPSMQTTPORT"]))
        MQTTClient.loop_start( )
    except:
        if  MQTT_DEBUGG_PRINT == _SET:
            print("MQTT: Unable to connect")
    return MQTTClient

######################################################################
def FnMQTTConnect( ) -> GPSMQTTClient:
    global MQTTClient, varMQTTStatus
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            varMQTTStatus = _SET
            FnMQTTSubscribe(client)
            if  MQTT_DEBUGG_PRINT == _SET:
                sleep(0.01)
                print("MQTT: Connected to MQTT Broker")
        else:
            varMQTTStatus = _RESET
            FnMQTTSubscribe(client)
            if  MQTT_DEBUGG_PRINT == _SET:
                print("Failed to connect, return code %d", rc)
    def on_disconnect(client, userdata, rc):
        client.disconnect( )
        varMQTTStatus = _RESET
        if  MQTT_DEBUGG_PRINT == _SET:
            sleep(0.01)
            print("MQTT: Disconnected!")


    # Set Connecting Client ID
    MQTTClient = GPSMQTTClient.Client(SystemConfigPara["SystemIMEI"])
    # client.username_pw_set(username, password)
    MQTTClient.on_connect    = on_connect
    MQTTClient.on_disconnect = on_disconnect
    FnMQTTReconnect( )


######################################################################
def FnMQTTSubscribe(client: GPSMQTTClient):
    def on_message(client, userdata, msg):
        FnSerialGSPWrite(msg.payload)
        print(msg.payload.decode())

    client.subscribe(SystemConfigPara["SystemGPSMQTTTOPIC"])
    client.on_message = on_message

