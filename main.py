import numpy as np
import cv2
cascade_names = ["A"]
cascades = [cv2.CascadeClassifier("")]
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
while True:
	for i in range(len(cascades)):
		ret, img = cap.read()
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(20, 20)
    )
    for (x,y,w,h) in cascades[i]:
        cv2.rectangle(img,(x,y),(x+w,y+h),(500,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        cv2.rectangle(img,(x,y),(x+w,y+h),(500,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = cascade_names[i]
        cv2.putText(img, text, (x, y), font, 1, (500,0,0), 2)
	cv2.imshow('video',img)
  k = cv2.waitKey(5) & 0xff
  if k == 27: # press 'ESC' to quit
      break
cap.release()
cv2.destroyAllWindows()
