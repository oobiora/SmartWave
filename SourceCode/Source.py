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


def main(): #Main Function
    data = GrabData() #Call to the Gab Data Func.
    print(data)
    temp = acquireTemp(data) #passes food into acquireTemp retrieves temp
    temp = int(temp)
    startHeating(temp) #Passes temp to startHeating func in Temp_Sense File

def GrabData(): # Grabs Barcode data/food stand-in for (OR)
        unorganizedData = barcodeScanner() #Runs function within finalBarScanner
        oData = unorganizedData[1]
        return oData

def acquireTemp(data): #Converts Food name to temperature located in a CSV file 
        inFile = open('foodtemps.csv','r')
        translateDict = {}
        for line in inFile:
            line = line.split(',')
            translateDict[line[0]]=line[1] #makes a dictionary of food names and temps
        return translateDict.get(data) #finds corresponding temp to food passed in



main()


