#SmartWave SourceCode developed by Olisa Obiora for EG1003 Rapid Assembly And Design
#dependant libraries git/adafruit/amg88xx
#adapted barcode scanner code created by Adrian Rosebrock
#Alexa Api integration

from barcode_scanner_video import acquireQRData
import os

class SmartWave:

    
###Broken###
   # def openInputFile(): #precalled
       # while not os.path.exists(foodtemps.csv):
       #     print("File does not exist!")
       # return open(foodtemps.csv, "r")

    def GrabData(): #precalled
        unorganizedData = DatacquireQRData()
        orgData = organizeData(unorganizedData)
        return food

    def organizeData(self,uoData): #precalled
        orgData = []
        sData = uoData.split(',')
        return sData[0]
    
    def acquireTemp():
        inFile = open('foodtemps.csv','r')
        translateDict = {}
        for line in inFile:
            translateDict[line[0]]=line[1]
        return translateDict.get(self.GrabData())
    
    translatedFoodTemp = acquireTemp()

def main():

    newWave = SmartWave()
    newWave.translatedFoodTemp
    print(newWave)
