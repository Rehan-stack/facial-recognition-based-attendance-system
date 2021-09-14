from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector.utils import int1store
import cv2


class students :
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition Based attendance system")

        #========variables========

        self.var_dept=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_div=StringVar()
        self.var_rollno=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_advisor=StringVar()
        self.var_name=StringVar()
        


        img = Image.open(r"C:\Users\Rehan Ahmed\Desktop\face recognition system\images\logo.jpg")
        img = img.resize((500,90),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1500,height=130)


       
       
        
        
        title_lbl= Label(self.root,text="STUDENT MANAGEMENT",font=("Ariel",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=130,width=1530,height=45)

       

        #left label frame
        Left_frame = LabelFrame(root,text="student Details",bg="white",font=("Ariel",12,"bold"))
        Left_frame.place(x=20,y=180,width=640,height=530)

        #current course information
        current_course_frame = LabelFrame(Left_frame,relief=RIDGE,text="current course information",bg="white",font=("Ariel",20,"bold"))
        current_course_frame.place(x=5,y=10,width=660,height=150)
        #dept label
        dep_label = Label(current_course_frame,text="Department",font=("Ariel",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dept,font=("Ariel",12,"bold"),width=17,state="readonly")
        dep_combo["values"] = ("select department","computer science","electrical and computer engineering","chemical and material","biomedical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        #course label
        course_label = Label(current_course_frame,text="course",font=("Ariel",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("Ariel",12,"bold"),width=17,state="readonly")
        course_combo["values"] = ("select course","BSCS","BSSE","BS Information Design","BS BIOMEDICAL","BS cyber security","BS Datascience","BEEE","BECE","BSAI")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_label = Label(current_course_frame,text="year",font=("Ariel",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("Ariel",12,"bold"),width=17,state="readonly")
        year_combo["values"] = ("select Year","2K20","2K21","2K22","2K23","2K24","2K25")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester

        semester_label = Label(current_course_frame,text="semester",font=("Ariel",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("Ariel",12,"bold"),width=17,state="readonly")
        semester_combo["values"] = ("select semester","1st","2nd","3rd","4th","5th","6th","7th","8th")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #class student information
        class_student_frame = LabelFrame(Left_frame,relief=RIDGE,text="class student information",bg="white",font=("Ariel",12,"bold"))
        class_student_frame.place(x=5,y=150,width=640,height=330)

        student_id_label = Label(class_student_frame,text="student id:",font=("Ariel",12,"bold"),bg="white")
        student_id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        student_id_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("Ariel",12,"bold"))
        student_id_entry.grid(row=0,column=1,padx=10,sticky=W)
       #student name
        student_name_label = Label(class_student_frame,text="Name:",font=("Ariel",12,"bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        student_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=20,font=("Ariel",12,"bold"))
        student_name_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        #class division

        class_div_label = Label(class_student_frame,text="SECTION:",font=("Ariel",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        #class_div_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=("Ariel",12,"bold"))
        #class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        div_combo = ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("Ariel",12,"bold"),width=17,state="readonly")
        div_combo["values"] = ("select division","A","B","C","D")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #rol no
        roll_no_label = Label(class_student_frame,text="roll no:",font=("Ariel",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_rollno,width=20,font=("Ariel",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        #gender
        gender_label = Label(class_student_frame,text="gender:",font=("Ariel",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        #gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("Ariel",12,"bold"))
        #gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("Ariel",12,"bold"),width=17,state="readonly")
        gender_combo["values"] = ("select gender","male","female","shemale","other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #date of birth
        
        date_of_birth_label = Label(class_student_frame,text="DOB:",font=("Ariel",12,"bold"),bg="white")
        date_of_birth_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        date_of_birth_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("Ariel",12,"bold"))
        date_of_birth_entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)

        #email adress

        email_label = Label(class_student_frame,text="Email:",font=("Ariel",12,"bold"),bg="white")
        email_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("Ariel",12,"bold"))
        email_entry.grid(row=4,column=3,padx=2,pady=5,sticky=W)

        #phone no
        
        phone_no_label = Label(class_student_frame,text="phone no:",font=("Ariel",12,"bold"),bg="white")
        phone_no_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("Ariel",12,"bold"))
        phone_no_entry.grid(row=3,column=3,padx=5,pady=5,sticky=W)
        #Address
        
        address_label = Label(class_student_frame,text="Address:",font=("Ariel",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("Ariel",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Advisor name

        
        advisor_name_label = Label(class_student_frame,text="advisor:",font=("Ariel",12,"bold"),bg="white")
        advisor_name_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        advisor_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_advisor,width=20,font=("Ariel",12,"bold"))
        advisor_name_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)


        #radio buttons
        self.var_radio1=StringVar()
        radiobtn = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="take photo sample",value="Yes")
        radiobtn.grid(row=5,column=0)
        
        radiobtn1 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="take no photo sample",value="No")
        radiobtn1.grid(row=5,column=1)
        
        #buttons frame

        btn_frame = Frame(class_student_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=660,height=70)

        sav_btn=Button(btn_frame,width=17,text="save",command=self.add_data,font=("Ariel",11,"bold"),bg="blue",fg="white")
        sav_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,width=17,text="update",command=self.update_data,font=("Ariel",11,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,width=17,text="delete",command=self.delete_data,font=("Ariel",11,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,width=17,text="reset",command=self.reset_data,font=("Ariel",11,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        take_photo_btn=Button(btn_frame,width=17,text="take a photo sample",command=self.generate_dataset,font=("Ariel",11,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=1,column=1)

        update_photo_btn=Button(btn_frame,width=17,text="update photo sample",font=("Ariel",11,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=1,column=2)
        
           #right label frame 
        Right_frame = LabelFrame(root,text="student Details",bg="white",font=("Ariel",20,"bold"))
        Right_frame.place(x=690,y=180,width=660,height=530)

        #=========Searching system=========

        # search_frame = LabelFrame(Right_frame,relief=RIDGE,text="searching system",bg="white",font=("Ariel",11,"bold"))
        # search_frame.place(x=5,y=20,width=710,height=100)

        # search_label = Label(search_frame,text="search by:",font=("Ariel",12,"bold"),bg="white")
        # search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        # search_combo = ttk.Combobox(search_frame,font=("Ariel",12,"bold"),width=15,state="readonly")
        # search_combo["values"] = ("select","roll no","phone no")
        # search_combo.current(0)
        # search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # search_entry=ttk.Entry(search_frame,width=20,font=("Ariel",12,"bold"))
        # search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        # search_btn=Button(search_frame,width=17,text="search",font=("Ariel",11,"bold"),bg="blue",fg="white")
        # search_btn.grid(row=1,column=2)

        # show_all_btn=Button(search_frame,width=17,text="show all",font=("Ariel",11,"bold"),bg="blue",fg="white")
        # show_all_btn.grid(row=1,column=3)

        #======table frame========
        table_frame =Frame(Right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=20,width=650,height=450)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table = ttk.Treeview(table_frame,column=("dept","course","year","semester","id","name","division","rollno","gender","advisor","email","address","phone no","date of birth","take photo","take no photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading('dept',text="Department")
        self.student_table.heading('course',text="Course")
        self.student_table.heading('year',text="Year")
        self.student_table.heading('semester',text="Semester")
        self.student_table.heading('id',text="StudentID")
        self.student_table.heading('name',text="name")
        self.student_table.heading('division',text="Division")
        self.student_table.heading('rollno',text="Rollno")
        self.student_table.heading('gender',text="Gender")
        self.student_table.heading('advisor',text="Advisor")
        self.student_table.heading('email',text="Email")
        self.student_table.heading('address',text="Address")
        self.student_table.heading('phone no',text="Phone no")
        self.student_table.heading('date of birth',text="DOB")
        self.student_table.heading('take photo',text="Photosample status")
        
    
        self.student_table["show"]="headings"

        self.student_table.column("dept",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("semester",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("division",width=100)
        self.student_table.column("rollno",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("advisor",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("phone no",width=100)
        self.student_table.column("date of birth",width=100)
        self.student_table.column("take photo",width=150)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #===========functions ============

    def add_data(self):
        if self.var_dept.get()=="select department" or self.var_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="admin",database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                            self.var_dept.get(),
                                                                                            self.var_course.get(),
                                                                                            self.var_year.get(),
                                                                                            self.var_semester.get(),
                                                                                            self.var_std_id.get(),
                                                                                            self.var_name.get(),
                                                                                            self.var_div.get(),
                                                                                            self.var_rollno.get(),
                                                                                            self.var_gender.get(),
                                                                                            self.var_advisor.get(),
                                                                                            self.var_email.get(),
                                                                                            
                                                                                            self.var_address.get(),
                                                                                            self.var_phone.get(),
                                                                                            self.var_dob.get(),
                                                                                            
                                                                                            self.var_radio1.get()
    
                                                                                            ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","student detail has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("error",f"due to :{str(es)}",parent=self.root)

          
    #======fetch data=============
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="admin",database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    #======get cursor===============
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dept.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_rollno.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_advisor.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[12]),
        self.var_address.set(data[11]),
        self.var_dob.set(data[13]),
        self.var_radio1.set(data[14])

    #=update=====
    def update_data(self):
        if self.var_dept.get()=="select department" or self.var_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)

        else:
            try:
                Update=messagebox.askyesno("update","do you want to update this student details",parent=self.root)
                if Update>0:
                     conn=mysql.connector.connect(host="localhost",username="root",password="admin",database="face_recognizer")
                     my_cursor = conn.cursor()
                     my_cursor.execute("update student set dept=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,rollno=%s,gender=%s,advisor=%s,email=%s,address=%s,phoneno=%s,dateofbirth=%s,takephoto=%s where id=%s",(

                                                                                                                                                                                                      self.var_dept.get(),
                                                                                                                                                                                                      self.var_course.get(),
                                                                                                                                                                                                      self.var_year.get(),
                                                                                                                                                                                                      self.var_semester.get(),
                                                                                                                                                                                                      
                                                                                                                                                                                                      self.var_name.get(),
                                                                                                                                                                                                      self.var_div.get(),
                                                                                                                                                                                                      self.var_rollno.get(),
                                                                                                                                                                                                      self.var_gender.get(),
                                                                                                                                                                                                      self.var_advisor.get(),
                                                                                                                                                                                                      self.var_email.get(),
                                                                                            
                                                                                                                                                                                                      self.var_address.get(),
                                                                                                                                                                                                      self.var_phone.get(),
                                                                                                                                                                                                      self.var_dob.get(),
                                                                                            
                                                                                                                                                                                                      self.var_radio1.get(),
                                                                                                                                                                                                      self.var_std_id.get()
                                                                                                              
                                                                                                                                                                                                 ))
                else:
                    if not Update:
                        return 
                messagebox.showinfo("success","details updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"due to:{str(es)}",parent=self.root)
    #delete func
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("error","student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("student delete","do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="admin",database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql="delete from student where id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                                 
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","deleted details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"due to:{str(es)}",parent=self.root)
    #reset function
    def reset_data(self):
        self.var_dept.set("select department")
        self.var_course.set("select course")
        self.var_year.set("select year")
        self.var_semester.set("select semester")
        self.var_std_id.set("")
        self.var_name.set("")
        self.var_div.set("select division")
        self.var_rollno.set("")
        self.var_gender.set("select gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_advisor.set("")
        self.var_radio1.set("")

#=======generate a data set or take photo sample=
    
    def generate_dataset(self):
          if self.var_dept.get()=="select department" or self.var_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)

          else:
            try:
                 conn=mysql.connector.connect(host="localhost",username="root",password="admin",database="face_recognizer")
                 my_cursor = conn.cursor()
                 my_cursor.execute("select * from student")
                 myresult=my_cursor.fetchall()
                 id=0
                 for x in myresult:
                     id+=1
                 my_cursor.execute("update student set dept=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,rollno=%s,gender=%s,advisor=%s,email=%s,address=%s,phoneno=%s,dateofbirth=%s,takephoto=%s where id=%s",(

                                                                                                                                                                                                      self.var_dept.get(),
                                                                                                                                                                                                      self.var_course.get(),
                                                                                                                                                                                                      self.var_year.get(),
                                                                                                                                                                                                      self.var_semester.get(),
                                                                                                                                                                                                      
                                                                                                                                                                                                      self.var_name.get(),
                                                                                                                                                                                                      self.var_div.get(),
                                                                                                                                                                                                      self.var_rollno.get(),
                                                                                                                                                                                                      self.var_gender.get(),
                                                                                                                                                                                                      self.var_advisor.get(),
                                                                                                                                                                                                      self.var_email.get(),
                                                                                            
                                                                                                                                                                                                      self.var_address.get(),
                                                                                                                                                                                                      self.var_phone.get(),
                                                                                                                                                                                                      self.var_dob.get(),
                                                                                            
                                                                                                                                                                                                      self.var_radio1.get(),
                                                                                                                                                                                                      self.var_std_id.get()==id+1 
                                                                                                                                                                                    ))
                 conn.commit()
                 self.fetch_data()
                 self.reset_data()
                 conn.close()
                 #===========load predefined data on face frontals from open cv==============

                 face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                 def face_cropped(img):
                     gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                     faces=face_classifier.detectMultiScale(gray,1.3,5)
                     #scaling factor=1.3
                     #minimum neighbot=5

                     for (x,y,w,h) in faces:
                         face_cropped=img[y:y+h,x:x+w]
                         return face_cropped

                 cap=cv2.VideoCapture(0)
                 img_id=0
                 while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                         img_id+=1
                         face=cv2.resize(face_cropped(my_frame),(450,450))
                         face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                         file_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                         cv2.imwrite(file_path,face)
                         cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                         cv2.imshow("face_cropped",face)
                        

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                 cap.release()
                 cv2.destroyAllWindows()
                 messagebox.showinfo("result","generating dataset successed")

            except Exception as es:
                messagebox.showerror("Error",f"due to:{str(es)}",parent=self.root)


 

if __name__ == "__main__":
        root=Tk()
        obj=students(root)
        root.mainloop()