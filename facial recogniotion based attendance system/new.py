
from tkinter import *
from tkinter import ttk
import tkinter
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from student import students
from train import Train
import cv2
import numpy as np
from tkinter import messagebox
from face_recognition import Face_Recognition
from attendance import Attendance
from time import strftime
from datetime import datetime




class face_recognition_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition Based attendance system")



               #logo of a university
        img = Image.open(r"C:\Users\Rehan Ahmed\Desktop\face recognition system\images\logo.jpg")
        img = img.resize((500,90),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1500,height=130)



   
        #background image
        img1 = Image.open(r"C:\Users\Rehan Ahmed\Desktop\face recognition system\images\1599119798997.jpg")
        img1 = img1.resize((1366,768),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img=Label(self.root,image=self.photoimg1)
        bg_img.place(x=0,y=130,width=1366,height=768)
        bg_img= Label(bg_img,text="PAF-IAST Facial Recognition Attendance System",font=("Ariel",35,"bold"),bg="white",fg="blue")
        bg_img.place(x=0,y=0,width=1366,height=60)

        #=========time================
        # def time():
        #   string = strftime('%H:%M:%S %p')
        #   lbl.config(text=string)
        #   lbl.after(1000, time)

        # lbl = Label(bg_img,font=("Ariel",14,"bold"),bg="white",fg="blue")
        # lbl.place(x=0,y=0,width=110,height=45)
        # time()


        #student detail button
        b1 = Button(text="Student Details",command=self.student,font=("Ariel",11,"bold"),bg="blue",border="0",cursor="hand2")
        b1.place(x=300,y=300,width=105,height=60)


        #Face detection button
        # b2 = tkinter.Button(text="Take Attendance",command=self.face_data,font=("Ariel",11,"bold"),bg="blue",border="0",cursor="hand2")
        # b2.place(x=500,y=300,width=120,height=60)
        #Attendance button
        b3 = tkinter.Button(text="Attendance Management",command=self.take_attend,font=("Ariel",11,"bold"),bg="blue",border="0",cursor="hand2")
        b3.place(x=500,y=300,width=180,height=60)
       #train button
        b4 = tkinter.Button(text="Train DATA",command=self.train_data,font=("Ariel",11,"bold"),bg="blue",border="0",cursor="hand2")
        b4.place(x=300,y=500,width=100,height=60)
       #photos
        b5 = tkinter.Button(text="Photos",command=self.open_img,font=("Ariel",11,"bold"),bg="blue",border="0",cursor="hand2")
        b5.place(x=500,y=500,width=100,height=60)
        #developer
        #b6 = tkinter.Button(text="Developer",font=("Ariel",11,"bold"),bg="blue",border="0",cursor="hand2")
        #b6.place(x=700,y=500,width=100,height=60)
       #exit button
        b6 = tkinter.Button(text="Exit",command=self.exit,font=("Ariel",11,"bold"),bg="blue",border="0",cursor="hand2")
        b6.place(x=700,y=500,width=100,height=60)
        def students_details(self):
          self.new_window=Toplevel(self.root)
          self.app=students(self.new_window)



    def open_img(self):
      os.startfile("data")

     #======function button=========

    def student(self):
      self.new_window=Toplevel(self.root)
      self.app=students(self.new_window)

    def face_data(self):
      self.new_window=Toplevel(self.root)
      self.app=Face_Recognition(self.new_window)

    def train_data(self):
      self.new_window=Toplevel(self.root)
      self.app=Train(self.new_window)

    def take_attend(self):
      self.new_window=Toplevel(self.root)
      self.app=Attendance(self.new_window)
#=====EXIT FUNCTION FROM SYSTEM================
    def exit(self):
      self.exit=messagebox.askyesno("Face recogniotion attendance system","are you sure to exit the system",parent=self.root)
      if self.exit >0:
        self.root.destroy()



if __name__ == "__main__":
        root=Tk()
        obj=face_recognition_system(root)
        root.mainloop()

