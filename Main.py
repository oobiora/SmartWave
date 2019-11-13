#SmartWave SourceCode developed by Olisa Obiora for EG1003 Rapid Assembly And Design
#dependant libraries git/adafruit/amg88xx
#adapted barcode scanner code created by Adrian Rosebrock
#Alexa Api integration

from barcode_scanner_video import acquireQRData
import os

class SmartWave:

    translatedFoodTemp = acquireTemp()
    
    def acquireTemp():
        inFile = openInputFile()
        traslateDict = {}
        for line in inFile:
            translateDict[line[0]]=int(line[1])
        return traslateDict.get(GrabData())

    def openInputFile(): #precalled
        while not os.path.exists(foodtemps.csv)
            print(F"File does not exist!")
        return open(foodtemps.csv, "r")
        
    

    def GrabData: #precalled
        unorganizedData = DatacquireQRData()
        orgData = organizeData(unorganizedData)
        return food

    def organizeData(uoData): #precalled
        orgData = []
        sData = uoData.split(',')
        return sData[0]

def main():

    newWave = SmartWave()
    newWave.translatedFoodTemp
    print(newWave)
