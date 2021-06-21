from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random
import time;
import datetime

def main():
    root=Tk()
    app= Window1(root)

class Window1:
    def __init__(self,master):
        self.master=master
        self.master.title("College management system")
        self.master.geometry('1350x750+0+0')
        self.frame =Frame(self.master)
        self.frame.pack()

        self.Username= StringVar()
        self.Password= StringVar()
        


        self.LabelTitle=Label(self.frame, text='College mangement system',font=('arial',50,'bold'),bd=20)
        self.LabelTitle.grid(row=0,column=0,columnspan=2,pady=20)

        self.Loginframe1=Frame(self.frame,width=1010,height=300,bd=20,relief='ridge')
        self.Loginframe1.grid(row=1,column=0)
        
        self.Loginframe2=Frame(self.frame,width=1000,height=100,bd=20,relief='ridge')
        self.Loginframe2.grid(row=2,column=0)

        self.Loginframe3=Frame(self.frame,width=1000,height=200,bd=20,relief='ridge')
        self.Loginframe3.grid(row=3,column=0,pady=2)

        #=================================================================================================================

        self.lblUsername=Label(self.Loginframe1, text='Username',font=('arial',30,'bold'),bd=22)
        self.lblUsername.grid(row=0,column=0)
        self.txtUsername=Entry(self.Loginframe1, text='Username',font=('arial',30,'bold'),bd=22,textvariable=self.Username)
        self.txtUsername.grid(row=0,column=1)

        self.lblPassword=Label(self.Loginframe1, text='Password',font=('arial',30,'bold'),bd=22)
        self.lblPassword.grid(row=1,column=0)
        self.txtPassword=Entry(self.Loginframe1, text='Password',font=('arial',30,'bold'),bd=22,show="*",textvariable=self.Password)
        self.txtPassword.grid(row=1,column=1,padx=85)
        #=================================================================================================================


        self.btnLogin= Button(self.Loginframe2,text="Login",width=20,font=('arial',17,'bold'), command=self.Login_system)
        self.btnLogin.grid(row=0,column=0)

        self.btnReset= Button(self.Loginframe2,text="Reset",width=20,font=('arial',17,'bold'), command=self.Reset)
        self.btnReset.grid(row=0,column=1)

        self.btnExit= Button(self.Loginframe2,text="Exit",width=20,font=('arial',17,'bold'), command=self.Exit)
        self.btnExit.grid(row=0,column=2)

        #===================================================================================================================

        self.btnRegistration= Button(self.Loginframe3,text="Student Registration system",font=('arial',20,'bold'),state=DISABLED, command=self.Registration_window)
        self.btnRegistration.grid(row=0,column=0)

        self.btnHospital= Button(self.Loginframe3,text="Student management system",font=('arial',20,'bold'),state=DISABLED, command=self.Management_window)
        self.btnHospital.grid(row=0,column=1,pady=8,padx=20)
        
        #===================================================================================================================
    def Login_system(self):
        user=(self.Username.get())
        pas=(self.Password.get())


        if (user== str(1234)) and (pas== str(2345)):
            self.btnRegistration.config(state =NORMAL)
            self.btnHospital.config(state =NORMAL)

        else:
            messagebox.askyesno("Student Management syste","you have entered an invalid login detail")
            self.btnRegistration.config(state =DISABLED)
            self.btnHospital.config(state =DISABLED)
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()

    def Reset(self):
        
      self.btnRegistration.config(state =DISABLED)
      self.btnHospital.config(state =DISABLED)
      self.Username.set("")
      self.Password.set("")
      self.txtUsername.focus()

    def Exit(self):
        self.Exit= messagebox.askyesno("Student Management syste","Confirm if you want to exit")
        if self.Exit >0:
            self.master.destroy()
            return        
            
        #===================================================================================================================

    def Registration_window(self):
        self.newWindow=Toplevel(self.master)
        self.app= Window2(self.newWindow)

    def Management_window(self):
        self.newWindow=Toplevel(self.master)
        self.app= Window3(self.newWindow)


