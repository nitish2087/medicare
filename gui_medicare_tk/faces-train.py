import cv2
import os
import numpy as np
from PIL import Image
import pickle

face_cascade = cv2.CascadeClassifier('/home/nitish/Desktop/project/s_w/opencv-4.1.2/data/haarcascades/haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

# if os.path.exists("trainer.yml"):
# 	recognizer.read("trainer.yml")
# 	BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 	image_dir=os.path.join(BASE_DIR,"newstudent")
# else:
   
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir=os.path.join(BASE_DIR,"images")


with open("lables.pickle",'rb') as f:
	try:
		og_labels =pickle.load(f)
		recognizer.read("trainer.yml")  
		existing_labels={v:k for k,v in og_labels.items()}
	except EOFError:
		existing_labels={}
	
	existing_image_count =len(existing_labels)


print(existing_labels)
print(existing_image_count)

current_id = existing_image_count
label_ids = existing_labels
y_labels =[]
x_train = []

count=0

for root,dirs,files in os.walk(image_dir):
	for file in files:
		if file.endswith("jpg"):
			path=os.path.join(root,file)
			label=os.path.basename(root).replace(" " ,"-").lower()
			# print(label,path)
			if not label in label_ids:
				label_ids[label] = current_id
				current_id += 1 

			if not label in existing_labels or existing_image_count==0:	
				
				id_ = label_ids[label]
				pil_image = Image.open(path)
				size = (90,90)
				final_image=pil_image.resize(size,Image.ANTIALIAS)
				image_array = np.array(final_image,"uint8")
				faces = face_cascade.detectMultiScale(image_array,
						scaleFactor=1.5,
						 minNeighbors=5)
					
				for(x,y,w,h) in faces:
					roi = image_array[y:y+h,x:x+w]
					count+=1
					x_train.append(roi)
					# print(id_)
					y_labels.append(id_)
					 
 
# print(np.array(x_train[0]))
# print(np.array(y_labels))
print(label_ids)
print(count)

# picklename = "lables.pickle"
# # Load or create a recognizer and apply training set to it
# if exists(picklename):
#     # Update existing recognizer
#     with open(picklename, "rb") as f:
#         recognizer = pickle.load(f)
#     	recognizer.train(x_train,np.array(y_labels))
#     	recognizer.update('trainer.yml')
# else:
#     # Create a brand new recognizer    
#     recognizer = cv2.face.LBPHFaceRecognizer_create()
#     recognizer.train(x_train,np.array(y_labels))
#     recognizer.update('trainer.yml')
# # Create backup
# if exists(picklename):
#     backupname = picklename + '.bak'
#     if exists(backupname):
#         os.remove(backupname)
#     os.rename(picklename, backupname)

# # Save
# with open(picklename, "wb") as f:
#     pickle.dump(label_ids, f)


# with open(picklename, "rb") as f:
#     recognizer = pickle.load(f)

if count>0:
	with open("lables.pickle",'wb') as f:
		pickle.dump(label_ids,f)

	recognizer.update(x_train,np.array(y_labels))
	recognizer.save('trainer.yml')