import numpy as np
import cv2 
import pickle
import os
import time
import sqlite3
from datetime import datetime
# from flask import Flask,render_template

# app=Flask(__name__)

# @app.route("/")
# def home():
# 	return render_template("index.php")



# if __name__=="__main__":
# 	app.run()
'''
conn = sqlite3.connect('Automated_attendance.db')
c = conn.cursor()
'''
name=""
face_cascade = cv2.CascadeClassifier('/home/nitish/Desktop/project/s_w/opencv-4.1.2/data/haarcascades/haarcascade_frontalface_alt2.xml')

labels = {"person-name":0}

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

with open("lables.pickle",'rb') as f:
	og_labels =pickle.load(f)
	labels={v:k for k,v in og_labels.items()}

# print (labels)

cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 200)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)

while(True):
	ret,frame=cap.read()
	# print(ret)
	gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

	faces = face_cascade.detectMultiScale(gray,scaleFactor=1.3, minNeighbors=5)
	for(x,y,w,h) in faces:
		#print(x,y,w,h)
		roi_gray = gray[y:y+h,x:x+h]
		roi_color = frame[y:y+h,x:x+h]

#recognition

		id_ ,conf = recognizer.predict(roi_gray)
		#print(labels[id_])
		if(conf > 100):
			name="unknown"
			break
		else:
			name= labels[id_]
			#print(name)
			break

		  
		color = (255,255,0)
		stroke =2
		cv2.putText(frame,name,(x,y),font,1,color,stroke,cv2.LINE_AA)

		color = (255,0,0)
		stroke = 5
		end_cord_x = x + w
		end_cord_y = y + h
		cv2.rectangle(frame ,(x,y) ,(end_cord_x, end_cord_y),color,stroke)

	#cv2.imshow('frame',frame)

	if name != "unknown":
		cv2.putText(frame, "Unlocked", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
		cv2.imshow('frame', frame)
		#cv2.imshow('Face detector', frame)
		os.system('python3 predic_test.py')
		exit(1)
	else:
		cv2.putText(frame, "login failed", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
		cv2.imshow('frame', frame)

	if cv2.waitKey(20) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()


