import time
import busio
import board
import adafruit_amg88xx

i2c = busio.I2C(board.SCL, board.SDA)
amg = adafruit_amg88xx.AMG88XX(i2c)

def startHeating(foodTemp): #Declare main class

    ##ALEXA STUFF##

    ###############


    while not isHeated():  #Run Thermal Camera until correct temperature is reached
        for row in range(2,5):
            for x in range(2,5):
                temp = amg.pixels[row][x]
                print('{0:.1f}'.format((temp*1.8)+32), end=' || ')
            print()
        print('\n',isHeated(foodTemp), avgTemp(),'\n')
        time.sleep(1)
    if isHeated(foodTemp):
        print("The temperature has been reached")


        ###ALEXASTUFF####


        #################

def isHeated(foodTemp):
    acc = 0
    for row in range(2,5):
        for x in range(2,5):
            temp = amg.pixels[row][x]
            acc += (temp*1.8)+32
    if acc/9 >= foodTemp:
        return True
    else:
        return False
    
def avgTemp():
    acc = 0
    for row in range(2,5):
        for x in range(2,5):
            temp = amg.pixels[row][x] 
            acc += (temp*1.8)+32
    return acc/9

