from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector.utils import int1store
import cv2


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition Based attendance system")

        img = Image.open(r"C:\Users\Rehan Ahmed\Desktop\face recognition system\images\logo.jpg")
        img = img.resize((500,90),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1500,height=130)

        b1_img= Label(self.root,text="Developer",font=("Ariel",35,"bold"),bg="white",fg="blue")
        b1_img.place(x=0,y=130,width=1530,height=45)












if __name__ == "__main__":
        root=Tk()
        obj=Developer(root)
        root.mainloop()