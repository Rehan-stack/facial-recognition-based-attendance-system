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

class Train :
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition Based attendance system")

        img = Image.open(r"C:\Users\Rehan Ahmed\Desktop\face recognition system\images\logo.jpg")
        img = img.resize((500,90),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1500,height=130)

        b1_img= Label(self.root,text="TRAIN DATA",font=("Ariel",35,"bold"),bg="white",fg="blue")
        b1_img.place(x=0,y=130,width=1530,height=45)

        b10 = tkinter.Button(self.root,text="Train Data",command=self.train_classifier,font=("Ariel",30,"bold"),bg="blue",border="0",cursor="hand2")
        b10.place(x=200,y=380,width=900,height=60)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir("data")]

        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L')#Gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training model",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #=================classifier training===========
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.json")
        cv2.destroyAllWindows()
        messagebox.showinfo("success","process completed",parent=self.root)

            


if __name__ == "__main__":
        root=Tk()
        obj=Train(root)
        root.mainloop()