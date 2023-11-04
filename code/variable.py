'''_____________________________________________________________________________________
@file name    : 1variable.py
@description  : This file contains all the required definition
@started building on: 1.11.2022
@last modification: 1.11.2022
@author: Aatif Shaikh (v16he8m2@gmail.com)
________________________________________________________________________________________'''

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
---------------------------------gps variables--------------------------------------
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
varlistgpsparameter = ["","","","","","","","","","","",""]


'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
--------------------------------------defines--------------------------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
_ERROR = -1
_RESET =  0
_SET   =  1
