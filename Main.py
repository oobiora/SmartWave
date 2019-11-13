#SmartWave SourceCode developed by Olisa Obiora for EG1003 Rapid Assembly And Design
#dependant libraries git/adafruit/amg88xx
#adapted barcode scanner code created by Adrian Rosebrock
#Alexa Api integration

from barcode_scanner_video import acquireQRData
import os

class SmartWave:

    
    foodName = self.GrabData()
###Broken###
   # def openInputFile(): #precalled
       # while not os.path.exists(foodtemps.csv):
       #     print("File does not exist!")
       # return open(foodtemps.csv, "r")
    @classmethod
    def GrabData(self,): #precalled
        unorganizedData = DatacquireQRData()
        orgData = organizeData(unorganizedData)
        return food, self
    @classmethod
    def organizeData(cls,uoData): #precalled
        orgData = []
        sData = uoData.split(',')
        return sData[0], cls
    @classmethod
    def acquireTemp():
        inFile = open('foodtemps.csv','r')
        translateDict = {}
        for line in inFile:
            translateDict[line[0]]=line[1]
        return translateDict.get(cls.foodName)
    
    translatedFoodTemp = acquireTemp()

def main():

    newWave = SmartWave()
    newWave.translatedFoodTemp
    print(newWave)
