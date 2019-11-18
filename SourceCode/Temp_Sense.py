import time
import busio
import board
import adafruit_amg88xx
from SerialTest import servoOn
from SerialTest import servoOff

i2c = busio.I2C(board.SCL, board.SDA)
amg = adafruit_amg88xx.AMG88XX(i2c)

def startHeating(foodTemp): #Declare main class
    
    servoOn()#When file function called stove turns on

    while not isHeated(foodTemp):  #Run Thermal Camera until correct temperature is reached
        for row in range(2,5):
            for x in range(2,5): #Boundries of camera inner 9 sensors range(2,5)
                temp = amg.pixels[row][x]
                print('{0:.1f}'.format((temp*1.8)+32), end=' || ') #temp*1.8+32 gives temp in F
            print()
        print('\n',isHeated(foodTemp), avgTemp(),'\n') #print false if not heated + average temp
        time.sleep(1)
    if isHeated(foodTemp): #pass to isHeated w foodtemp passed from Source file
        servoOff() #turns off if isHeated
        print("The temperature has been reached")
        return;


        ###ALEXASTUFF####
            ## SERVO CALL STUFF

        #################

def isHeated(foodTemp): #Checks to see if the temperature of the food within the inner 9 sections is
    acc = 0
    for row in range(2,5):
        for x in range(2,5):#same func in avgTemp but used here to compare against avgTemp
            temp = amg.pixels[row][x]
            acc += (temp*1.8)+32
    if acc/9 >= foodTemp:
        return True #returns true if food if average temperature is greater than temperature passed through
    else:
        return False#returns false if not ^^comment above^^
    
def avgTemp(): #aquires average temperature
    acc = 0
    for row in range(2,5): #temps read by 9 sensors 3x3
        for x in range(2,5): #adds all temperature and divides by 9
            temp = amg.pixels[row][x] 
            acc += (temp*1.8)+32
    return acc/9 #return average

