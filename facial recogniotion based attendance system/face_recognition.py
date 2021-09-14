from os import path
from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
from tkinter import messagebox
from cv2 import data
import mysql.connector
from mysql.connector.utils import int1store
import cv2
import os
import numpy as np
from numpy.lib.type_check import imag
from time import strftime
from datetime import datetime

class Face_Recognition :
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition Based attendance system")


        img = Image.open(r"C:\Users\Rehan Ahmed\Desktop\face recognition system\images\logo.jpg")
        img = img.resize((500,90),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1500,height=130)

        title_lbl= Label(self.root,text="ATTENDANCE",font=("Ariel",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=130,width=1530,height=45)

        b10 = tkinter.Button(self.root,text="TAKE ATTENDANCE",command=self.face_recog,font=("Ariel",30,"bold"),bg="blue",border="0",cursor="hand2")
        b10.place(x=200,y=380,width=900,height=60)
    #===marking attenance==========
    def mark_attendance(self,i,r,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
            mydatalist=f.readlines()
            name_list=[]
            for line in mydatalist:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list) ):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtstring=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{r},{d},{dtstring},{d1},Present")


    #============face recognition function=========

    def face_recog(self):
        def draw_boundry(img,classifier,scaleFactor,minNeighbors,color,text,clf):
           gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
           features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

           coord=[]

           for (x,y,w,h) in features:
             cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
             id,predict=clf.predict(gray_image[y:y+h,x:x+h])
             confidence=int((100*(1-predict/300)))
            #==fetching data from database=====

             conn=mysql.connector.connect(host="localhost",username="root",password="admin",database="face_recognizer")
             my_cursor = conn.cursor()

             my_cursor.execute("select name from student where id="+ str(id))
             n=my_cursor.fetchone()
             n="+".join(n)

             my_cursor.execute("select rollno from student where id="+ str(id))
             r=my_cursor.fetchone()
             r="+".join(r)

             my_cursor.execute("select dept from student where id="+ str(id))
             d=my_cursor.fetchone()
             d="+".join(d)

             my_cursor.execute("select id from student where id="+ str(id))
             i=my_cursor.fetchone()
             i="+".join(i)

             if confidence>77:
                 cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                 cv2.putText(img,f"Rolno:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                 cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                 cv2.putText(img,f"Dept:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                 self.mark_attendance(i,r,n,d )
             else:
                 cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                 cv2.putText(img,"UNKNOWN PERSON",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

             coord=[x,y,w,h]

           return coord

        def recognize(img,clf,facecascade):
            coord=draw_boundry(img,facecascade,1.1,10,(255,25,255),"face",clf)
            return img

        
        
        facecascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.json")

        video_cap=cv2.VideoCapture(0)

        while True:
         ret, img=video_cap.read()
         img=recognize(img,clf,facecascade)
         cv2.imshow("welcome to face recognition ",img)
         
         if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()





if __name__ == "__main__":
        root=Tk()
        obj=Face_Recognition(root)
        root.mainloop()