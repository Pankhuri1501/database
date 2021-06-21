from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import os
import random
import time
import datetime
import sqlite3

conn=sqlite3.connect("login.db")
c= conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS student ( fname text, mname text, mobno integer,email text, pas text, cpas text)")
conn.commit()
conn.close()




def main():
    root=Tk()
    app=FirstPage(root)

class FirstPage:
    def __init__(self,master):
        self.master=master
        self.master.title("College Management System")
        self.master.geometry("700x300+0+0")
        self.master.maxsize(500, 300)
        self.master.minsize(500, 300)
        
        self.master.config(bg='grey')
        self.frame=Frame(self.master,bg='grey')
        self.frame.pack()

        self.Username=StringVar()
        self.Password=StringVar()
        
        self.fname = StringVar()
        self.mname = StringVar()
        self.mobno = StringVar()
        self.email = StringVar()
        self.dob = StringVar()
        self.id=StringVar()
        self.pas=StringVar()
        self.cpas=StringVar()
        self.chk=StringVar()


        def action():
                
            return

        
        self.lblTitle=Label(self.frame,text="College Management System",font=("arial",20,'bold'),bg='pink',fg='white')
        self.lblTitle.grid(row=0,column=0,columnspan=2,pady=10,padx=10)



        #=====================================LOGIN AND SIGN UP BUTTONS=======================================================================

        self.btnLogin= Button(self.frame,text="LOGIN",width=15,height=3,font=('arial',10,'bold'),bg='grey',fg='pink', command=self.x)
        self.btnLogin.grid(row=1,column=0,sticky="e")

        self.btnSign= Button(self.frame,text="SIGN UP",width=15,height=3,font=('arial',10,'bold'),bg='grey',fg='pink', command=self.y)
        self.btnSign.grid(row=2,column=0,sticky="e")

       #=====================================LOGIN AND SIGN UP BUTTONS=======================================================================
               
    def y(self):
        self.newWindow=Toplevel(self.master)
        self.app= CollegeSignUpPage(self.newWindow)

    def x(self):
        self.newWindow=Toplevel(self.master)
        self.app= Window1(self.newWindow)

class CollegeSignUpPage:
    def __init__(self,master):
        self.master=master
        self.master.title("College Management System")
        self.master.geometry("1350x700+0+0")
        self.master.config(bg='grey')
    
        Manage_Frame=Frame(self.master,bd=4,relief=RIDGE,bg="cornsilk")
        Manage_Frame.place(x=250,y=100,width=850,height=550)

        title=Label(Manage_Frame,text="REGISTER HERE",bg="cornsilk",fg="grey",font=("times new roman",20,"bold"))
        title.place(x=10,y=1,width=300,height=80)

        f_name=Label(Manage_Frame,text="First Name",bg="cornsilk",fg="grey",font=("times new roman",15,"bold"))
        f_name.place(x=100,y=90)

        txt_fname=Entry(Manage_Frame,font=("times new roman",15),bg='lightgrey', textvariable = self.fname)
        txt_fname.place(x=100,y=120,width=250)

        l_name=Label(Manage_Frame,text="Last Name",bg="cornsilk",fg="grey",font=("times new roman",15,"bold"))
        l_name.place(x=500,y=90)

        txt_lname=Entry(Manage_Frame,font=("times new roman",15),bg='lightgrey',textvariable = self.mname)
        txt_lname.place(x=500,y=120,width=250)

        contact_no=Label(Manage_Frame,text="Contact No.",bg="cornsilk",fg="grey",font=("times new roman",15,"bold"))
        contact_no.place(x=100,y=170)

        txt_contact=Entry(Manage_Frame,font=("times new roman",15),bg='lightgrey', textvariable = self.mobno)
        txt_contact.place(x=100,y=200,width=250)

        email=Label(Manage_Frame,text="Email",bg="cornsilk",fg="grey",font=("times new roman",15,"bold"))
        email.place(x=500,y=170)

        txt_email=Entry(Manage_Frame,font=("times new roman",15),bg='lightgrey', textvariable = self.email)
        txt_email.place(x=500,y=200,width=250)

        designation=Label(Manage_Frame,text="Designation",bg="cornsilk",fg="grey",font=("times new roman",15,"bold"))
        designation.place(x=100,y=250)

        txt_designation=ttk.Combobox(Manage_Frame,state='readonly',font=("times new roman",15),textvariable = self.dob)
        
        txt_designation['values']=("","Student","Faculty Member")
        txt_designation.current(0)
        txt_designation.place(x=100,y=280,width=250)

        ids=Label(Manage_Frame,text="Roll No./Faculty Id.",bg="cornsilk",fg="grey",font=("times new roman",15,"bold"))
        ids.place(x=500,y=250)

        txt_ids=Entry(Manage_Frame,font=("times new roman",15),bg='lightgrey', textvariable=self.id)
        txt_ids.place(x=500,y=280,width=250)

        passw=Label(Manage_Frame,text="Password",bg="cornsilk",fg="grey",font=("times new roman",15,"bold"))
        passw.place(x=100,y=330)

        txt_passw=Entry(Manage_Frame,font=("times new roman",15),bg='lightgrey',textvariable=self.pas)
        txt_passw.place(x=100,y=360,width=250)

        cpass=Label(Manage_Frame,text="Confirm Password",bg="cornsilk",fg="grey",font=("times new roman",15,"bold"))
        cpass.place(x=500,y=330)

        txt_cpass=Entry(Manage_Frame,font=("times new roman",15),bg='lightgrey',textvariable=self.cpas)
        txt_cpass.place(x=500,y=360,width=250)

        chk=Checkbutton(Manage_Frame,textvariable=self.chk,text="I Agree the Terms & Conditions",bg="cornsilk").place(x=100,y=410)
        self.btnLogin= Button(Manage_Frame,text="Register Now",width=15,font=('times new roman',17,'italic'),bg='grey',fg='Cornsilk',command=self.z)
        self.btnLogin.place(x=100,y=450)

    def z(self):
        self.newWindow=Toplevel(self.master)
        self.app= Window1(self.newWindow)



if __name__=='__main__':
    main()
