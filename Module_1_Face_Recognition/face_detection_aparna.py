#Importing the libraries
import cv2

#Now loading the cascades
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')

#Now we woll define the function that will do the detection
def detect(gray,frame):
    #1.3 are no of times we scaled down the image or we scaled  up the features
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    # 5 is the number of neighbors we need to have so that it gets accepted
    #By for loop we will iterate through the face and for each of the face we draw a rectangle to detect eye
    for(x,y,w,h) in faces:
        #draw a rectangle
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            #(x,y) are the coordinates of upper left corner, w is width and h is height
            #(255,0,0) is the color and 2 is width of rectangle
        region_of_interest_gray=gray[y:y+h,x:x+w]
        region_of_interest_color=frame[y:y+h,x:x+w]
        eye=eye_cascade.detectMultiScale(region_of_interest_gray,1.1,3)
        for(ex,ey,ew,eh) in eye:
        #draw a rectangle for eyes
            cv2.rectangle(region_of_interest_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    return frame           

# Face recognition with webcam
video=cv2.VideoCapture(0)
while True:
    _,frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    canvas=detect(gray,frame)
    cv2.imshow('Video',canvas) 
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
video.release()
cv2.destrouyAllWindows()



 


        