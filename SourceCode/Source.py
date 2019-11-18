#import barcode_scanner_video
from finalBarScanner import barcodeScanner
from Temp_Sense import startHeating
from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2


def main():
    data = GrabData()
    print(data)
    temp = acquireTemp(data)
    temp = int(temp)
    startHeating(80)

def GrabData():
        unorganizedData = barcodeScanner()
        oData = unorganizedData[1]
        return oData

def acquireTemp(data):
        inFile = open('foodtemps.csv','r')
        translateDict = {}
        for line in inFile:
            line = line.split(',')
            translateDict[line[0]]=line[1]
        return translateDict.get(data)



main()


