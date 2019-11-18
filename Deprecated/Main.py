#SmartWave SourceCode developed by Olisa Obiora for EG1003 Rapid Assembly And Design
#dependant libraries git/adafruit/amg88xx
#adapted barcode scanner code created by Adrian Rosebrock
#Alexa Api integration

from barcode_scanner_video import acquireQRData
import Temp_Sense
import os

class SmartWave:
    def __init__(self):
        self.food = self.GrabData()
        self.temp = self.acquireTemp()
        

    def GrabData(self,): #precalled
        unorganizedData = DatacquireQRData()
        oData = unorganizedData.split(',')
        food = oData[0]
        return food, self

    def acquireTemp(self,):
        inFile = open('foodtemps.csv','r')
        translateDict = {}
        for line in inFile:
            translateDict[line[0]]=line[1]
        return translateDict.get(self.food)
    
    translatedFoodTemp = acquireTemp()

def main():

    newWave = SmartWave()
    newWave.temp
    print(newWave)
