# Kalmar

Configure parameters
1.	Configure Device IMEI on the device. [config json file]
2.	Configure Device IP address. [Not required]
3.	Configure TCP/IP or HTTP details [config json file]
4.	Configure MQTT details for collecting GPS correction data from the base station 
5.	Configure Device Reboot time [config json file]
a.	Fix Time in day ..hour
b.	Reboot after no connection found in consecutive 5 time.
6.	Configure ALL UART port 
        Check Before start 
1.	Check Internet connection 
2.	Check Server Status
3.	Check Mqtt Status
4.	Check GPS Status
5.	Check Height Status
6.	Check ALL UART port
        Data Collection 

1.	Get Ignition Status ON/OFF
2.	Get Movement Status LK/UK
3.	Get GPS Co-ordinates
4.	Get GPS Date-time, Speed, GPS Height(if available) 
5.	Get Analog Data (like Height Sensor, Fuel Sensor)
6.	Get RFID Data
7.	Get Camera OCR Result
8.	Get Digital Input Data (Proximity Sensor Data NO/NC)

        All Setting should be configure from web browser for the device.
