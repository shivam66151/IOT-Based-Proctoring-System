import cv2, time

# Create an object. Zero for external Camera
video = cv2.VideoCapture(0)

a = 0

while True:
    a = a + 1
    
    # Create a frame object
    check, frame = video.read()

    print(check)
    print(frame)   #Representing image

    # COnverting to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #  SHow the frame
    cv2.imshow("Capturing", gray)

    # For press any key to out(miliseconds)
    cv2.waitKey(0)

    # for playing
    key = cv2.waitKey(1)

    if key == ord('q'):
                  break

print(a)
# Shutdown the camera
video.release()
cv2.destroyAllWindows()
