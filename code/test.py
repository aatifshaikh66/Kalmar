from serial import Serial
from pynmeagps import NMEAReader


str1= "$GNRMC,174246.00,A,1910.07591,N,07304.50456,E,0.043,,031222,,,A,V*10"
str2= "$GNGGA,174246.00,1910.07591,N,07304.50456,E,1,07,1.98,67.0,M,-65.6,M,,*5F"
str3= "$GNGSA,A,3,06,02,11,,,,,,,,,,2.85,1.98,2.05,1*0D"


nmr = NMEAReader.parse(str1)
print(str(nmr))
nmr = NMEAReader.parse(str2)
print(str(nmr))
nmr = NMEAReader.parse(str3)
print(str(nmr))