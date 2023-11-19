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
varlistgpsparameter = ["0","0/0/0","0:0:0","12.12","S","21.21","N","0.0","0","","",""]


varDeviceStatus = {
    "MQTTStatus"  : _RESET,
    "HTTPStatus"  : _RESET
}


'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
--------------------------------------Configuration----------------------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

SystemConfigPara = {
"SystemIMEI"      : "NO-IMEI",
"SystemTCPIP"     : "127.0.0.1",
"SystemTCPPORT"   : "20202",
"SystemHTTPURL"   : "www.qikkle.com",
"SystemGPSMQTTURL"   : "www.qikkle.com",
"SystemGPSMQTTPORT"  : "1883",
"SystemGPSMQTTTOPIC" : "GPS Data",
"SystemREBOOTNOCON"  : "5",
"SystemREBOOTTIME"   : "00:00:05",
"SystemHealthPacket" : "70"
}

HttpCurrentData = {
"FRAME_NUMBER": "0",
"FRAME_TYPE"  : "HEALTH", #HEALTH, DATA
"LOCK_UNLOCK" : "NONE",   #NONE, LOCK, UNLOCK
"GPS_STATUS"  :  str(varlistgpsparameter[0]), #0 to 5
"Date_Time"   :  str(varlistgpsparameter[1]) +" "+ str(varlistgpsparameter[2]), #12-12-12 12:12:12 
"LAT"         :  str(varlistgpsparameter[3]), #12.23
"LAT_DIR"     :  str(varlistgpsparameter[4]), #NS
"LON"         :  str(varlistgpsparameter[5]), #12.23
"LON_DIR"     :  str(varlistgpsparameter[6])  #SW
#add your parameter heres
}
