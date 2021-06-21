from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import ttk,messagebox
import pymysql
import random
import time
import datetime

def main():
    root=Tk()
    app=FirstPage(root)

class FirstPage:
    def __init__(self,master):
        self.master=master
        self.master.title("College Management")
        self.master.geometry("700x300+0+0")
        self.master.maxsize(500, 300)
        self.master.minsize(500, 300)
        self.master.config(bg='cadet blue')
        self.frame=Frame(self.master,bg='cadet blue')
        self.frame.pack()

        self.Username=StringVar()
        self.Password=StringVar()

        
        self.lblTitle=Label(self.frame,text="College Management System",font=("arial",20,'bold'),bg='cadet blue',fg='Cornsilk')
        self.lblTitle.grid(row=0,column=0,columnspan=2,pady=10,padx=10)


   #=====================================ADMIN , STUDENT AND FACULTY BUTTONS=======================================================================

        self.btnAdmin= Button(self.frame,text="ADMIN",width=15,height=3,font=('arial',10,'bold'),bg='Cornsilk',fg='cadet blue',command = self.x)
        self.btnAdmin.grid(row=1,column=0,sticky="e")

        self.btnStd= Button(self.frame,text="STUDENT",width=15,height=3,font=('arial',10,'bold'),bg='Cornsilk',fg='cadet blue',command = self.y)
        self.btnStd.grid(row=2,column=0,sticky="e")

        self.btnFac= Button(self.frame,text="FACULTY",width=15,height=3,font=('arial',10,'bold'),bg='Cornsilk',fg='cadet blue',command = self.z)
        self.btnFac.grid(row=3,column=0,sticky="e")

        

   #=====================================ADMIN , STUDENT AND FACULTY BUTTONS=======================================================================

    def x(self):
        self.newWindow=Toplevel(self.master)
        self.app= Window1(self.newWindow)

    def y(self):
        self.newWindow = Toplevel(self.master)
        self.app = StudentManagement(self.newWindow)

    def z(self):
        self.newWindow = Toplevel(self.master)
        self.app = FacultyManagement(self.newWindow)




        #============================================================STUDENT MANAGEMENT==================================================================================
