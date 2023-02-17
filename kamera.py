import cv2

cap = cv2.VideoCapture(0)
while True:
	_,image = cap.read()
	image = cv2.flip(image,0)
	resize = cv2.resize(image, (1280,960))
	cv2.imshow("live vid", resize)
	if(cv2.waitKey(1)==ord("q")):
		break
cap.release()
cv2.destroyAllWindows()
