# Required Libraries
import cv2
import numpy as np  # To convert images into array
import urllib.request # for Opening and reading url
import time 
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

cam_url = 'https://'
cv2.namedWindow("Live Streaming", cv2.WINDOW_AUTOSIZE)

count = 0

google_auth = GoogleAuth()
google_auth.LocalWebserviceAuth()
drive = GoogleDrive(google_auth)

# Google Drive folder Id
fold_id = "1vvAzTtx4RQ_mv6Pn3uZh3kEcFgnfUDrX"    

while True:
    img_response = urllib.request.urlopen(cam_url)   # Opening and reading url
    imgnp = np.array(bytearray(img_response.read()) , dtype = np.uint8)
    frame = cv2.imdecode(imgnp, -1)

    cv2.imshow("live Streaming",frame)

    key = cv2.waitKey(5)

    if key == 
