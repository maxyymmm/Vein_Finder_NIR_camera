from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.annotate_text = "Ver 1.0"
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

# allow the camera to warmup
time.sleep(0.1)

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    imgclahe = image

    # image processing Histogram equalization and CLAHE
    for i in range(2):
        imgclahe= cv2.cvtColor(imgclahe, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(imgclahe)
        equ = cv2.equalizeHist(l)
        imgclahe  = cv2.merge((equ,a,b))
        imgclahe = imgclahe = cv2.cvtColor(imgclahe, cv2.COLOR_LAB2BGR)
        imgclahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(4+i*8,4+i*8))
        imgclahe = imgclahe.apply(l)
        imgclahe = cv2.merge((imgclahe,a,b))
        imgclahe = cv2.cvtColor(imgclahe, cv2.COLOR_LAB2BGR)
	
    # show the frame
    cv2.imshow("Vein Finder", imgclahe)
    key = cv2.waitKey(1) & 0xFF

    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
