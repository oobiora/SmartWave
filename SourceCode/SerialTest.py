import serial
import sys
import time

ser = serial.Serial('/dev/ttyUSB0',9600)

def servoOn():
    val = '0'   
    ser.write(val.encode('utf-8'))
def servoOff():
    val = '1'
    ser.write(val.encode('utf-8'))
