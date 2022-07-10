import cv2

classifier =  cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
pic = cv2.imread('test1.jpg')
graypic= cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
bboxes = classifier.detectMultiScale(pic)
for box in bboxes:
    print(box)
for box in bboxes:
    x,y,width,height = box
    x2,y2=x+width,y+height
    cv2.rectangle(pic,(x,y),(x2,y2),(255,255,0))
    
for box in bboxes:
    print(box)
    
cv2.imshow('facedetection',pic)
cv2.waitKey()

    
