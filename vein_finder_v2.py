from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np

if __name__ == "__main__":
    # initialize the camera and grab a reference to the raw camera capture
    camera = PiCamera()
    camera.resolution = (1280, 720)
    camera.annotate_text = "Ver 2.0"
    camera.framerate = 30 
    rawCapture = PiRGBArray(camera, size=(1280, 720 ))

    # allow the camera to warmup
    time.sleep(0.1)

    # capture frames from the camera
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        img = image
        img1 = image
        img2 = image

        cv2.imshow("ORIGINAL", img)

        # RGB to GRAY 
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        #1) CLAHE GRAY MEDIAN BLUR
        #Applying CLAHE
        for i in range (3):
            clahe = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(8+i*4,8+i*4 ))
            gray_img = clahe.apply(gray_img)

        #median filter
        median = cv2.medianBlur(gray_img, 3)

        #LAB to RGB 
        # median = cv2.cvtColor(median, cv2.COLOR_LAB2BGR)

        #----------------------------------------------------------
        # OTSU BINARIZATION
        # blur = cv2.GaussianBlur(gray_img, (5,5),0)
        # ret3,th3 = cv2.threshold(blur,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        #----------------------------------------------------------	
         # RGB to LAB 
        lab1 = cv2.cvtColor(img1, cv2.COLOR_BGR2LAB)
        #spliting 3 LAB chanells 
        l, a, b = cv2.split(lab1)

        #Applying CLAHE to l chanell
        #2)CLAHE COLOR MEDIAN BLUR AND GAUSSIAN FILTER 
        for i in range (3):
            clahe = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(8+i*4,8+i*4))
            l = clahe.apply(l)

        #merge l chanell (after CLAHE) to untouched a,b  ls
        lab1 = cv2.merge((l,a,b))

        #median filter
        median1 = cv2.medianBlur(lab1, 3)
        gaus_blur = cv2.GaussianBlur(lab1, (3,3), 0)

        #LAB to RGB 
        median1 = cv2.cvtColor(median1, cv2.COLOR_LAB2BGR)
        gaus_blur = cv2.cvtColor(gaus_blur, cv2.COLOR_LAB2BGR)

        #3)CLAHE COLOR NO FILTER (OLD)
        for i in range(3):
            img2= cv2.cvtColor(img2, cv2.COLOR_BGR2LAB)
            l, a, b = cv2.split(img2)
            equ = cv2.equalizeHist(l)
            img2  = cv2.merge((equ,a,b))
            img2 = img2 = cv2.cvtColor(img2, cv2.COLOR_LAB2BGR)
            img2 = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(4+i*8,4+i*8))
            img2 = img2.apply(l)
            img2 = cv2.merge((img2,a,b))
            img2 = cv2.cvtColor(img2, cv2.COLOR_LAB2BGR)
	
        # show the frame
        cv2.imshow("CLAHE GRAY MEDIAN BLUR", median)
        cv2.imshow("CLAHE COLOR MEDIAN BLUR", median1)
        cv2.imshow("CLAHE COLOR GAUSSIAN FILTER", gaus_blur)
        cv2.imshow("CLAHE COLOR NO FILTER (OLD)", img2)
        
        key = cv2.waitKey(1) & 0xFF

        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break