class Window2:
    def __init__(self,master):
        self.master=master
        self.master.title("Student Registration system")
        self.master.geometry('1350x750+0+0')
        self.frame =Frame(self.master)
        self.frame.pack()
      #===================================================================================================================
        DateofOrder=StringVar()
        DateofOrder.set(time.strftime("%d/%m/%Y"))

        var1=StringVar()
        var2=StringVar()
        var3=StringVar()
        var4=IntVar()

        Firstname=StringVar()
        Secondname=StringVar()
        Address=StringVar()
        Postcode=StringVar()
        Contact=StringVar()
        Ref=StringVar()
    

        Membership=StringVar()
        Membership.set("0")
        
    #===============================================Functions======================================================
        def Exit():
            Exit=messagebox.askyesno("club member registration system","confirm if you want to exit")
            if Exit>0:
                self.master.destroy()
                return

        def Reset():
            Firstname.set("")
            Secondname.set("")
            Address.set("")
            Postcode.set("")
            Contact.set("")
            Ref.set("")
            Membership.set("0")
        

            var1.set("")
            var2.set("")
            var3.set("")
            var4.set(0)
            self.cboProve_of_ID.current(0)
            self.cboType_of_Member.current(0)
            self.cboMethod_of_payment.current(0)
            self.txtMembership.config(state=DISABLED)
        def iResetRecord():
            iResetRecord=messagebox.askokcancel("club member registration system","confirm if you want to add new record")
            if  iResetRecord>0:
                Reset()
            elif iResetRecord<=0:
                Reset()
                self.txtReceipt.delete("1.0",END)
                return
        def Ref_No():
    
            x=random.randint(10903,600873)
            randomRef=str(x)
            Ref.set(randomRef)

        def Receipt():
            Ref_No()
            self.txtReceipt.insert(END,"\t"+ Ref.get()+ "\t\t" + Firstname.get()+ "\t\t" + Secondname.get() + "\t\t" + Address.get() + "\t\t" + DateofOrder.get() + "\t\t" +
                                   Contact.get() + "\t\t" + Membership.get() +"\n")

        def Membership_Fees():
        

           if(var4.get()==1):
              self.txtMembership.configure(state=NORMAL)
              Item1=float(50)
              Membership.set("$" + str(Item1))
              
           elif(var4.get()==0):
              self.txtMembership.configure(state=DISABLED)
              Membership.set("0")
            
            
    #===============================================Frame======================================================
        Mainframe=Frame(self.frame)
        Mainframe.grid()

        Titleframe=Frame(Mainframe, bd=20, width=1350, padx=26, relief=RIDGE)
        Titleframe.pack(side=TOP)

        self.lblTitle=Label(Titleframe, font=('arial',59,'bold'),text="Member Registration system",padx=2)
        self.lblTitle.grid()

    #============================================LowerFrame======================================================
        MemberDetailsFrame = LabelFrame(Mainframe, width=1350, height=500, bd=20, pady=5, relief=RIDGE)
        MemberDetailsFrame.pack(side=BOTTOM)

        FrameDetails= LabelFrame(MemberDetailsFrame, bd=10, width=880, height=400, relief=RIDGE)
        FrameDetails.pack(side=LEFT)

        MembersName_F=LabelFrame(FrameDetails, bd=10,width=350,height=400,font=('arial',12,'bold'),text='Customer Name', relief=RIDGE)
        MembersName_F.grid(row=0,column=0)

        Receipt_ButtonFrame=LabelFrame(MemberDetailsFrame, bd=10, width=1000, height=400, relief=RIDGE)
        Receipt_ButtonFrame.pack(side=RIGHT)
     #============================================================================================================
        self.lblRefere=Label(MembersName_F, font=('arial',14,'bold'),text="Reference NO", bd=7)
        self.lblRefere.grid(row=0,column=0,sticky=W)
        self.txtRefere=Entry(MembersName_F, font=('arial',14,'bold'),bd=7,textvariable=Ref, state=DISABLED, insertwidth=2)
        self.txtRefere.grid(row=0,column=1)

        self.lblFirstName=Label(MembersName_F, font=('arial',14,'bold'),text="First name", bd=7)
        self.lblFirstName.grid(row=1,column=0,sticky=W)
        self.txtFirstName=Entry(MembersName_F, font=('arial',14,'bold'),textvariable=Firstname,bd=7,insertwidth=2)
        self.txtFirstName.grid(row=1,column=1)

        self.lblSecondName=Label(MembersName_F, font=('arial',14,'bold'),text="Second name", bd=7)
        self.lblSecondName.grid(row=2,column=0,sticky=W)
        self.txtSecondName=Entry(MembersName_F, font=('arial',14,'bold'),textvariable=Secondname,bd=7,insertwidth=2)
        self.txtSecondName.grid(row=2,column=1)

        self.lblAddress=Label(MembersName_F, font=('arial',14,'bold'),text="Address", bd=7)
        self.lblAddress.grid(row=3,column=0,sticky=W)
        self.txtAddress=Entry(MembersName_F, font=('arial',14,'bold'),bd=7,textvariable=Address,insertwidth=2)
        self.txtAddress.grid(row=3,column=1)

        self.lblPostCode=Label(MembersName_F, font=('arial',14,'bold'),text="PostCode", bd=7)
        self.lblPostCode.grid(row=4,column=0,sticky=W)
        self.txtPostCode=Entry(MembersName_F, font=('arial',14,'bold'),textvariable=Postcode,bd=7,insertwidth=2)
        self.txtPostCode.grid(row=4,column=1)

        self.lblContact=Label(MembersName_F, font=('arial',14,'bold'),text="Contact", bd=7)
        self.lblContact.grid(row=5,column=0,sticky=W)
        self.txtContact=Entry(MembersName_F, font=('arial',14,'bold'),textvariable=Contact,bd=7,insertwidth=2)
        self.txtContact.grid(row=5,column=1)

        self.lblDate=Label(MembersName_F, font=('arial',14,'bold'),text="Date", bd=7)
        self.lblDate.grid(row=6,column=0,sticky=W)
        self.txtDate=Entry(MembersName_F, font=('arial',14,'bold'),textvariable=DateofOrder,bd=7,insertwidth=2)
        self.txtDate.grid(row=6,column=1)
        

     #============================================================================================================
        self.lblProve_of_ID=Label(MembersName_F,font=('arial',14,'bold'),text="Prove of ID",bd=7)
        self.lblProve_of_ID.grid(row=7,column=0,sticky=W)
        
        self.cboProve_of_ID=ttk.Combobox(MembersName_F,textvariable=var1, state='readonly',font=('arial',14,'bold'),width=19)
        self.cboProve_of_ID['value']=('','Adhaar card','Driving Licence','Student ID','Passport')
        self.cboProve_of_ID.current(0)
        self.cboProve_of_ID.grid(row=7,column=1)

        self.lblType_of_Member=Label(MembersName_F,font=('arial',14,'bold'),text="Type of member",bd=7)
        self.lblType_of_Member.grid(row=8,column=0,sticky=W)
        
        self.cboType_of_Member=ttk.Combobox(MembersName_F,textvariable=var2, state='readonly',font=('arial',14,'bold'),width=19)
        self.cboType_of_Member['value']=('','Full member','Annual Member','Honorary member','Pay as you go')
        self.cboType_of_Member.current(0)
        self.cboType_of_Member.grid(row=8,column=1)

        self.lblMethod_of_payment=Label(MembersName_F,font=('arial',14,'bold'),text="Method of payment",bd=7)
        self.lblMethod_of_payment.grid(row=9,column=0,sticky=W)
        
        self.cboMethod_of_payment=ttk.Combobox(MembersName_F,textvariable=var3, state='readonly',font=('arial',14,'bold'),width=19)
        self.cboMethod_of_payment['value']=('','Visa card','Master Card','Debit card','Cash')
        self.cboMethod_of_payment.current(0)
        self.cboMethod_of_payment.grid(row=9,column=1)
        
     #================================================Checkbutton=======================================================
        self.chkMembership= Checkbutton(MembersName_F, text="membership fees", variable=var4, onvalue=1, offvalue=0,font=('arial',16,'bold'),command=Membership_Fees).grid(row=10,column=0,sticky=W)
        self.txtMembership=Entry(MembersName_F, font=('arial',16,'bold'),textvariable=Membership,bd=7,insertwidth=2,state=DISABLED, justify=RIGHT)
        self.txtMembership.grid(row=10,column=1)

     #===================================================receipt========================================================
        self.lblLabel=Label(Receipt_ButtonFrame,font=('arial',10,'bold'),pady=10,text="Member Ref\t Firstname\t Secondname\t Address\t\t Date Reg.\t Contact\t Member Paid",bd=7)
        self.lblLabel.grid(row=0,column=0,columnspan=4)
        self.txtReceipt=t=Text(Receipt_ButtonFrame,width=112,height=22,font=('arial',10,'bold'))
        self.txtReceipt.grid(row=1,column=0,columnspan=4)
    #================================================buttons============================================================
        self.btnReceipt=Button(Receipt_ButtonFrame,padx=18,bd=7,font=('arial',16,'bold'),width=13,text="Receipt",command=Receipt).grid(row=2,column=0)
        self.btnReset=Button(Receipt_ButtonFrame,padx=18,bd=7,font=('arial',16,'bold'),width=13,text="Reset",command=iResetRecord).grid(row=2,column=1)
        self.btnExit=Button(Receipt_ButtonFrame,padx=18,bd=7,font=('arial',16,'bold'),width=13,text="Exit",command=Exit).grid(row=2,column=2)
        

    #===================================================================================================================
        
        
    #===================================================================================================================
        self.quitButton= Button(self.frame, text="Quit",width=25,command=self.Exit)
        self.quitButton.grid(row=3,column=0)

    def close_windows(self):
        self.master.destroy()

    def Exit(self):
        def Exit(self):
            
            self.Exit= messagebox.askyesno("Student Management system","Confirm if you want to exit")
            if self.Exit >0:
                self.master.destroy()
                return        
            else:
                self.newWindow=Toplevel(self.master)
                self.app=Window2(self.newWindow)
                return
     
        
    


