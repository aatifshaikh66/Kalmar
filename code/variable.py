'''_____________________________________________________________________________________
@file name    : 1variable.py
@description  : This file contains all the required definition
@started building on: 1.11.2022
@last modification: 1.11.2022
@author: Aatif Shaikh (v16he8m2@gmail.com)
________________________________________________________________________________________'''

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
--------------------------------------defines--------------------------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

_ERROR = -1
_RESET =  0
_SET   =  1

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
---------------------------------gps variables---------------------------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
#these are the gps frame types
varlistgpsframetype = ["RMC","GGA","GSA","GSV","GPVTG","GLL","$PSTI,032","PSTMANTENNASTATUS"]
#an example frame of RMC frame 
varlistgpsRMC = []
#an example frame of GGA frame
varlistgpsGGA = []
#an example frame of GSA frame
varlistgpsGSA = []
#an example frame of GGA frame
varlistgpsparameter = ["0","0/0/0","0:0:0","12.12","S","21.21","N","0.0","0","0","",""]


varDeviceStatus = {
    "MQTTStatus"  : _RESET,
    "HTTPStatus"  : _RESET,
    "MQTTByte"	  : _RESET

}


'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
--------------------------------------Configuration----------------------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

#qikkle.com:8084/GPS/Api/SendDeviceData

SystemConfigPara = {
"SystemVehicle"   : "RS-01",    
"SystemIMEI"      : "NO-IMEI",
"SystemTCPIP"     : "127.0.0.1",
"SystemTCPPORT"   : "20202",
"SystemHTTPURL"   : "http://www.qikkle.com:8084/GPS/Api/SendDeviceData",
"SystemGPSMQTTURL"   : "www.qikkle.com",
"SystemGPSMQTTPORT"  : "1883",
"SystemGPSMQTTTOPIC" : "GPS Data",
"SystemREBOOTNOCON"  : "5",
"SystemREBOOTTIME"   : "00:00:05",
"SystemHealthPacket" : "70"
}

HttpCurrentData = {
"Vehicle_No"  : SystemConfigPara["SystemVehicle"],
"DeviceIMEI"  : SystemConfigPara["SystemIMEI"],
"FRAME_TYPE"  : 0, # #HEALTH, DATA
"Last_Container": "00012345",
"LOCK_UNLOCK" : "NONE",   #NONE, LOCK, UNLOCK
"GPS_STATUS"  :  "0", #str(varlistgpsparameter[0])
"Date_Time"   :  "12-12-12 12:12:12", #str(varlistgpsparameter[1]) +" "+ str(varlistgpsparameter[2]) 
"LAT"         :  "12.23",#str(varlistgpsparameter[3]), #12.23
"LAT_DIR"     :  "NS",#str(varlistgpsparameter[4]), #NS
"LON"         :  "12.23",#str(varlistgpsparameter[5]), #12.23
"LON_DIR"     :  "SW",#str(varlistgpsparameter[6]), #SW
"Speed"       :  "1.3",#str(varlistgpsparameter[7]),
"Altitude"    :  "5",#str(varlistgpsparameter[8]),
"Satellite_count": "0", #str(varlistgpsparameter[9]),
"Height"      : "0",
"Analog"      : "0.0",
"Digital"     : "0",
"FRAME_NUMBER": "0"
}
