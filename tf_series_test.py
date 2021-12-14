#Create date：Dec,2021
#Version: v1.0
#This program codes correspond with the Benewake TTL-USB coverter
#This program is for reference only
# -*- coding: utf-8 -*-

import serial.tools.list_ports
import time
import numpy as np

ser = serial.Serial()
ser.port = '/dev/ttyUSB1'    #set usb port
ser.baudrate = 115200        #set the baudrate of Lidar
def getTFminiData():
   while True:
      count = ser.in_waiting        #get the data length of recv
      if count > 8:
         recv = ser.read(9)         #read data and save in recv
         #print('get data from serial port:', recv)
         ser.reset_input_buffer()   #Clear input buffer
         if recv[0] == 0x59 and recv[1] == 0x59:  # python3
            distance = np.int16(recv[2] + np.int16(recv[3] << 8))
            strength = recv[4] + recv[5] * 256
            temp = (np.int16(recv[6] + np.int16(recv[7] << 8)))/8-256 #Calculate chip temperature
            print('distance = %5d  strengh = %5d  temperature = %5d' % (distance, strength, temp))
            ser.reset_input_buffer()
         if recv[0] == 'Y' and recv[1] == 'Y':  # python2 //the Ascii code of Y is 0x59
            lowD = int(recv[2].encode('hex'), 16)
            highD = int(recv[3].encode('hex'), 16)
            lowS = int(recv[4].encode('hex'), 16)
            highS = int(recv[5].encode('hex'), 16)
            lowT = int(recv[6].encode('hex'), 16)
            highT = int(recv[7].encode('hex'), 16)
            distance = np.int16(lowD + np.int16(highD << 8))
            strength = lowS + highS * 256
            temp = (np.int16(lowD + np.int16(highD << 8)))/8-256 #Calculate chip temperature
            print('distance = %5d  strengh = %5d  temperature = %5d' % (distance, strength, temp))
      else:
         time.sleep(0.005) #50ms
if __name__ == '__main__':
   try:
      if ser.is_open == False:
         try:
            ser.open()
         except:
            print('Open COM failed!')
      getTFminiData()
   except KeyboardInterrupt:  # Ctrl+C stop outputting data
      if ser != None:
         ser.close()