class StudentManagement:
    def __init__(self,master):
        self.master = master
        self.master.title("Student Management System")
        self.master.geometry("1350x700+0+0")
        self.master.config(bg = 'cadet blue')
        self.frame=Frame(self.master,bg='cadet blue')
        self.frame.pack()

        self.Username=StringVar()
        self.Password=StringVar()

        Manage_Frame1=Frame(self.master,bd=4,relief=RIDGE,bg="cornsilk")
        Manage_Frame1.place(x=250,y=100,width=850,height=550)

        title=Label(Manage_Frame1,text="Welcome students:",bg="cornsilk",fg="cadet blue",font=("times new roman",20,"bold"))
        title.place(x=5,y=1,width=220,height=80)

        Manage_Frame2=Frame(self.master,bd=4,relief=RIDGE,bg="cornsilk")
        Manage_Frame2.place(x=350,y=170,width=650,height=350)


       
        u_name=Label(Manage_Frame2,text="Username",bg="cornsilk",fg="grey",font=("times new roman",15,"bold"))
        u_name.place(x=150,y=70)

        self.textUsername=Entry(Manage_Frame2,font=("times new roman",15),bg='lightgrey',textvariable=self.Username)
        self.textUsername.place(x=270,y=70,width=250)

        p_name=Label(Manage_Frame2,text="Password",bg="cornsilk",fg="grey",font=("times new roman",15,"bold"))
        p_name.place(x=150,y=110)

        self.textPassword=Entry(Manage_Frame2,font=("times new roman",15),bg='lightgrey',textvariable=self.Password)
        self.textPassword.place(x=270,y=110,width=250)

        #=============================================================student page button====================================================

        self.btnlogin= Button(Manage_Frame2,text="Login",width=5,font=('times new roman',17,'italic'),bg='cadet blue',fg='Cornsilk',command=self.Login_system)
        self.btnlogin.place(x=135,y=225,width=120)

        self.btnreset= Button(Manage_Frame2,text="Reset",width=5,font=('times new roman',17,'italic'),bg='cadet blue',fg='Cornsilk', command=self.iReset)
        self.btnreset.place(x=265,y=225,width=120)

        self.btnexit= Button(Manage_Frame2,text="Exit",width=5,font=('times new roman',17,'italic'),bg='cadet blue',fg='Cornsilk', command=self.iExit)
        self.btnexit.place(x=395,y=225,width=120)

        Manage_Frame3=Frame(self.master,bd=4,relief=RIDGE,bg="cornsilk")
        Manage_Frame3.place(x=350,y=520,width=650,height=60)

        self.btnstudent= Button(Manage_Frame3,text="View Profile",width=25,font=('arial',12,'bold'),bg='cadet blue',fg='Cornsilk',state=DISABLED,
                                command=self.reg)
        self.btnstudent.place(x=55,y=10)
         
        self.btnfaculty= Button(Manage_Frame3,text="View Performance",width=25,font=('arial',12,'bold'),bg='cadet blue',fg='Cornsilk',state=DISABLED,
                                command=self.g)
        self.btnfaculty.place(x=325,y=10)


        
      #===========================================student fxn=================================================================================


    def Login_system(self):
        user = (self.Username.get())
        pas = (self.Password.get())
        if(user==str(1234) and pas == str(2345)):
            self.btnstudent.config(state=NORMAL)
            self.btnfaculty.config(state=NORMAL)
            
        else :
            self.Username.set("")
            self.Password.set("")
            
            messagebox.showerror("Error","All fields are required",parent=self.master)
            
            
        
            try:
                con=pymysql.connect(host="localhost",user="root",password="",db="management")
                cur=con.cursor()
                if cur.execute("SELECT * FROM user WHERE username=%s AND password=%s AND designation='Student'",(self.Username.get(),self.Password.get())):
                    row=cur.fetchone()
                    if row==None:
                        messagebox.showerror("Error","Invalid USERNAME & PASSWORD",parent=self.master)
                    
                    else:
                        messagebox.showinfo("success","Welcome",parent=self.master)
                        self.btnstudent.config(state =NORMAL)
                        self.btnfaculty.config(state =DISABLED)
                elif cur.execute("SELECT * FROM user WHERE username=%s AND password=%s AND designation='Faculty Member'",(self.Username.get(),self.Password.get())):

                    row=cur.fetchone()
                    if row==None:
                        messagebox.showerror("Error","Invalid USERNAME & PASSWORD",parent=self.master)
                    
                    else:
                        messagebox.showinfo("success","Welcome",parent=self.master)
                        self.btnfaculty.config(state =NORMAL)
                        self.btnstudent.config(state =DISABLED)
                else:
                     messagebox.showerror("error","error handle,(str(es))",parent=self.master)
            except Exception as es:
                messagebox.showerror("error","error handle,(str(es))",parent=self.master)


    def iReset(self):
        self.btnstudent.config(state =DISABLED)
        self.btnfaculty.config(state =DISABLED)
        self.Username.set("")
        self.Password.set("")
        self.textUsername.focus()

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("College Login Sytem","Confirm if you want to exit")
        if self.iExit>0:
            self.master.destroy()
            return
    
    def reg(self):
        self.newWindow=Toplevel(self.master)
        self.app= CollegeRegistration(self.newWindow)

    def manage(self):
        self.newWindow=Toplevel(self.master)
        self.app= CollegeManagement(self.newWindow)
    def g(self):
        self.newWindow=Toplevel(self.master)
        self.app= Window_g(self.newWindow)

class Window_g:
    def __init__(self,master):
        self.master=master
        self.master.title("College Management")
        self.master.geometry("700x300+0+0")
        self.master.maxsize(500, 300)
        self.master.minsize(500, 300)
        self.master.config(bg='cadet blue')
        self.frame=Frame(self.master,bg='cadet blue')
        self.frame.pack()

        self.lblTitle=Label(self.frame,text="College Management System",font=("arial",20,'bold'),bg='cadet blue',fg='Cornsilk')
        self.lblTitle.grid(row=0,column=0,columnspan=2,pady=10,padx=10)


        #=====================================ADMIN , STUDENT AND FACULTY BUTTONS=======================================================================

        self.btnAdmin= Button(self.frame,text="View Attendance",width=15,height=3,font=('arial',10,'bold'),bg='Cornsilk',fg='cadet blue')
        self.btnAdmin.grid(row=1,column=0,sticky="e")

        self.btnStd= Button(self.frame,text="View Marksheet",width=15,height=3,font=('arial',10,'bold'),bg='Cornsilk',fg='cadet blue')
        self.btnStd.grid(row=2,column=0,sticky="e")

    

#====================================================FACULTY MANAGEMENT=============================================================================================

