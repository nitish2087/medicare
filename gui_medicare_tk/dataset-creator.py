import os
import cv2
cam = cv2.VideoCapture(0)
detector=cv2.CascadeClassifier('D:\\Project\\src\\cascades\\data\\haarcascade_frontalface_alt2.xml')

Id=input('enter your id: ')
os.mkdir("newstudent/"+Id)
sampleNum=0
while(True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray,scaleFactor=1.5, minNeighbors=5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        
        #incrementing sample number 
        sampleNum=sampleNum+1
        #saving the captured face in the dataset folder
        #cv2.imwrite("images/user/."+Id+'.'+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.imwrite("newstudent/"+Id+"/"+Id+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])

        cv2.imshow('frame',img)
    if cv2.waitKey(1) & sampleNum==200:
        break
cam.release()
cv2.destroyAllWindows()