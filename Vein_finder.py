import cv2
import time

vid = cv2.VideoCapture(0)

while True:
		ret, imgclahe = vid.read()
		imgclahe = cv2.resize(imgclahe, (1280,720))
		
		for i in  range(1):
			imgclahe= cv2.cvtColor(imgclahe, cv2.COLOR_BGR2LAB)
			l, a, b = cv2.split(imgclahe)
			equ1 = cv2.equalizeHist(l)
			imgclahe  = cv2.merge((equ1,a,b))
			imgclahe = imgclahe = cv2.cvtColor(imgclahe, cv2.COLOR_LAB2BGR)
			imgclahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(4+i*2,4+i*2))
			imgclahe = imgclahe.apply(l)
			imgclahe = cv2.merge((imgclahe,a,b))
			imgclahe = cv2.cvtColor(imgclahe, cv2.COLOR_LAB2BGR)
			cv2.imshow("Vein Finder CLAHE?", imgclahe)
		
		if(cv2.waitKey(1)==ord("q")):
			break
			
vid.release()
cv2.destroyAllWindows()