class FacultyManagement:
    def __init__(self,master):
        self.master = master
        self.master.title("Faculty Management System")
        self.master.geometry("1350x700+0+0")
        self.master.config(bg = 'cadet blue')
        self.frame=Frame(self.master,bg='cadet blue')
        self.frame.pack()

        self.Username=StringVar()
        self.Password=StringVar()

        Manage_Frame1=Frame(self.master,bd=4,relief=RIDGE,bg="cornsilk")
        Manage_Frame1.place(x=250,y=100,width=850,height=550)

        title=Label(Manage_Frame1,text="Welcome teachers:",bg="cornsilk",fg="cadet blue",font=("times new roman",20,"bold"))
        title.place(x=5,y=1,width=220,height=80)

        Manage_Frame2=Frame(self.master,bd=4,relief=RIDGE,bg="cornsilk")
        Manage_Frame2.place(x=350,y=170,width=650,height=350)


       
        u_name=Label(Manage_Frame2,text="Username",bg="cornsilk",fg="grey",font=("times new roman",15,"bold"))
        u_name.place(x=150,y=70)

        self.textUsername=Entry(Manage_Frame2,font=("times new roman",15),bg='lightgrey',textvariable=self.Username)
        self.textUsername.place(x=270,y=70,width=250)

        p_name=Label(Manage_Frame2,text="Password",bg="cornsilk",fg="grey",font=("times new roman",15,"bold"))
        p_name.place(x=150,y=110)

        self.textPassword=Entry(Manage_Frame2,font=("times new roman",15),bg='lightgrey',textvariable=self.Password)
        self.textPassword.place(x=270,y=110,width=250)

       
        self.btnlogin= Button(Manage_Frame2,text="Login",width=5,font=('times new roman',17,'italic'),bg='cadet blue',fg='Cornsilk',command=self.Login_system)
        self.btnlogin.place(x=135,y=225,width=120)

        self.btnreset= Button(Manage_Frame2,text="Reset",width=5,font=('times new roman',17,'italic'),bg='cadet blue',fg='Cornsilk', command=self.iReset)
        self.btnreset.place(x=265,y=225,width=120)

        self.btnexit= Button(Manage_Frame2,text="Exit",width=5,font=('times new roman',17,'italic'),bg='cadet blue',fg='Cornsilk', command=self.iExit)
        self.btnexit.place(x=395,y=225,width=120)

        Manage_Frame3=Frame(self.master,bd=4,relief=RIDGE,bg="cornsilk")
        Manage_Frame3.place(x=350,y=520,width=650,height=60)

        self.btnstudent= Button(Manage_Frame3,text="View profile",width=25,font=('arial',12,'bold'),bg='cadet blue',fg='Cornsilk',state=DISABLED,
                                command=self.reg)
        self.btnstudent.place(x=55,y=10)
         
        self.btnfaculty= Button(Manage_Frame3,text="Provide student details",width=25,font=('arial',12,'bold'),bg='cadet blue',fg='Cornsilk',state=DISABLED,
                                command=self.h)
        self.btnfaculty.place(x=325,y=10)


        



    def Login_system(self):
        user = (self.Username.get())
        pas = (self.Password.get())
        if(user==str(1234) and pas == str(2345)):
            self.btnstudent.config(state=NORMAL)
            self.btnfaculty.config(state=NORMAL)
            
        else :
            self.Username.set("")
            self.Password.set("")
            
            messagebox.showerror("Error","All fields are required",parent=self.master)
            
            
        
            try:
                con=pymysql.connect(host="localhost",user="root",password="",db="management")
                cur=con.cursor()
                if cur.execute("SELECT * FROM user WHERE username=%s AND password=%s AND designation='Student'",(self.Username.get(),self.Password.get())):
                    row=cur.fetchone()
                    if row==None:
                        messagebox.showerror("Error","Invalid USERNAME & PASSWORD",parent=self.master)
                    
                    else:
                        messagebox.showinfo("success","Welcome",parent=self.master)
                        self.btnstudent.config(state =NORMAL)
                        self.btnfaculty.config(state =DISABLED)
                elif cur.execute("SELECT * FROM user WHERE username=%s AND password=%s AND designation='Faculty Member'",(self.Username.get(),self.Password.get())):

                    row=cur.fetchone()
                    if row==None:
                        messagebox.showerror("Error","Invalid USERNAME & PASSWORD",parent=self.master)
                    
                    else:
                        messagebox.showinfo("success","Welcome",parent=self.master)
                        self.btnfaculty.config(state =NORMAL)
                        self.btnstudent.config(state =DISABLED)
                else:
                     messagebox.showerror("error","error handle,(str(es))",parent=self.master)
            except Exception as es:
                messagebox.showerror("error","error handle,(str(es))",parent=self.master)


    def iReset(self):
        self.btnstudent.config(state =DISABLED)
        self.btnfaculty.config(state =DISABLED)
        self.Username.set("")
        self.Password.set("")
        self.textUsername.focus()

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("College Login Sytem","Confirm if you want to exit")
        if self.iExit>0:
            self.master.destroy()
            return
    
    def reg(self):
        self.newWindow=Toplevel(self.master)
        self.app= CollegeRegistration(self.newWindow)

    def manage(self):
        self.newWindow=Toplevel(self.master)
        self.app= CollegeManagement(self.newWindow)

    def h(self):
        self.newWindow=Toplevel(self.master)
        self.app= Window_h(self.newWindow)

