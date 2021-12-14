Benewake TFmini-S\TFmimi Plus\TFluna\TF02-Pro\TF03 Lidar-UART working in Linux(Ubuntu)-Python


Software: 
Ubuntu 18.04
Python 3.8.5
third party lib of python :
pyserial
numpy

How to install the third party libs
sudo apt-get install python3-pip
pip3 install pyserial
pip3 install numpy

Tools:
Benewake Lidar
TTL-USB converter
USB line
Computer

Check the port of device
$ls -l /dev/ttyUSB*

then change the corresponded port in code
ser.port = '/dev/ttyUSB1' 

$sudo python3 tf_series_test.py
