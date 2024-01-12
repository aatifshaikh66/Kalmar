from pynmeagps import NMEAReader

strr = "$GPGGA,123519,4807.038,N,01131.000,E,1,08,,545.440,M,,,,*3C\r\n"
print(NMEAReader.parse(strr))