class Window_h:
    def __init__(self,master):
        self.master=master
        self.master.title("College Management")
        self.master.geometry("700x300+0+0")
        self.master.maxsize(500, 300)
        self.master.minsize(500, 300)
        self.master.config(bg='cadet blue')
        self.frame=Frame(self.master,bg='cadet blue')
        self.frame.pack()

        self.lblTitle=Label(self.frame,text="College Management System",font=("arial",20,'bold'),bg='cadet blue',fg='Cornsilk')
        self.lblTitle.grid(row=0,column=0,columnspan=2,pady=10,padx=10)


        #=====================================ADMIN , STUDENT AND FACULTY BUTTONS=======================================================================

        self.btnAdmin= Button(self.frame,text="Mark Attendance",width=15,height=3,font=('arial',10,'bold'),bg='Cornsilk',fg='cadet blue')
        self.btnAdmin.grid(row=1,column=0,sticky="e")

        self.btnStd= Button(self.frame,text="Grade Marksheet",width=15,height=3,font=('arial',10,'bold'),bg='Cornsilk',fg='cadet blue')
        self.btnStd.grid(row=2,column=0,sticky="e")





#==========================================================ADMIN SYSTEM======================================================================================   
            
class Window1:
    def __init__(self,master):
        self.master=master
        self.master.title("College Management System")
        self.master.geometry("1350x700+0+0")
        self.master.config(bg='cadet blue')
        self.frame=Frame(self.master,bg='cadet blue')
        self.frame.pack()

        self.Username=StringVar()
        self.Password=StringVar()
    #==============================================admin frame============================================================================
        Manage_Frame1=Frame(self.master,bd=4,relief=RIDGE,bg="cornsilk")
        Manage_Frame1.place(x=250,y=100,width=850,height=550)

        title=Label(Manage_Frame1,text="Welcome Admin:",bg="cornsilk",fg="cadet blue",font=("times new roman",20,"bold"))
        title.place(x=5,y=1,width=200,height=80)

        Manage_Frame2=Frame(self.master,bd=4,relief=RIDGE,bg="cornsilk")
        Manage_Frame2.place(x=350,y=170,width=650,height=350)

     #=====================================admin login=====================================================================================
       
        u_name=Label(Manage_Frame2,text="Username",bg="cornsilk",fg="grey",font=("times new roman",15,"bold"))
        u_name.place(x=150,y=70)

        self.textUsername=Entry(Manage_Frame2,font=("times new roman",15),bg='lightgrey',textvariable=self.Username)
        self.textUsername.place(x=270,y=70,width=250)

        p_name=Label(Manage_Frame2,text="Password",bg="cornsilk",fg="grey",font=("times new roman",15,"bold"))
        p_name.place(x=150,y=110)

        self.textPassword=Entry(Manage_Frame2,font=("times new roman",15),bg='lightgrey',textvariable=self.Password)
        self.textPassword.place(x=270,y=110,width=250)

    #======================================admin login button================================================================================
        self.btnlogin= Button(Manage_Frame2,text="Login",width=5,font=('times new roman',17,'italic'),bg='cadet blue',fg='Cornsilk',command=self.Login_system)
        self.btnlogin.place(x=135,y=225,width=120)

        self.btnreset= Button(Manage_Frame2,text="Reset",width=5,font=('times new roman',17,'italic'),bg='cadet blue',fg='Cornsilk', command=self.iReset)
        self.btnreset.place(x=265,y=225,width=120)

        self.btnexit= Button(Manage_Frame2,text="Exit",width=5,font=('times new roman',17,'italic'),bg='cadet blue',fg='Cornsilk', command=self.iExit)
        self.btnexit.place(x=395,y=225,width=120)

        Manage_Frame3=Frame(self.master,bd=4,relief=RIDGE,bg="cornsilk")
        Manage_Frame3.place(x=350,y=520,width=650,height=60)
    #==============================================student teacher registratiob button======================================================

        self.btnstudent= Button(Manage_Frame3,text="Register new student",width=25,font=('arial',12,'bold'),bg='cadet blue',fg='Cornsilk',state=DISABLED,
                                command=self.reg)
        self.btnstudent.place(x=55,y=10)
         
        self.btnfaculty= Button(Manage_Frame3,text="Register new teacher",width=25,font=('arial',12,'bold'),bg='cadet blue',fg='Cornsilk',state=DISABLED,
                                command=self.manage)
        self.btnfaculty.place(x=325,y=10)


    def Login_system(self):
        user = (self.Username.get())
        pas = (self.Password.get())
        if(user==str(1234) and pas == str(2345)):
            self.btnstudent.config(state=NORMAL)
            self.btnfaculty.config(state=NORMAL)
            
        else :
            self.Username.set("")
            self.Password.set("")
            
            messagebox.showerror("Error","All fields are required",parent=self.master)
            
            
        
            try:
                con=pymysql.connect(host="localhost",user="root",password="",db="management")
                cur=con.cursor()
                if cur.execute("SELECT * FROM user WHERE username=%s AND password=%s AND designation='Student'",(self.Username.get(),self.Password.get())):
                    row=cur.fetchone()
                    if row==None:
                        messagebox.showerror("Error","Invalid USERNAME & PASSWORD",parent=self.master)
                    
                    else:
                        messagebox.showinfo("success","Welcome",parent=self.master)
                        self.btnstudent.config(state =NORMAL)
                        self.btnfaculty.config(state =DISABLED)
                elif cur.execute("SELECT * FROM user WHERE username=%s AND password=%s AND designation='Faculty Member'",(self.Username.get(),self.Password.get())):

                    row=cur.fetchone()
                    if row==None:
                        messagebox.showerror("Error","Invalid USERNAME & PASSWORD",parent=self.master)
                    
                    else:
                        messagebox.showinfo("success","Welcome",parent=self.master)
                        self.btnfaculty.config(state =NORMAL)
                        self.btnstudent.config(state =DISABLED)
                else:
                     messagebox.showerror("error","error handle,(str(es))",parent=self.master)
            except Exception as es:
                messagebox.showerror("error","error handle,(str(es))",parent=self.master)


    def iReset(self):
        self.btnstudent.config(state =DISABLED)
        self.btnfaculty.config(state =DISABLED)
        self.Username.set("")
        self.Password.set("")
        self.textUsername.focus()

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("College Login Sytem","Confirm if you want to exit")
        if self.iExit>0:
            self.master.destroy()
            return
    
    def reg(self):
        self.newWindow=Toplevel(self.master)
        self.app= StudentRegistration(self.newWindow)

    def manage(self):
        self.newWindow=Toplevel(self.master)
        self.app= TeacherRegistration(self.newWindow)
         

