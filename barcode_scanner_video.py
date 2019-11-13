from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-o","--output", type=str,default="barcode.csv",
                help ="path to output... CSV file")
args = vars(ap.parse_args())

print("[INFO] starting video stream...")
vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)

csv = open(args["output"], "w")
found = set()
run = True
while run == True:
    frame = vs.read()
    frame = imutils.resize(frame, width=400)
    barcodes = pyzbar.decode(frame)
    
    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x,y), (x+w,y+h),(0,0,255), 2)
    
        barcodeData = barcode.data.decode('utf-8')
        barcodeType = barcode.type
        
    
        text = "{}({})".format(barcodeData, barcodeType)
        cv2.putText(frame,text,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0,0,255),2)
        
    
        if barcodeData not in found:
            csv.write("{},{}\n".format(datetime.datetime.now(),
                                   barcodeData))
            csv.flush()
            found.add(barcodeData)
        if barcodeData in found:
            decodedData = barcodeData.split(',')
            print(decodedData[1], "temperature")
            run = False
            
            

        
        
        
        
    cv2.imshow("Barcode Scanner", frame)
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord("q"):
        break

print("[INFO] cleaning up...")
csv.close()
cv2.destroyAllWindows()
vs.stop()