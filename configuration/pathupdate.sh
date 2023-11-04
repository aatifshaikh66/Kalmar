#This script will build the code
#sudo pon > /home/pi/Desktop/main_pro/logs/alllogs.txt
#change the root folder to code directory
echo "CHANGED THE ROOT FOLDER"
cd /home/pi/Desktop/main_pro/codefile

#remove the executable file if it's already present
echo "REMOVED PREVIOUS CODE"
sudo rm RunMain

#compile the code 
echo "COMPILE THE CODE"
sudo c++ 1main.cpp 2serial.cpp 3dcio.cpp 4ethernethandle.cpp 5gps.cpp 6rfid.cpp 7filehandle.cpp 8Serverhandle.cpp 9timerhandler.cpp 10mqtthandle.cpp -o RunMain -lwiringPi -lpthread -lpaho-mqtt3c

#change the executable file permission
echo "CHANGE THE PERMISSION"
sudo chmod 777 RunMain

#sudo pon > /home/pi/Desktop/main_pro/logs/alllogs.txt

while true
do
	echo "RUN THE CODE"
	sudo ./RunMain	
	sleep 3
	#sudo killall RunMain
done