class TeacherRegistration():
    def __init__(self,master):
        self.master=master
        self.master.title("College Management System")
        self.master.geometry("1350x700+0+0")
        self.master.config(bg='cadet blue')
 

        Manage_Frame=Frame(self.master,bd=4,relief=RIDGE,bg="cornsilk")
        Manage_Frame.place(x=150,y=50,width=1050,height=600)

        title=Label(Manage_Frame,text="REGISTER NEW FACULTY HERE:",bg="cornsilk",fg="cadet blue",font=("times new roman",20,"bold"))
        title.place(x=10,y=1,width=500,height=80)

        f_name=Label(Manage_Frame,text="First Name",bg="cornsilk",fg="grey",font=("times new roman",15,"bold"))
        f_name.place(x=100,y=90)
        self.txt_fname=Entry(Manage_Frame,font=("times new roman",15),bg='lightgrey')
        self.txt_fname.place(x=100,y=120)

        l_name=Label(Manage_Frame,text="Last Name",bg="cornsilk",fg="grey",font=("times new roman",15,"bold"))
        l_name.place(x=400,y=90)
        self.txt_lname=Entry(Manage_Frame,font=("times new roman",15),bg='lightgrey')
        self.txt_lname.place(x=400,y=120)

        contact_no=Label(Manage_Frame,text="Contact No.",bg="cornsilk",fg="grey",font=("times new roman",15,"bold"))
        contact_no.place(x=700,y=90)
        self.txt_contact=Entry(Manage_Frame,font=("times new roman",15),bg='lightgrey')
        self.txt_contact.place(x=700,y=120)

        
        mstatus=Label(Manage_Frame,text="Marital Status",bg="cornsilk",fg="grey",font=("times new roman",15,"bold"))
        mstatus.place(x=100,y=170)
        self.txt_mstatus=ttk.Combobox(Manage_Frame,font=("times new roman",15),state='readonly')
        
        self.txt_mstatus['values']=("Married","Unmarried","Divorced")
        self.txt_mstatus.place(x=100,y=200)

        email=Label(Manage_Frame,text="Email",bg="cornsilk",fg="grey",font=("times new roman",15,"bold"))
        email.place(x=400,y=170)
        self.txt_email=Entry(Manage_Frame,font=("times new roman",15),bg='lightgrey')
        self.txt_email.place(x=400,y=200)

        dob=Label(Manage_Frame,text="Date of Birth",bg="cornsilk",fg="grey",font=("times new roman",15,"bold"))
        dob.place(x=700,y=170)
        self.txt_dob=Entry(Manage_Frame,font=("times new roman",15),bg='lightgrey')
        self.txt_dob.place(x=700,y=200)

        gender=Label(Manage_Frame,text="Gender",bg="cornsilk",fg="grey",font=("times new roman",15,"bold"))
        gender.place(x=100,y=250)

        self.txt_gender=ttk.Combobox(Manage_Frame,font=("times new roman",15),state='readonly')
        
        self.txt_gender['values']=("Male","Female","Other")
        self.txt_gender.place(x=100,y=280)


       

        qual=Label(Manage_Frame,text="Education Qualification",bg="cornsilk",fg="grey",font=("times new roman",15,"bold"))
        qual.place(x=400,y=250)
        self.txt_qual=Text(Manage_Frame,font=("times new roman",15),bg='lightgrey')
        self.txt_qual.place(x=400,y=280,width=250,height=80)
        

        address=Label(Manage_Frame,text="Permament Address",bg="cornsilk",fg="grey",font=("times new roman",15,"bold"))
        address.place(x=700,y=250)
        self.txt_address=Text(Manage_Frame,font=("times new roman",15),bg='lightgrey')
        self.txt_address.place(x=700,y=280,width=250,height=80)

        uname=Label(Manage_Frame,text="Username",bg="cornsilk",fg="grey",font=("times new roman",15,"bold"))
        uname.place(x=100,y=380)
        self.txt_uname=Entry(Manage_Frame,font=("times new roman",15),bg='lightgrey')
        self.txt_uname.place(x=100,y=410)

        passw=Label(Manage_Frame,text="Password",bg="cornsilk",fg="grey",font=("times new roman",15,"bold"))
        passw.place(x=400,y=380)
        self.txt_passw=Entry(Manage_Frame,font=("times new roman",15),bg='lightgrey')
        self.txt_passw.place(x=400,y=410)

        cpass=Label(Manage_Frame,text="Confirm Password",bg="cornsilk",fg="grey",font=("times new roman",15,"bold"))
        cpass.place(x=700,y=380)
        self.txt_cpass=Entry(Manage_Frame,font=("times new roman",15),bg='lightgrey')
        self.txt_cpass.place(x=700,y=410)

        chk=Checkbutton(Manage_Frame,text="I Agree the Terms & Conditions",bg="cornsilk").place(x=280,y=480)

        self.btnReg= Button(Manage_Frame,text="Register Account",width=15,font=('times new roman',17,'italic'),bg='cadet blue',fg='Cornsilk',command=self.register)
        self.btnReg.place(x=280,y=500)

        self.btnupdate= Button(Manage_Frame,text="Update Account",width=15,font=('times new roman',17,'italic'),bg='cadet blue',fg='Cornsilk',command=self.register)
        self.btnupdate.place(x=530,y=500)
        self.btnupdate= Button(Manage_Frame,text="Exit",width=15,font=('times new roman',17,'italic'),bg='cadet blue',fg='Cornsilk',command=self.Exit)
        self.btnupdate.place(x=730,y=500)

    def register(self):
        if self.txt_fname.get()=="" or self.txt_lname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.txt_designation.get()=="" or self.txt_ids.get()=="" or self.txt_passw.get()=="" :
            messagebox.showerror("Warning","All fields are reguired to fill",parent=self.master)
        elif self.txt_passw.get() != self.txt_cpass.get():
            messagebox.showerror("Warnng","Password and Confirm password must be same",parent=self.master)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",db="management")
                cur=con.cursor()
                cur.execute("insert into user(f_name,l_name,contact,email,designation,username,password)values(%s,%s,%s,%s,%s,%s,%s)",
                            (
                                self.txt_fname.get(),
                                self.txt_lname.get(),
                                self.txt_contact.get(),
                                self.txt_email.get(),
                                self.txt_designation.get(),
                                self.txt_ids.get(),
                                self.txt_passw.get()
                            ))
                con.commit()
                con.close()
                messagebox.showinfo("success","Registered successfully",parent=self.master)
            except Exception as es:
                messagebox.showerror("error","error handle,(str(es))",parent=self.master)
    def Exit(self):
        self.Exit=tkinter.messagebox.askyesno("College Login Sytem","Confirm if you want to exit")
        if self.Exit>0:
            self.master.destroy()
            return   
 
            
    def z(self):
        self.newWindow=Toplevel(self.master)
        self.app= Window1(self.newWindow)



