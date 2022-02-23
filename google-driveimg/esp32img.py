# Required Libraries
import cv2
import numpy as np  # To convert images into array
import urllib.request # for Opening and reading url
import time 
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

cam_url = 'http://192.168.1.104'
cv2.namedWindow("Live Streaming", cv2.WINDOW_AUTOSIZE)

count = 0

google_auth = GoogleAuth()
google_auth.LocalWebserverAuth()
drive = GoogleDrive(google_auth)

# Google Drive folder Id
fold_id = "1vvAzTtx4RQ_mv6Pn3uZh3kEcFgnfUDrX"    

while True:
    img_response = urllib.request.urlopen(cam_url)   # Opening and reading url
    imgnp = np.array(bytearray(img_response.read()) , dtype = np.uint8)
    frame = cv2.imdecode(imgnp, -1)

    cv2.imshow("live Streaming",frame)

    key = cv2.waitKey(5)

    if key ==('k'):
        count += 1
        t = str(count) + '.png'
        cv2.imwrite(t,frame)
        print("Image saved as: "+t)
        f = drive.CreateFile({"parents" : [{'id' : fold_id}] , "title" : t})
        f.SetContentFile('1.png')
        f.Upload()
        print("Image successfully uploaded as: "+t)
        
        if key ==ord('q'):
         break
    else:
        continue

    cv2.destroyAllWindows()
