'''_____________________________________________________________________________________
@file name    : 3gps.py
@description  : This file contains all the required definition
@started building on: 1.11.2022
@last modification: 13.11.2022
@author: Aatif Shaikh (v16he8m2@gmail.com)
________________________________________________________________________________________'''

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
---------------------------------imports--------------------------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''


from io import StringIO
import csv
from pynmeagps import NMEAReader
from variable  import *
from variable import _ERROR, _RESET, _SET

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
--------------------------------------defines--------------------------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
#enable/ disable the debugg
_GPS_DEBUGG_PRINT = _RESET

#number of coma present in the respected frame
_GPS_FRAME_RMC_COUNT  =13
_GPS_FRAME_GGA_COUNT  =14
_GPS_FRAME_GSA_COUNT  =17
_GPS_FRAME_PSTI2_COUNT=15

#frame type 
_GPS_FRAME_TYPE_GGA  =1
_GPS_FRAME_TYPE_GSA  =2		
_GPS_FRAME_TYPE_RMC  =3		
_GPS_FRAME_TYPE_PSTI2 =4				

#parse charcater
_COMA_CHAR   = ','
_DOT_CHAR    = '.'

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
---------------------------------Function definition---------------------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
#this function is to check the number of coma present in the gps frame
def FnGPSFrameErrorCheck (frame,type):

      #check if the received frame is proper or not
      if   (type == _GPS_FRAME_TYPE_GGA)   and (frame.count(_COMA_CHAR) == _GPS_FRAME_GGA_COUNT)  : return _SET    
      elif (type == _GPS_FRAME_TYPE_GSA)   and (frame.count(_COMA_CHAR) == _GPS_FRAME_GSA_COUNT)  : return _SET
      elif (type == _GPS_FRAME_TYPE_RMC)   and (frame.count(_COMA_CHAR) == _GPS_FRAME_RMC_COUNT)  : return _SET      
      elif (type == _GPS_FRAME_TYPE_PSTI2) and (frame.count(_COMA_CHAR) == _GPS_FRAME_PSTI2_COUNT): return _SET      
      else : return _RESET #reject unwanted and incorrect frame


#parse the GGA frame, note* here frame is a list
def FnGPSParseGGA(frame):
      
      TempList = frame.split(",")
      if (TempList[6]):
         varlistgpsparameter[0] = TempList[6]
      else:
         varlistgpsparameter[0] = '0'
      
      GGAPara = NMEAReader.parse(str(frame))
      varlistgpsparameter[3] = str(GGAPara.lat)
      varlistgpsparameter[4] = str(GGAPara.NS)
      varlistgpsparameter[5] = str(GGAPara.lon)
      varlistgpsparameter[6] = str(GGAPara.EW)
      varlistgpsparameter[8] = str(GGAPara.alt)                  
      varlistgpsparameter[9] = str(GGAPara.numSV)

#parse the RMC frame, note* here frame is a list
def FnGPSParseRMC(frame):
      #nsats
      RMCPara = NMEAReader.parse(str(frame))
      #varlistgpsparameter[0] = str(GGAPara.status)
      varlistgpsparameter[1] = str(RMCPara.time)
      varlistgpsparameter[2] = str(RMCPara.date)
      varlistgpsparameter[7] = str(RMCPara.spd)
      #PrintString = "GPS: ST=" + str(varlistgpsparameter[0]) + " T/D=" + str(varlistgpsparameter[1]) +" "+ str(varlistgpsparameter[2]) + " LAT=" + str(varlistgpsparameter[3]) +" "+ str(varlistgpsparameter[4]) + " LON=" + str(varlistgpsparameter[5]) +" "+ str(varlistgpsparameter[6])
      #if _GPS_DEBUGG_PRINT == 1:
      #   print(PrintString)

#varlistgpsframetype = ["RMC","GGA","GSA","GSV","GPVTG","GLL","$PSTI,032","PSTMANTENNASTATUS"]
#gprs frame parse
def FnGPSFrameParse(frame):
    #to check and parse the frame 
    varFrameType = _ERROR
    #convert the string to IO file stream 
    varIOstream = StringIO(frame) 
    #convert the IO file stream to CSV file
    varCSVConvo = csv.reader(varIOstream, delimiter=_COMA_CHAR)
    #check the gps type of frame
    if    frame.find(varlistgpsframetype[0]) != _ERROR : #RMC
          #check if the frame is proper or not            
          if FnGPSFrameErrorCheck(frame,_GPS_FRAME_TYPE_RMC) == _SET:          
             #copy the csv data into the list  
             varlistgpsRMC = list(varCSVConvo)     
             #remove the nested list created by previous command                 
             varlistgpsRMC = varlistgpsRMC[0]
             #_GPS_FRAME_TYPE_RMC  indicate that the frame is RMC
             varFrameType = _GPS_FRAME_TYPE_RMC   
             #put the data in log
             if _GPS_DEBUGG_PRINT == 1:
                print("GPS: RMC Frame="+ str(varlistgpsRMC))
             #parse the frame   
             FnGPSParseRMC(frame)                  
          else:
             #_ERROR  indicate that the frame is unwanted
             varFrameType = _ERROR   
             if _GPS_DEBUGG_PRINT == 1:
                print("GPS: RMC Frame error="+ str(frame))      

    elif  frame.find(varlistgpsframetype[1]) != _ERROR : #GGA
          #check if the frame is proper or not            
          if FnGPSFrameErrorCheck(frame,_GPS_FRAME_TYPE_GGA) == _SET:                
             #copy the csv data into the list  
             varlistgpsGGA = list(varCSVConvo)
             #remove the nested list created by previous command    
             varlistgpsGGA = varlistgpsGGA[0]
             #_GPS_FRAME_TYPE_GGA  indicate that the frame is GGA
             varFrameType = _GPS_FRAME_TYPE_GGA   
             #put the data in log
             if _GPS_DEBUGG_PRINT == 1:
                print("GPS: GGA Frame="+ str(varlistgpsGGA))          
             #parse the frame
             FnGPSParseGGA(frame)   
          else:
             #_ERROR  indicate that the frame is unwanted
             varFrameType = _ERROR   
             if _GPS_DEBUGG_PRINT == 1:
                print("GPS: GGA Frame error="+ str(frame))                      
    else:  
          #_ERROR  indicate that the frame is unwanted
          varFrameType = _ERROR
          #put the data in log
          #if _GPS_DEBUGG_PRINT == 1:
          #   print("GPS: Unknown Frame="+ str(frame))
    #return the frame type  
    return varFrameType  