class StudentRegistration():
    def __init__(self,master):
        self.master=master
        self.master.title("College Management System")
        self.master.geometry("1350x700+0+0")
        self.master.config(bg='cadet blue')
        Manage_Frame=Frame(self.master,bd=4,relief=RIDGE,bg="cornsilk")
        Manage_Frame.place(x=50,y=100,width=1250,height=550)

        title=Label(Manage_Frame,text="REGISTER NEW STUDENT HERE:",bg="cornsilk",fg="cadet blue",font=("times new roman",20,"bold"))
        title.place(x=10,y=1,width=500,height=80)

        f_name=Label(Manage_Frame,text="First Name",bg="cornsilk",fg="grey",font=("times new roman",15,"bold"))
        f_name.place(x=100,y=90)
        self.txt_fname=Entry(Manage_Frame,font=("times new roman",15),bg='lightgrey')
        self.txt_fname.place(x=100,y=120)

        l_name=Label(Manage_Frame,text="Last Name",bg="cornsilk",fg="grey",font=("times new roman",15,"bold"))
        l_name.place(x=400,y=90)
        self.txt_lname=Entry(Manage_Frame,font=("times new roman",15),bg='lightgrey')
        self.txt_lname.place(x=400,y=120)

        contact_no=Label(Manage_Frame,text="Contact No.",bg="cornsilk",fg="grey",font=("times new roman",15,"bold"))
        contact_no.place(x=700,y=90)
        self.txt_contact=Entry(Manage_Frame,font=("times new roman",15),bg='lightgrey')
        self.txt_contact.place(x=700,y=120)

        email=Label(Manage_Frame,text="Email",bg="cornsilk",fg="grey",font=("times new roman",15,"bold"))
        email.place(x=1000,y=90)
        self.txt_email=Entry(Manage_Frame,font=("times new roman",15),bg='lightgrey')
        self.txt_email.place(x=1000,y=120)

        father=Label(Manage_Frame,text="Father's Name",bg="cornsilk",fg="grey",font=("times new roman",15,"bold"))
        father.place(x=100,y=170)
        self.txt_father=Entry(Manage_Frame,font=("times new roman",15),bg='lightgrey')
        self.txt_father.place(x=100,y=200)

        mother=Label(Manage_Frame,text="Mother's Name",bg="cornsilk",fg="grey",font=("times new roman",15,"bold"))
        mother.place(x=400,y=170)
        self.txt_mother=Entry(Manage_Frame,font=("times new roman",15),bg='lightgrey')
        self.txt_mother.place(x=400,y=200)

        dob=Label(Manage_Frame,text="Date of Birth",bg="cornsilk",fg="grey",font=("times new roman",15,"bold"))
        dob.place(x=700,y=170)
        self.txt_dob=Entry(Manage_Frame,font=("times new roman",15),bg='lightgrey')
        self.txt_dob.place(x=700,y=200)

        gender=Label(Manage_Frame,text="Gender",bg="cornsilk",fg="grey",font=("times new roman",15,"bold"))
        gender.place(x=1000,y=170)

        self.txt_gender=ttk.Combobox(Manage_Frame,font=("times new roman",15),state='readonly')
        
        self.txt_gender['values']=("Male","Female","Other")
        self.txt_gender.place(x=1000,y=200)

       
        tmark=Label(Manage_Frame,text="10th Marks",bg="cornsilk",fg="grey",font=("times new roman",15,"bold"))
        tmark.place(x=100,y=250)
        self.txt_tmark=Entry(Manage_Frame,font=("times new roman",15),bg='lightgrey')
        self.txt_tmark.place(x=100,y=280)

        twmark=Label(Manage_Frame,text="12th Marks",bg="cornsilk",fg="grey",font=("times new roman",15,"bold"))
        twmark.place(x=400,y=250)
        self.txt_twmark=Entry(Manage_Frame,font=("times new roman",15),bg='lightgrey')
        self.txt_twmark.place(x=400,y=280)

        address=Label(Manage_Frame,text="Permament Address",bg="cornsilk",fg="grey",font=("times new roman",15,"bold"))
        address.place(x=700,y=250)
        self.txt_address=Text(Manage_Frame,font=("times new roman",15),bg='lightgrey')
        self.txt_address.place(x=700,y=280,width=400,height=50)

        uname=Label(Manage_Frame,text="Username",bg="cornsilk",fg="grey",font=("times new roman",15,"bold"))
        uname.place(x=100,y=330)
        self.txt_uname=Entry(Manage_Frame,font=("times new roman",15),bg='lightgrey')
        self.txt_uname.place(x=100,y=360)

        passw=Label(Manage_Frame,text="Password",bg="cornsilk",fg="grey",font=("times new roman",15,"bold"))
        passw.place(x=400,y=330)
        self.txt_passw=Entry(Manage_Frame,font=("times new roman",15),bg='lightgrey')
        self.txt_passw.place(x=400,y=360)

        cpass=Label(Manage_Frame,text="Confirm Password",bg="cornsilk",fg="grey",font=("times new roman",15,"bold"))
        cpass.place(x=700,y=330)
        self.txt_cpass=Entry(Manage_Frame,font=("times new roman",15),bg='lightgrey')
        self.txt_cpass.place(x=700,y=360)

        chk=Checkbutton(Manage_Frame,text="I Agree the Terms & Conditions",bg="cornsilk").place(x=400,y=415)

        self.btnReg= Button(Manage_Frame,text="Register Account",width=15,font=('times new roman',17,'italic'),bg='cadet blue',fg='Cornsilk',command=self.register)
        self.btnReg.place(x=400,y=440)

        self.btnupdate= Button(Manage_Frame,text="Update Account",width=15,font=('times new roman',17,'italic'),bg='cadet blue',fg='Cornsilk',command=self.register)
        self.btnupdate.place(x=650,y=440)

        self.btnupdate= Button(Manage_Frame,text="Exit",width=15,font=('times new roman',17,'italic'),bg='cadet blue',fg='Cornsilk',command=self.Exit)
        self.btnupdate.place(x=900,y=440)



    def register(self):
        if self.txt_fname.get()=="" or self.txt_lname.get()=="" or self.txt_contact.get()=="" or self.txt_father.get()=="" or self.txt_mother.get()=="" or self.txt_dob.get()=="" or self.txt_gender.get()=="" or self.txt_tmark.get()=="" or self.txt_twmark.get()=="" or self.txt_address.get()=="" or self.txt_uname.get()=="" or self.txt_passw.get()=="" or self.txt_cpass.get()=="" or self.txt_email.get()=="" :
            messagebox.showerror("Warning","All fields are reguired to fill",parent=self.master)
        elif self.txt_passw.get() != self.txt_cpass.get():
            messagebox.showerror("Warnng","Password and Confirm password must be same",parent=self.master)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",db="database system")
                cur=con.cursor()
                cur.execute("insert into student(first name,last name,contact,father's name, mother's name,Dob, gender, 10th marks, 12th marks, permannent address,username,password,confirm password, email)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                            (
                                self.txt_fname.get(),
                                self.txt_lname.get(),
                                self.txt_contact.get(),
                                self.txt_father.get(),
                                self.txt_mother.get(),
                                
                                self.txt_dob.get(),
                                self.txt_gender.get(),
                                self.txt_tmark.get(),
                                self.txt_twmark.get(),
                                self.txt_address.get(),
                                self.txt_uname.get(),
                                self.txt_passw.get(),
                                self.txt_cpass.get(),
                                self.txt_email.get(),
                             
                            ))
                con.commit()
                con.close()
                messagebox.showinfo("success","Registered successfully",parent=self.master)
            except Exception as es:
                messagebox.showerror("error","error handle,(str(es))",parent=self.master)
 
    def Exit(self):
        self.Exit=tkinter.messagebox.askyesno("College Login Sytem","Confirm if you want to exit")
        if self.Exit>0:
            self.master.destroy()
            return    



        


                
       
        
        
    
 
        
        


        

        
 
        
       

if __name__=='__main__':
    main()

