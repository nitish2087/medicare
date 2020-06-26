from tkinter import *
import os
import os
import cv2
import sqlite3
#import faces
from PIL import ImageTk,Image
def training():
	os.system('python3 faces-train.py')
	tr = Label(screen, fg='red', text="Training Complete", font=("roboto", 8))
	tr.place(x=295,y=160)

	

def show_regis():
	'''
	screen2=Toplevel(screen)
	screen2.geometry("500x500")
	screen2.title("registered")
	conn = sqlite3.connect('Automated_attendance.db')
	c = conn.cursor()
	c.execute("SELECT * from student_details")
	records=c.fetchall()
	print(records)
	#print(type(records[0][0]))
	print_records= []
	for record in records:
		print_records += list(record) 

	query_lebel = Label(screen2, text=records)
	query_lebel.grid(row="0",column="0")
	'''
	screen2 = Toplevel(screen)
	screen2.geometry("500x500")
	screen2.title("M.E.D.I.C.A.R.E-Users")
	conn = sqlite3.connect('Automated_attendance.db')
	c = conn.cursor()
	c.execute("SELECT * from student_details")
	records = c.fetchall()
	print(records)
	name_label = Label(screen2, text="Name ", font="Arial 12 bold italic")
	name_label.grid(row=0, column=0)

	year_label = Label(screen2, text="Age", font="Arial 12 bold italic")
	year_label.grid(row=0, column=1)

	branch_label = Label(screen2, text="D.O.B", font="Arial 12 bold italic")
	branch_label.grid(row=0, column=2)

	course_label = Label(screen2, text="Address", font="Arial 12 bold italic")
	course_label.grid(row=0, column=3)
	row = 1
	print_records=""
	for record in records:
		for i in range(4):
			print_records = str(record[i]) + " "
			query_lebel = Label(screen2, text=print_records, font="Arial 12 normal normal")
			query_lebel.grid(row=row, column=i)
		row += 1

	#query_lebel = Label(screen2, text=print_records,font = "Arial 12 normal normal")
	#query_lebel.grid(row="0",column="0")
	quit = Button(screen2, text="Quit", command=screen2.destroy, font="Arial 14 bold normal", pady="10")
	quit.grid(row=row, column=3)


def recognition():
    os.system('python3 faces.py')


def capture():
	#Capture user image
	
	Id= name.get()
	cam = cv2.VideoCapture(0)
	detector=cv2.CascadeClassifier('/home/nitish/Desktop/project/s_w/opencv-4.1.2/data/haarcascades/haarcascade_frontalface_alt2.xml')

	 
	os.mkdir("images/"+Id)
	sampleNum=0
	while(sampleNum!=200):
	    ret, img = cam.read()
	    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	    faces = detector.detectMultiScale(gray,scaleFactor=1.5, minNeighbors=5)
	    for (x,y,w,h) in faces:
	        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	        
	        #incrementing sample number 
	        sampleNum=sampleNum+1
	        #saving the captured face in the dataset folder
	        #cv2.imwrite("images/user/."+Id+'.'+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
	        cv2.imwrite("images/"+Id+"/"+Id+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])

	        cv2.imshow('frame',img)

	    if cv2.waitKey(1) & sampleNum==200:
	        break
	cam.release()
	cv2.destroyAllWindows()

def data():
	#create database or connect to existing database
	conn = sqlite3.connect('Automated_attendance.db')
	c = conn.cursor()

	c.execute("""CREATE TABLE IF NOT EXISTS student_details (
			name text,
			year text,
			branch text,
			course text,
			reg_no text,
			password text
		)""")

	c.execute("Insert into student_details values(:name, :year, :branch, :course, :reg_no, :password)",
		{
			'name':name.get(),
			'year':year.get(),
			'branch':branch.get(),
			'course':course.get(),
			'reg_no':reg_no.get(),
			'password':password.get()
		})

	c.execute("SELECT *,oid from student_details")
	records = c.fetchall()
	print(records)

	conn.commit()
	conn.close()
	#register user to database	


	name.delete(0,END)
	year.delete(0,END)
	branch.delete(0,END)
	course.delete(0,END)
	reg_no.delete(0,END)
	password.delete(0,END)


def register():
	screen1=Toplevel(screen)
	screen1.geometry("500x500")
	screen1.title("M.E.D.I.C.A.R.E")
	screen1.config(bg="skyblue")

	var = Label(screen1, fg="red", height="2", text="Sign Up !!!")
	var.place(x=180, y=20)

	global name,year,branch,course,reg_no,password
	name=Entry(screen1,width="20")
	name.place(x=180,y=100)

	year=Entry(screen1,width="20")
	year.place(x=180, y=130)


	branch=Entry(screen1,width="20")
	branch.place(x=180, y=160)

	course = Entry(screen1,width="20")
	course.place(x=180, y=190)

	reg_no=Entry(screen1,width="20")
	reg_no.place(x=180, y=220)

	password = Entry(screen1,width=20)
	password.place(x=180, y=250)

	name_label=Label(screen1,text ="Name:")
	name_label.place(x=100, y=100)

	year_label=Label(screen1,text ="Age:")
	#year_label.grid(row=1,column=0)
	year_label.place(x=100, y=130)

	branch_label=Label(screen1,text ="DOB:")
	branch_label.place(x=100, y=160)

	course_label = Label(screen1,text="Address:")
	course_label.place(x=100, y=190)


	reg_label=Label(screen1,text ="Username:")
	reg_label.place(x=100, y=220)
	
	password_label=Label(screen1,text="Password:")
	password_label.place(x=100, y=250)

 
	image=Button(screen1,text="Take Image",command=capture)
	image.place(x=180, y=300)
	var=StringVar(screen1,name="str")
	var = Label(screen1, fg="red", height="2", text="")
	var.place(x=80, y=390)
	regis=Button(screen1,text="Submit data",command=data)
	regis.place(x=180, y=360)
	quit = Button(screen1, text="Quit", command=screen1.destroy)
	quit.place(x=205, y=420)

def Home():
	global screen
	screen=Tk()
	screen.geometry("400x400")
	screen.title("M.E.D.I.C.A.R.E")
	screen.config(bg="skyblue")

	var = Label(screen,fg="red",height= "2",text="M.E.D.I.C.A.R.E")

	var.place(x=140,y=20)

	register_button=Button(text= "Sign Up", height= "2", command = register)
	register_button.place(x=60,y=100)
	train_button=Button(text="Train images[Registered Users]",height= "2", command=training)
	train_button.place(x=60, y=160)
	recognize_button=Button(text= "login", height= "2", command = recognition)
	recognize_button.place(x=60, y=220)
	show_registered=Button(text="Show Registered Users",height= "2",command=show_regis)
	show_registered.place(x=60, y=280)
	quit_button=Button(text="Quit",height= "2",command=screen.destroy)
	quit_button.place(x=60, y=340)
	


	screen.mainloop()

Home()
