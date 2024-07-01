from tkinter import *
import pymysql
import csv

import webbrowser


window=Tk()
window.title("Besant Technologies")
window.configure(background='light blue')
window.geometry("640x480")

def open_link():
    webbrowser.open_new("https://www.besanttechnologies.com/")

def getDetails():
    connection = pymysql.connect(host="localhost", user="root", passwd="",database="company")
    cursor = connection.cursor()
    print("Date :",date.get())
    print("Name :",fname.get())
    print("Mobile Number :",mobile.get())
    print("Alternate Number :",amobile.get())
    print("Email ID :",email.get())
    print("Address :",address.get())
    print("Courses Interested :",course.get())
    print("Batch Preferred:",batch.get())

    print("Referral Name- How you came to know about us :",referral.get())
    print("Are you Experienced or Fresher ? ",exp.get())
    print("Contact Person from Besant ",bcontact.get())
    print("Counsellor :",couns.get())
    print("Fees :",fees.get())
    print("Comment :",comment.get())
    print("Option :",varM.get())
    print("Option :",varF.get())
    
    sdate=date.get()
    sname=fname.get()
    smob=mobile.get()
    amob=amobile.get()
    semail=email.get()
    saddress=address.get()
    scourse=course.get()
    sbatch=batch.get()
    sreferral=referral.get()
    sexp=exp.get()
    sbcontact=bcontact.get()
    scouns=couns.get()
    sfees=fees.get()
    scomment=comment.get()
    svarM=varM.get()
    svarF=varF.get()
    if (sdate == "" or sname=="" or smob=="" or amob=="" or semail=="" or saddress=="" or scourse=="" or sbatch=="" or sreferral=="" or sexp=="" or sbcontact=="" or scouns=="" or sfees=="" or scomment==""):
        print("Empty data")
    else:
        record="insert into besant(Date,Name,Mobile,Amobile,Email,Address,Courses,Batch,Referral,Experience,Besantcontact,Counsellor,Fees,Comment)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(date.get(),fname.get(),mobile.get(),amobile.get(),email.get(),address.get(),course.get(),batch.get(),referral.get(),exp.get(),bcontact.get(),couns.get(),fees.get(),comment.get())
        if varM.get()==1:
            cursor.execute(record)
        connection.commit()
        connection.close()
        with open("employees.csv","w",newline="") as f1:
            a=csv.writer(f1) 
            a.writerow(["Date","Name","Mobile","Amobile","Email","Address","Courses","Batch","Referral","Experience","Besantcontact","Counsellor","Fees","Comment"])
            a.writerow([sdate,sname,smob,amob,semail,saddress,scourse,sbatch,sreferral,sexp,sbcontact,scouns,sfees,scomment])
        print("data updated in CSV")
        linkAdd = Button(window,text='Click Here to Enter Besant Website',command = open_link)
        linkAdd.place(x=190,y=350)
        
    date.delete(0,END)
    fname.delete(0,END)
    mobile.delete(0,END)
    amobile.delete(0,END)
    
    email.delete(0,END)
    address.delete(0,END)
    course.delete(0,END)    
    batch.delete(0,END)

    referral.delete(0,END)
    exp.delete(0,END)    
    bcontact.delete(0,END)

    couns.delete(0,END)
    fees.delete(0,END)    
    comment.delete(0,END)


    

#window.title("Besant Technologies")
#window.configure(background='light blue')
#window.geometry("640x480")

varM=IntVar()
varF=IntVar()

Label(window, text='Besant Technologies Enquiry Form').grid(row=1, column=1, sticky=W+E)
Label(window, text='Date :').grid(row=2,sticky=W)
Label(window, text='Name :').grid(row=3,sticky=W)
Label(window, text='Mobile No :').grid(row=4,sticky=W)
Label(window, text='Alternate Mobile No :').grid(row=5,sticky=W)

Label(window, text='Email ID :').grid(row=6,sticky=W)
Label(window, text='Address').grid(row=7,sticky=W)
Label(window, text='Course Interested').grid(row=8,sticky=W)
Label(window, text='Batch Preferred :').grid(row=9,sticky=W)


Label(window, text='Referral - How you came to know about Besant :').grid(row=10,sticky=W)
Label(window, text='Experienced or Fresher ? ').grid(row=11,sticky=W)
Label(window, text='Contact Person from Besant Technologies :').grid(row=12,sticky=W)


Label(window, text='Counsellor').grid(row=13,sticky=W)
Label(window, text='Fees').grid(row=14,sticky=W)
Label(window, text='Comments').grid(row=15,sticky=W)


date=Entry(window)
date.grid(row=2,column=1,ipadx="80")
fname=Entry(window)
fname.grid(row=3,column=1,ipadx="80")
mobile=Entry(window)
mobile.grid(row=4,column=1,ipadx="80")
amobile=Entry(window)
amobile.grid(row=5,column=1,ipadx="80")

email=Entry(window)
email.grid(row=6,column=1,ipadx="80")
address=Entry(window)
address.grid(row=7,column=1,ipadx="80")
course=Entry(window)
course.grid(row=8,column=1,ipadx="80")
batch=Entry(window)
batch.grid(row=9,column=1,ipadx="80")


referral=Entry(window)
referral.grid(row=10,column=1,ipadx="80")
exp=Entry(window)
exp.grid(row=11,column=1,ipadx="80")
bcontact=Entry(window)
bcontact.grid(row=12,column=1,ipadx="80")

couns=Entry(window)
couns.grid(row=13,column=1,ipadx="80")
fees=Entry(window)
fees.grid(row=14,column=1,ipadx="80")
comment=Entry(window)
comment.grid(row=15,column=1,ipadx="80")




checkM=Checkbutton(window,bg="Red",text="Register",variable=varM)
checkM.grid(row=16,column=1,sticky=W)
checkF=Checkbutton(window,bg="Pink",text="Enquire",variable=varF)
checkF.grid(row=16,column=1,sticky=E)

Button(window,text="Submit",bg="Green",command=getDetails).grid(row=18)

mainloop()

