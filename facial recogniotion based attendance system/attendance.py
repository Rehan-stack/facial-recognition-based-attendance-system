import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import constants
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector.utils import int1store
import cv2
import os
import csv
from tkinter import filedialog
from face_recognition import Face_Recognition

mydata=[]

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition Based attendance system")

        #=========variables=================

        self.var_atten_id=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_rollno=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_dept=StringVar()
        self.var_atten_attendance=StringVar()

        
        img = Image.open(r"C:\Users\Rehan Ahmed\Desktop\face recognition system\images\logo.jpg")
        img = img.resize((500,90),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1500,height=130)

        title_lbl= Label(self.root,text="Attendance Management",font=("Ariel",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=130,width=1530,height=45)
         #==========left frame===============#
        Left_frame = LabelFrame(root,text="Attendance Details",bg="white",font=("Ariel",12,"bold"))
        Left_frame.place(x=20,y=180,width=660,height=530)


        class_student_frame = LabelFrame(Left_frame,relief=RIDGE,text="class student information",bg="white",font=("Ariel",12,"bold"))
        class_student_frame.place(x=3,y=100,width=650,height=330)

        student_id_label = Label(class_student_frame,text="student id:",font=("Ariel",12,"bold"),bg="white")
        student_id_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        student_id_entry=ttk.Entry(class_student_frame,textvariable=self.var_atten_id,width=20,font=("Ariel",12,"bold"))
        student_id_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)
       #student name
        student_name_label = Label(class_student_frame,text="Name:",font=("Ariel",12,"bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        student_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_atten_name,width=20,font=("Ariel",12,"bold"))
        student_name_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        #class division

        class_div_label = Label(class_student_frame,text="Attendance status",font=("Ariel",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        #class_div_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=("Ariel",12,"bold"))
        #class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        div_combo = ttk.Combobox(class_student_frame,textvariable=self.var_atten_attendance,font=("Ariel",12,"bold"),width=17,state="readonly")
        div_combo["values"] = ("status","present","absent")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #rol no
        roll_no_label = Label(class_student_frame,text="roll no:",font=("Ariel",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_atten_rollno,width=20,font=("Ariel",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)



        #department
        
        date_of_birth_label = Label(class_student_frame,text="Department",font=("Ariel",12,"bold"),bg="white")
        date_of_birth_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        date_of_birth_entry=ttk.Entry(class_student_frame,textvariable=self.var_atten_dept,width=20,font=("Ariel",12,"bold"))
        date_of_birth_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        #Date

        email_label = Label(class_student_frame,text="Date",font=("Ariel",12,"bold"),bg="white")
        email_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_atten_date,width=20,font=("Ariel",12,"bold"))
        email_entry.grid(row=4,column=1,padx=2,pady=5,sticky=W)

        #Time
        
        phone_no_label = Label(class_student_frame,text="Time",font=("Ariel",12,"bold"),bg="white")
        phone_no_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        phone_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_atten_time,width=20,font=("Ariel",12,"bold"))
        phone_no_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)

         #=====Buttons======#
        btn_frame = Frame(class_student_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=660,height=70)

        sav_btn=Button(btn_frame,width=17,text="Import csv",command=self.import_csv,font=("Ariel",11,"bold"),bg="blue",fg="white")
        sav_btn.grid(row=1,column=0)

        update_btn=Button(btn_frame,width=17,text="Export csv",command=self.export_csv,font=("Ariel",11,"bold"),bg="blue",fg="white")
        update_btn.grid(row=1,column=1)

        delete_btn=Button(btn_frame,width=17,text="Update",command=self.action,font=("Ariel",11,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=1,column=2)

        reset_btn=Button(btn_frame,width=17,text="reset",command=self.reset_data,font=("Ariel",11,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=1,column=3)

        attend_btn=Button(btn_frame,width=17,text="Take Attendance",command=self.attendance,font=("Ariel",11,"bold"),bg="blue",fg="white")
        attend_btn.grid(row=0,column=1)








         #==========right frame==============#
        Right_frame = LabelFrame(root,text="Attendance Details",bg="white",font=("Ariel",12,"bold"))
        Right_frame.place(x=690,y=180,width=660,height=530)

        table_frame = Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=3,y=5,width=650,height=445)

        #=============scroll bar table=================

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("id","name","roll","dept","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("id",text="attendance id")
        self.AttendanceReportTable.heading("name",text="name")
        self.AttendanceReportTable.heading("roll",text="roll no")
        self.AttendanceReportTable.heading("dept",text="dept")
        self.AttendanceReportTable.heading("time",text="time")
        self.AttendanceReportTable.heading("date",text="date")
        self.AttendanceReportTable.heading("attendance",text="attendance")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("dept",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    #========face data============
    def face_data(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
#==========import csv=====
    def import_csv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="open csv",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csv_read=csv.reader(myfile,delimiter=",")
            for i in csv_read:
                mydata.append(i)
            self.face_data(mydata)

    #   =========export csv=====
    def export_csv(self):
      try:
          if len(mydata)<1:
              messagebox.showerror("No data","no data found",parent=self.root)
              return False
          fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="open csv",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
          with open(fln,mode="w",newline="") as myfile:
              exwrite=csv.writer(myfile,delimiter=",")
              for i in mydata:
                  exwrite.writerow(i)
              messagebox.showinfo("success","your data is exported"+os.path.basename(fln+"success"),parent=self.root)
      except Exception as es:
          messagebox.showerror("Error",f"due to:{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_name.set(rows[1])
        self.var_atten_rollno.set(rows[2])
        self.var_atten_dept.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])


    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_name.set("")
        self.var_atten_rollno.set("")
        self.var_atten_dept.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")

    def action(self):
        id=self.var_atten_id.get()
        roll=self.var_atten_rollno.get()
        name=self.var_atten_name.get()
        dep=self.var_atten_dept.get()
        time=self.var_atten_time.get()
        date=self.var_atten_date.get()
        attendn=self.var_atten_attendance.get()

        # write to csv file
        try:
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save CSV",filetypes=(("CSV file","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="a",newline="\n") as f:
                dict_writer=csv.DictWriter(f,fieldnames=(["id","roll no","name","dept","time","date","attendance"]))
                dict_writer.writeheader()
                dict_writer.writerow({
                "id":id,
                "roll no":roll,
                "name":name,
                "department":dep,
                "time":time,
                "date":date,
                "attendance":attendn
                    })
            messagebox.showinfo("Data Exported","Your data exported to " +os.path.basename(fln)+ " Successfully",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    

    def attendance(self):
      self.new_window=Toplevel(self.root)
      self.app=Face_Recognition(self.new_window)





if __name__ == "__main__":
        root=Tk()
        obj=Attendance(root)
        root.mainloop()