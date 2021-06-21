from tkinter import *
from tkinter import ttk
import random
import time;
import datetime
from tkinter import messagebox

class Hospital:


    def __init__(self,root):
        self.root=root
        self.root.title("Hospital management system")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background='powder blue')

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
                root.destroy()
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

        MainFrame=Frame(self.root)
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




if __name__=='__main__':
    root=Tk()
    application=Hospital(root)
    root.mainloop()











        
