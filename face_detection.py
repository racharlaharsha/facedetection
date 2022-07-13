#importing opencv2 module
import cv2

#using pretrained models one by one, the cascade classifier takes file name as argument
classifier =  cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')

#reading a sample image
pic = cv2.imread('test9.jpg')

#resizing all images for consistent results and easy analysis
pic = cv2.resize(pic,(450,350))

#using the detectMultiScale function returns bounding boxes of detected faces
bboxes = classifier.detectMultiScale(pic)

#for each box a rectangle is been drawn to identify clearly
for box in bboxes:
    x,y,width,height = box
    x2,y2=x+width,y+height
    cv2.rectangle(pic,(x,y),(x2,y2),(255,255,0))


#To display the output picture with detected faces
cv2.imshow('facedetection',pic)

#wait key is used to tell how much time the output must be displayed
cv2.waitKey()