class Window3:
    def __init__(self,master):
        self.master=master
        self.master.title("Student management system")
        self.master.geometry('1350x750+0+0')
        self.frame =Frame(self.master)
        self.frame.pack()

      #===================================================================================================================

        cmbNameTablets=StringVar()
        Ref=StringVar()
        Dose=StringVar()
        NumberTablets=StringVar()
        Lot=StringVar()
        IssuedDate=StringVar()
        ExpDate=StringVar()
        DailyDose=StringVar()
        PossibleSideEffects=StringVar()
        FurtherInformation=StringVar()
        StorageAdvice=StringVar()
        DrivingUsingMachines=StringVar()
        HowtoUseMedication=StringVar()
        PatientID=StringVar()
        PatientNHSNo=StringVar()
        PatientName=StringVar()
        DateofBirth=StringVar()
        PatientAddress=StringVar()
        Prescription=StringVar()
    #=========================================function declaration======================================================================
        def Exit():
            Exit=messagebox.askyesno("management system","Confirm if you want to exit")
            if Exit>0:
                self.master.destroy()
                return

        def Prescription():
            self.txtPrescription.insert(END,'Name of Tablets: \t\t\t\t' + cmbNameTablets.get()+ "\n")
            self.txtPrescription.insert(END,'Reference No: \t\t\t\t' + Ref.get()+ "\n")
            self.txtPrescription.insert(END,'Dose: \t\t\t\t' + Dose.get()+ "\n")
            self.txtPrescription.insert(END,'Number of tablets: \t\t\t\t' + NumberTablets.get()+ "\n")
            self.txtPrescription.insert(END,'Lot: \t\t\t\t' + Lot.get()+ "\n")
            self.txtPrescription.insert(END,'Issued Date: \t\t\t\t' + IssuedDate.get()+ "\n")
            self.txtPrescription.insert(END,'Exp DAte: \t\t\t\t' + ExpDate.get()+ "\n")
            self.txtPrescription.insert(END,'Daily dose: \t\t\t\t' + DailyDose.get()+ "\n")
            self.txtPrescription.insert(END,'Side effects: \t\t\t\t' + PossibleSideEffects.get()+ "\n")
            self.txtPrescription.insert(END,'Further info: \t\t\t\t' + FurtherInformation.get()+ "\n")
            self.txtPrescription.insert(END,'Storage advice: \t\t\t\t' + StorageAdvice.get()+ "\n")
            self.txtPrescription.insert(END,'Driving or using machines: \t\t\t\t' + DrivingUsingMachines.get()+ "\n")
            self.txtPrescription.insert(END,'How to use: \t\t\t\t' + HowtoUseMedication.get()+ "\n")
            self.txtPrescription.insert(END,'Patient ID: \t\t\t\t' + PatientID.get()+ "\n")
            self.txtPrescription.insert(END,'NHSS NO: \t\t\t\t' + PatientNHSNo.get()+ "\n")
            self.txtPrescription.insert(END,'Patient Name: \t\t\t\t' + PatientName.get()+ "\n")
            self.txtPrescription.insert(END,'DOB: \t\t\t\t' + DateofBirth.get()+ "\n")
            self.txtPrescription.insert(END,'Patient Address: \t\t\t\t' + PatientAddress.get()+ "\n")
            
            
            
            return
        def Receipt():
        
             self.txtFrameDetail.insert(END,"\t"+ cmbNameTablets.get() +"\t\t"+ Ref.get() +"\t"+ Dose.get() +"\t\t"+ NumberTablets.get() +"\t"+ Lot.get() +"\t"+ IssuedDate.get() +"\t\t"+ ExpDate.get() +"\t"+ DailyDose.get()+"\t\t"+ StorageAdvice.get() +"\t"+ PatientNHSNo.get() +"\t\t"+ PatientName.get() +"\t"+ DateofBirth.get() +"\t"+ PatientAddress.get() +"\n")
             self.txtFrameDetail.grid(row=1,column=0)

             return

        def Delete():
            cmbNameTablets.set("")
            self.cboNameTablet.current(0)
            Ref.set("")
            Dose.set("")
            NumberTablets.set("")
            Lot.set("")
            IssuedDate.set("")
            ExpDate.set("")
            DailyDose.set("")
            PossibleSideEffects.set("")
            FurtherInformation.set("")
            StorageAdvice.set("")
            DrivingUsingMachines.set("")
            HowtoUseMedication.set("")
            PatientID.set("")
            PatientNHSNo.set("")
            PatientName.set("")
            DateofBirth.set("")
            PatientAddress.set("")
            self.txtPrescription.delete("1.0",END)
            self.txtFrameDetail.delete("1.0",END)

            return    
        def Reset():
            cmbNameTablets.set("")
            self.cboNameTablet.current(0)
            Ref.set("")
            Dose.set("")
            NumberTablets.set("")
            Lot.set("")
            IssuedDate.set("")
            ExpDate.set("")
            DailyDose.set("")
            PossibleSideEffects.set("")
            FurtherInformation.set("")
            StorageAdvice.set("")
            DrivingUsingMachines.set("")
            HowtoUseMedication.set("")
            PatientID.set("")
            PatientNHSNo.set("")
            PatientName.set("")
            DateofBirth.set("")
            PatientAddress.set("")
            self.txtPrescription.delete("1.0",END)
            #self.txtFrameDetail.delete("1.0",END)

            return
            
    #=========================================frame=======================================================================

        MainFrame=Frame(self.frame)
        MainFrame.grid()

        TitleFrame=Frame(MainFrame,bd=20,width=1350,padx=20,relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle=Label(TitleFrame,width=39, font=('arial',40,'bold'), text="Hospital management system",padx=8)
        self.lblTitle.grid()

        FrameDetail=Frame(MainFrame, bd=20, width=1350, height=100,padx=20,relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        ButtonFrame=Frame(MainFrame, bd=20, width=1350, height=50,padx=20,relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame=Frame(MainFrame, bd=20, width=1350, height=400,padx=20,relief=RIDGE)
        DataFrame.pack(side=BOTTOM)
        DataFrameLEFT=LabelFrame(DataFrame, bd=10, width=800, height=300 ,padx=20, relief=RIDGE, font=('arial',12,'bold'), text="Patient Information:")
        DataFrameLEFT.pack(side=LEFT)
        DataFrameRIGHT=LabelFrame(DataFrame, bd=10, width=450, height=300 ,padx=20, relief=RIDGE, font=('arial',12,'bold'), text="Prescription:")
        DataFrameRIGHT.pack(side=RIGHT)
        #========================================Leftframe===================================================================
        self.lblNameTablet=Label(DataFrameLEFT, font=('arial',12,'bold'), text="Name of tablets",padx=2,pady=4)
        self.lblNameTablet.grid(row=0,column=0,sticky=W)

        self.cboNameTablet=ttk.Combobox(DataFrameLEFT,textvariable=cmbNameTablets, state='readonly',font=('arial',12,'bold'),width=23)
        self.cboNameTablet['values']=('','Ibuprofen','Co-codamol','Paracetamol','Amlodipine')
        self.cboNameTablet.current(0)
        self.cboNameTablet.grid(row=0,column=1)

        self.lblFurtherInfo=Label(DataFrameLEFT, font=('arial',12,'bold'), text="Further information",padx=2,pady=4)
        self.lblFurtherInfo.grid(row=0,column=2,sticky=W)
        self.txtlblFurtherInfo=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=FurtherInformation,width=25)
        self.txtlblFurtherInfo.grid(row=0,column=3)

        self.lblRef=Label(DataFrameLEFT, font=('arial',12,'bold'), text="Reference NO:",padx=2,pady=4)
        self.lblRef.grid(row=1,column=0,sticky=W)
        self.txtlblRef=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Ref,width=25)
        self.txtlblRef.grid(row=1,column=1)

        self.lblStorage=Label(DataFrameLEFT, font=('arial',12,'bold'), text="Storage Avice",padx=2,pady=4)
        self.lblStorage.grid(row=1,column=2,sticky=W)
        self.txtlblStorage=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=StorageAdvice,width=25)
        self.txtlblStorage.grid(row=1,column=3)

        self.lblDose=Label(DataFrameLEFT, font=('arial',12,'bold'), text="Dose:",padx=2,pady=4)
        self.lblDose.grid(row=2,column=0,sticky=W)
        self.txtlblDose=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Dose,width=25)
        self.txtlblDose.grid(row=2,column=1)

        self.lblDUseMachine=Label(DataFrameLEFT, font=('arial',12,'bold'), text="Driving Machine:",padx=2,pady=4)
        self.lblDUseMachine.grid(row=2,column=2,sticky=W)
        self.txtlblDUseMachine=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=DrivingUsingMachines,width=25)
        self.txtlblDUseMachine.grid(row=2,column=3)

        
        self.lblNoOfTablets=Label(DataFrameLEFT, font=('arial',12,'bold'), text="No. of tablets:",padx=2,pady=4)
        self.lblNoOfTablets.grid(row=3,column=0,sticky=W)
        self.txtlblNoOfTablets=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable= NumberTablets,width=25)
        self.txtlblNoOfTablets.grid(row=3,column=1)

        
        self.lblUseMedication=Label(DataFrameLEFT, font=('arial',12,'bold'), text="Driving Medicine:",padx=2,pady=4)
        self.lblUseMedication.grid(row=3,column=2,sticky=W)
        self.txtlblUseMedication=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=HowtoUseMedication,width=25)
        self.txtlblUseMedication.grid(row=3,column=3)

        self.lblPatientID=Label(DataFrameLEFT, font=('arial',12,'bold'), text="Patient ID:",padx=2,pady=4)
        self.lblPatientID.grid(row=4,column=0,sticky=W)
        self.txtlblPatientID=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=PatientID,width=25)
        self.txtlblPatientID.grid(row=4,column=1)
        
        self.lblLot=Label(DataFrameLEFT, font=('arial',12,'bold'), text="Lot:",padx=2,pady=4)
        self.lblLot.grid(row=4,column=2,sticky=W)
        self.txtlblLot=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable= Lot,width=25)
        self.txtlblLot.grid(row=4,column=3)

        self.lblIssuedDate=Label(DataFrameLEFT, font=('arial',12,'bold'), text="Issued Date:",padx=2,pady=4)
        self.lblIssuedDate.grid(row=5,column=0,sticky=W)
        self.txtlblIssuedDate=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=IssuedDate,width=25)
        self.txtlblIssuedDate.grid(row=5,column=1)

        self.lblNHSSNumber=Label(DataFrameLEFT, font=('arial',12,'bold'), text="NHSS Number:",padx=2,pady=4)
        self.lblNHSSNumber.grid(row=5,column=2,sticky=W)
        self.txtlblNHSSNumber=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=PatientNHSNo,width=25)
        self.txtlblNHSSNumber.grid(row=5,column=3)

        self.lblExpDate=Label(DataFrameLEFT, font=('arial',12,'bold'), text="Exp Date:",padx=2,pady=4)
        self.lblExpDate.grid(row=6,column=0,sticky=W)
        self.txtlblExpDate=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=ExpDate,width=25)
        self.txtlblExpDate.grid(row=6,column=1)

        self.lblPatientName=Label(DataFrameLEFT, font=('arial',12,'bold'), text="Patient Name:",padx=2,pady=4)
        self.lblPatientName.grid(row=6,column=2,sticky=W)
        self.txtlblPatientName=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=PatientName,width=25)
        self.txtlblPatientName.grid(row=6,column=3)
        
        self.lblDailyDose=Label(DataFrameLEFT, font=('arial',12,'bold'), text="Daily Dose:",padx=2,pady=4)
        self.lblDailyDose.grid(row=7,column=0,sticky=W)
        self.txtlblDailyDose=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=DailyDose,width=25)
        self.txtlblDailyDose.grid(row=7,column=1)

        self.lblDateofBirth=Label(DataFrameLEFT, font=('arial',12,'bold'), text="Date of Birth:",padx=2,pady=4)
        self.lblDateofBirth.grid(row=7,column=2,sticky=W)
        self.txtlblDateofBirth=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=DateofBirth,width=25)
        self.txtlblDateofBirth.grid(row=7,column=3)

        self.lblSideEffects=Label(DataFrameLEFT, font=('arial',12,'bold'), text="Side effects:",padx=2,pady=4)
        self.lblSideEffects.grid(row=8,column=0,sticky=W)
        self.txtlblSideEffects=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=PossibleSideEffects,width=25)
        self.txtlblSideEffects.grid(row=8,column=1)

        self.lblPatientAddress=Label(DataFrameLEFT, font=('arial',12,'bold'), text="Patient Address:",padx=2,pady=4)
        self.lblPatientAddress.grid(row=8,column=2,sticky=W)
        self.txtlblPatientAddress=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=PatientAddress,width=25)
        self.txtlblPatientAddress.grid(row=8,column=3)
        #======================================RightFrame=========================================================
        self.txtPrescription=Text(DataFrameRIGHT, font=('arial',12,'bold'),width=43, height=14,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)
        #======================================Buttonframe=========================================================
        self.btnPrescription=Button(ButtonFrame,text='Prescription',font=('arial',12,'bold'),width=24,bd=4,command=Prescription)
        self.btnPrescription.grid(row=0,column=0)
        self.btnReceipt=Button(ButtonFrame,text='Receipt',font=('arial',12,'bold'),width=24,bd=4,command=Receipt)
        self.btnReceipt.grid(row=0,column=1)
        self.btnDelete=Button(ButtonFrame,text='Delete',font=('arial',12,'bold'),width=24,bd=4,command=Delete)
        self.btnDelete.grid(row=0,column=2)
        self.btnReset=Button(ButtonFrame,text='Reset',font=('arial',12,'bold'),width=24,bd=4,command=Reset)
        self.btnReset.grid(row=0,column=3)
        self.btnExit=Button(ButtonFrame,text='Exit',font=('arial',12,'bold'),width=24,bd=4,command=Exit)
        self.btnExit.grid(row=0,column=4)
        
        #======================================Framedetail=========================================================

        self.lblLabel=Label(FrameDetail, font=('arial',10,'bold'),pady=8,text="Name of Tablets\t Reference No.\t Doseage\t No. of Tablets\t Lot\t Issued Date\t Exp.Date\t DailyDose\t StorageAdv.\t NHSS number\t Patient name\t Dob\t Address")
        self.lblLabel.grid(row=0,column=0)
        
        self.txtFrameDetail=Text(FrameDetail, font=('arial',12,'bold'),width=141, height=4,padx=2,pady=4)
        self.txtFrameDetail.grid(row=1,column=0)

       #===================================================================================================================
    
        
        



if __name__ =='__main__':
    main()
