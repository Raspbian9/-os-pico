import serial
import time
ser = serial.Serial('COM9', 9600, timeout=0)
open('data.txt', 'w').close()
while 1:
   data=ser.readline()
   f = open('data.txt','a')
   print(data)
   data=str(data)
   f.write(data)
   f.close()
   time.sleep(1)
