# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 11:29:07 2024

@author: Jossy
"""


import mysql.connector
obj=mysql.connector.connect(host="localhost",user="root",password="",auth_plugin='mysql_native_password')
mycursor=obj.cursor()

#Database
mycursor.execute("create database if not exists hms") 
mycursor.execute("use hms")

# create table for Patient
mycursor.execute("create table if not exists patient(patientid int auto_increment primary key, pname varchar(30) not null, page int(3)not null, pgender varchar(6) not null, phoneno bigint(10) not null, admitdate date, patient_problem varchar(30) not null)")
# create table for patient record
mycursor.execute("create table if not exists patientrecord(patientid int not null, pname varchar(30) not null, page int(3) not null, pgender varchar(6) not null, phoneno bigint(10) not null, admitdate date, dischargedate date)")
# create table for doctor 
mycursor.execute("create table if not exists doctor(doctorid int auto_increment primary key, doctorname varchar(40) not null, department varchar(40) not null, gender varchar(6) not null, work_experience int(5) not null, phone_number bigint(10) not null, dateofjoinig date, salary int (10)not null)")
# create table for doctor record 
mycursor.execute("create table if not exists doctorrecord(doctorid int, doctorname varchar(40) not null, department varchar(40) not null, gender varchar(6) not null, phone_number bigint(10) not null, dateofjoinig date, date_of_relived date)") 
# create table for symptoms and department
mycursor.execute("create table if not exists symptoms_and_dept(symptoms varchar(50), department varchar(40))")
# create table for appointment 
mycursor.execute("create table if not exists appointment(patient_name varchar(30) not null, age int(2) not null, gender varchar(6)not null,mobile_number bigint(10) not null, doctorid int(12) not null, department varchar(40))")

# for admin
def admin():
    n="n"
    while n=="n":
        print("")
        print("*"*15,"WELCOME TO ADMIN SECTION","*"*15)
        print("_______________________________________")
        print(" press 1 to ADD PATIENT: ")
        print("---------------------------------------")
        print(" press 2 to DISPLAY PATIENT RECORD: ")
        print("---------------------------------------")
        print(" press 3 to REMOVE PATIENT RECORDS: ")
        print("---------------------------------------")
        print(" press 4 to UPDATE PATIENT RECORDS': ")
        print("---------------------------------------")
        print(" press 5 to ADD DOCTOR: ")
        print("---------------------------------------")
        print(" press 6 to REMOVE DOCTOR: ")
        print("---------------------------------------")
        print(" press 7 To go back")
        print("_______________________________________")
        
        choice=int(input("ENTER YOUR CHOICE :- "))
        if choice==1:
            addpatients()
        elif choice==2: 
            patientsrecord()
        elif choice==3: 
            removepatients()
        elif choice==4: 
            update_patient()
        elif choice==5:
            add_doctor()
        elif choice==6:
            removedoctor()
        elif choice==7:
            front()
        else:
           print("INVALID CHOISE")
      
# To add patients
def addpatients():
    y="y"
    while y=="y":
        p=0
        
        print("*"*17,"ENTER PATIENT DETAILS","*"*17) 
        patientname=input("Enter Patient's Name:")
        
        for i in patientname: 
            if i.isdigit()==True:
                p=p+1 
            else:
                pass
            
        if p==0:
            age=input("Enter Patient's Age:")
            if age.isdigit()!=True:
                print("\n!!!...invalid age...!!!")
                print("please try again...")
                addpatients()
        else:
            print("\n!!!...INVALID NAME...!!!")
            print("please try again")
            print("")
            addpatients()
            return
                
        print("*"*13,"Select your gender","*"*13)
        print("if patient is male then press 1")
        print("if patient is female then press 2")
        choice=int(input("Enter the no. corresponding to your gender :-"))
        if choice==1:
            gender="Male"
            pass
        elif choice==2:
            gender="Female"
            pass
        else:
            print("!"*15,"INVALID CHOICE","!"*15) 
            addpatients()
            return
        mobnumber=input("Enter the patient's 10 digit mobile number:")
        if len(mobnumber)==10: 
            if mobnumber.isalpha(): 
                print("invalid mobile number")
                
            else:
                if mobnumber.isdigit()!=True: 
                    print("!"*15,"invalid mobile number","!"*15) 
                    addpatients()
                else:
                    if mobnumber.startswith("0"): 
                        print("!"*13,"mobile number can not start with 0","!"*13)
                    else:
                        
                        print("*"*15,"Enter patient's illness","*"*15)
                        print("----------------------------")
                        print("1. Eye related issues")
                        print("2. Ear related issues")
                        print("3. Nose related issues")
                        print("4. Throat related issues")
                        print("5. Hormones related issues")
                        print("6. Mouth related issues")
                        print("7. Surgical related issues")
                        print("8. Bone related issues")
                        print("9. Diabetes related issues")
                        print("10. Skin related issues")
                        print("11. Stomach related issues")
                        print("12. other issues")
                        
                        ch=int(input("enter the choice:"))   
                        if ch==1:
                            q="Eye related issues"
                            pass
                        elif ch==2:
                            q="Ear related issues"
                            pass
                        elif ch==3:
                            q="Nose related issues"
                            pass
                        elif ch==4:
                            q="Throat related issues"
                            pass
                        elif ch==5:
                            q="Hormones related issues"
                            pass
                        elif ch==6:
                            q="Mouth related issues"
                            pass
                        elif ch==7:
                            q="Surgical related issues"
                            pass
                        elif ch==8:
                            q="Bone related issues"
                            pass
                        elif ch==9:
                            q="Diabetes related issues"
                            pass
                        elif ch==10:
                            q="Skin related issues"
                            pass
                        elif ch==11:
                            q="Stomach related issues"
                            pass
                        elif ch==12:
                            q="Other issues"
                            pass
                        else:
                            print("invalid choice")
                            addpatients()
                        a="insert into patient values({},'{}',{},'{}',{},{},'{}')".format('patientid=patientid+100',patientname,age,gender,mobnumber,"curdate()",q)
                        mycursor.execute(a)
                        
                        patientid="select patientid from patient where pname='{}' and page={}".format(patientname,age) 
                        mycursor.execute(patientid) 
                        patientid=mycursor.fetchall()
                        
                        print("\n**********Patient added SUCCESSFULLY and Patient ID is", patientid[0][0], "**********")
                        
                        obj.commit()
                        
                        y=input("Do you want to add more patient(y/n):")
                        if y=="y":
                            addpatients()
                            
                        else:
                            admin()
                            
        else:
            print("\n!!!...Invalid Mobile number...!!!")
            print(" please try again")
            obj.commit()
            
        
#For patient record

def patientsrecord():
    y="y"
    while y=="y":
        
        pid=input("Enter patient ID:")
        if pid.isdigit()!=True:
            print("!"*15,"INVALID ID","!"*15)
        else:
            a="select patientid from patient where patientid={}".format(pid) 
            mycursor.execute(a)
            b=mycursor.fetchall()
            
            if len(b)<1:
                a="select patientid from patientrecord where patientid={}".format(pid)
                mycursor.execute(a)
                b=mycursor.fetchall()
                
                if len(b)<1:
                    print("!"*17,"INVALID PATIENT ID","!"*17)
                    print("OR".center(50))
                    print("!"*12," if ID is incorrect, please try again","!"*12)
                else:
                    result="select * from patientrecord where patientid={}".format(pid) 
                    mycursor.execute(result)
                    result1=mycursor.fetchall()
                    
                    print("*"*12,"PATIENT DETAILS ARE GIVEN BELOW:","*"*12)
                    print("\n patient id is:", result1[0][0])
                    print("\n patient name is:", result1[0][1])
                    print("\n patient age is:",result1[0][2])
                    print("\n patient gender is:", result1[0][3])
                    print("\n patient phone number is:", result1[0][4])
                    print("\n patient admit date:",result1[0][5])
                    print("\n patient discharge date:", result1[0][6])   
                    
                    y=input("Do you want more patient record(y/n):")
            else:
                result="select * from patient where patientid={}".format(pid)
                mycursor.execute(result) 
                result1=mycursor.fetchall()
                print("*"*12,"PATIENT DETAILS ARE GIVEN BELOW:","*"*12)
                print("\n patient id is:", result1[0][0])
                print("\n patient name is:", result1[0][1])
                print("\n patient age is:",result1[0][2])
                print("\n patient gender is:",result1[0][3])
                print("\n patient problem:",result1[0][6])
                print("\n patient phone number is:", result1[0][4])
                print("\n patient admit date:",result1[0][5]) 
                y=input("Do you want more patient record(y/n):") 
                
# To remove patient details from hospital
def removepatients():
    y="y"
    while y=="y":
        ID=int(input("enter patient id "))
        a="select * from patient where patientid={} ".format(ID) 
        mycursor.execute(a)
        result1=mycursor.fetchall()
        
        if len(result1)<1:
            b="select * from patientrecord where patientid={}".format(ID) 
            mycursor.execute(b)
            result2=mycursor.fetchall()
            if len(result2)<1:
                print("\n###...PATIENT ID IS INCORRECT !!!!###")
            else:
                print("###...PATIENT IS ALREADY REMOVED !!!### ") 
                admin()
        
        else:
            print("Do you confirm remove this", ID, "if yes press(y) else press any key except(y)):") 
            ch=input("y or n ? ")
            if ch=="y":
                
                b="select * from patient where patientid={}".format(ID)
                mycursor.execute(b)
                result2=mycursor.fetchall()
                
                pname=result2[0][1]
                page=result2[0][2]
                pgender=result2[0][3]
                phoneno=result2[0][4]
                admitdate=result2[0][5]
                admitdate=str(admitdate)
                admitdate=admitdate.replace("-","")
                
                patientrecord="insert into patientrecord values({},'{}',{},'{}',{},{},{})".format(ID,pname,page,pgender,phoneno,admitdate,"curdate()")
                mycursor.execute(patientrecord)
                
                deletepatient="delete from patient where patientid={}".format(ID) 
                mycursor.execute(deletepatient)
                
                print("\n************DISCHARGE SUCCESSFUL*******************") 
                obj.commit()
                y=input("Do you want to remove more patients(y/n):")
            else:
                admin()
                
# to update patient information

def update_patient():
    y="y"
    while y=="y":
        ID=input("enter patient ID :")
        if ID.isdigit()!=True:
            print("!"*15,"INVALID ID","!"*15)
        else:
            a="select * from patient where patientid={} ".format(ID)
            mycursor.execute(a)
            result1=mycursor.fetchall()
            if len(result1)<1:
                    print("\n###...PATIENT ID IS INCORRECT...!!!!")
                    print(" please try again ")
            else:
                    print("what do you want to update??")
                    print("press 1 to update patient name")
                    print("press 2 to update patient age")
                    print("press 3 to update patient gender")
                    print("press 4 to update patient phone number")
                    ch=int(input("Enter your choice :- "))
                    if ch==1: 
                        update_patient_name(ID)
                    elif ch==2: 
                        update_patient_age(ID)
                    elif ch==3:
                        print("if patient is male then press 1")
                        print("if patient is female then press 2")
                        choice=int(input("Enter the no. corresponding to the gender"))
                        if choice==1: 
                            update_patient_male(ID)
                        elif choice==2: 
                            update_patient_female(ID)
                        else: 
                            print("!"*15,"INVALID CHOICE","!"*15)
                    elif ch==4: 
                        update_patient_phone_number(ID)
                    else: 
                        print("!"*15,"INVALID CHOICE","!"*15)
                    y=input("Do you want to update the details of more patients??(y/n):")
                    
# to update patient name 

def update_patient_name(ID):
    
    p=0
    name=input("Enter patient name:")
    for i in name: 
        if i.isdigit()==True: 
            p=p+1 
        else: 
            pass
            
    if p==0:
        up="update patient set pname='{}' where patientid={}".format(name, ID) 
        mycursor.execute(up) 
        obj.commit() 
        print("*"*15,"PATIENT NAME UPDATED SUCCESSFULLY","*"*15) 
        y=input("Do you want to update the name of more patient??(y/n):")
        if y=="y":
            update_patient()        
        else:
            admin()

    else:
        print("!"*15,"INVALID NAME","!"*15)
        
# to update patient age 

def update_patient_age(ID):
    
    age=input("Enter patient age:")
    if age.isdigit()!=True:
        print("!"*15,"INVALID AGE","!"*15)
        update_patient_age(ID)
    else:
        up="update patient set page={} where patientid={}".format(age, ID) 
        mycursor.execute(up)
        obj.commit() 
        print("*"*15,"PATIENT AGE UPDATE SUCCESSFUL","*"*15)
        y=input("Do you want to update the age of more patients??(y/n):")
        if y=="y":
            update_patient()
        else:
            admin()
    
# to update patient gender if male 

def update_patient_male(ID):
    
    gender="male"
    up="update patient set pgender='{}' where patientid={}".format(gender, ID) 
    mycursor.execute(up)
    obj.commit()
    print("*"*15,"PATIENT GENDER UPDATE SUCCESSFUL","*"*15)
    y=input("Do you want to update the gender of more patient??(y/n):")
    if y=="y":
        update_patient()
    else:
        admin()
        
# to update patient gender if female 

def update_patient_female(ID):
    
    gender="female"
    up="update patient set pgender='{}' where patientid={}".format(gender, ID) 
    mycursor.execute(up)
    obj.commit()
    print("*"*15,"PATIENT GENDER UPDATE SUCCESSFUL","*"*15)
    y=input("Do you want to update the gender of more patient??(y/n):")
    if y=="y":
        update_patient()
    else:
        admin()
        
# To update patient phone number 

def update_patient_phone_number(ID):
    
    phone=input("enter the patient 10 digit phone number:")
    if len(phone)==10:
        if phone.isalpha():
            print("invalid mobile number")
            update_patient_phone_number(ID)
            
        else:   
            if phone.isdigit()!=True:
                print("!"*15,"invalid mobile number","!"*15)
                update_patient_phone_number(ID)
            else:
                if phone.startswith("0"):
                    print("!"*13,"mobile number can not start with 0","!"*13) 
                    update_patient_phone_number(ID)
                else:
                    up="update patient set phoneno={} where patientid={}".format(phone, ID)
                    mycursor.execute(up) 
                    obj.commit() 
                    print("*"*15,"PATIENT PHONE NUMBER UPDATE SUCCESSFUL","*"*15)
                    y=input("Do you want to update the phone number of more patients??(y/n):")
                    if y=="y":
                        update_patient()
                    else:   
                        admin()
    else:
        print("!"*15,"INVALID PHONE NUMBER","!"*15)
        update_patient_phone_number(ID)
                


# To add doctor

def add_doctor():
        
    p=0
    print("*"*15," ENTER DOCTOR DETAILS","*"*15) 
    name=input("Enter Doctor Name:")
    for i in name: 
        if i.isdigit()==True: 
            p=p+1 
        else: 
            pass
        
    if p==0:
        department=input("enter the department:")       
        for i in department:
            
            if i.isdigit()==True:
                p=p+1
            else: 
                pass
    
        if p==0:
            print("If doctor is male then press 1")
            print("If doctor is female then press 2")
            choice=int(input("Enter the number corresponding to the gender"))
            if choice==1:
                gender="male"
                pass
            elif choice==2:
                gender="female"
                pass
            else:
                print("!"*13,"invalid choice","!"*13)
                add_doctor()
                
            
            work_experience=input("Enter the work experience (in years):")
            if work_experience.isdigit()==True:
                phone_number=input("Enter the Doctor's 10 digit phone number:")
                if len(phone_number)==10:
                    if phone_number.isalpha():
                        print("invalid mobile number")
                        add_doctor()
                    else:
                        if phone_number.isdigit()!=True:    
                            print("!"*15,"invalid mobile number","!"*15) 
                            add_doctor()
                        else:
                            if phone_number.startswith("0"):
                                print("!"*13,"mobile number can not start with 0","!"*13)
                                add_doctor() 
                            else:
                                salary=input("Enter salary of the Doctor:")
                                if salary.isdigit()==True:
                                    a="insert into doctor values({},'{}','{}','{}',{},{},{},{})".format('null', name, department, gender, work_experience,
                                           phone_number, "curdate()", salary)
                                    
                                    mycursor.execute(a)
                                    obj.commit()
                                    
                                    doctorid="select doctorid from doctor where doctorname='{}' and department='{}'".format(name,department) 
                                    mycursor.execute(doctorid)
                                    doctorid=mycursor.fetchall()
                                    
                                    print("*"*15, "DOCTOR ADDED SUCCESSFULLY AND DOCTOR ID IS", doctorid[0][0],"*"*15)
                                else:
                                    print("\n!!!!...invalid salary...!!!!")
                                    print("please try again ")
                                    add_doctor()
                else:
                    print("!"*15,"invalid mobile number","!"*15) 
                    add_doctor()
            else:
                print("\n!!!!...invalid work experience!!!...")
                print("please try again")
                add_doctor()
        else:
            print("\n!!!!...invalid department...!!!")
            print("please try again")
            add_doctor()
    else:
        print("!"*15,"invalid name","!"*15)
        add_doctor()
        
# To Remove doctor

def removedoctor():
    
    y="y"
    while y=="y":
        ID=int(input("Enter Doctor ID"))
        a="select * from doctor where doctorid={} ".format(ID)
        mycursor.execute(a)
        result1=mycursor.fetchall()
        if len(result1)<1:
            b="select * from doctorrecord where doctorid={}".format(ID)     
            mycursor.execute(b)
            result2=mycursor.fetchall()
            if len(result2)<1:
                print("\n###...DOCTOR ID IS INCORRECT!...####")
            else:
                print("####...DOCTOR HAS BEEN ALREADY REMOVED!...####")
                
        else:
            print("Are you sure to remove ID NO.",ID,"if yes press(y) else press (n):") 
            ch=input("Enter y or n :-")
            
            if ch=="y":
                b="select * from doctor where doctorid={}".format(ID)
                mycursor.execute(b)
                result2=mycursor.fetchall()
                
                doctorname=result2[0][1]
                dateofjoining=result2[0][6]
                dateofjoining=str(dateofjoining)
                dateofjoining=dateofjoining.replace("-","")
                department=result2[0][2]
                gender=result2[0][3]
                phone_number=result2[0][5]
                
                doctorrecord="insert into doctorrecord values({},'{}','{}','{}',{},{},{})".format(ID,doctorname,department,gender,
                                                                                                      phone_number, dateofjoining,"curdate()")
                mycursor.execute(doctorrecord)    
                                
                deletedoctor="delete from doctor where doctorid={}".format(ID) 
                mycursor.execute(deletedoctor)
                print("\n********REMOVED SUCCESSFULLY******")
                obj.commit()
                y=input("Do you want TO REMOVEmore patientS (y/n):")
            else:
                admin()       

#for front page design

def front():
    
    print("")
    print(" "*10,"*"*70)
    print(" ")
    print("WELCOME TO BMI HOSPITAL".center(80))
    print(" ")
    print(" "*10,"*"*70)
    print(" ")
    print("        _______________________________________")
    print("        |         press 1 for ADMIN:          |")        
    print("        ---------------------------------------")
    print("        |          press 2 for PATIENT:       |")
    print("        ---------------------------------------")
    print("        |         press 3 for EXIT:           |")        
    print("        _______________________________________")

    ch=int(input("Enter your choice :-"))
    if ch==1:
        admin()
    elif ch==2:
        patient()
    elif ch==3:
        print("*"*16,"THANK YOU", "*"* 16)
        while True:
            break
    else:
        print("INVALID CHOICE")
        front()
        
        
# for patient use

def patient():
        print("*"*15,"WELCOME TO OUR MOBILE APPLICATION", "*"*15)
        print("press 1 To Book Appointment")
        print("press 2 To go back")
        ch=int(input("Enter your choice:-"))
        if ch==1:
            appointment()
        elif ch==2:
            front()
        else:
            print("!!!...invalid choice...!!!\n")
            patient()

# for booking appointment

def appointment():
    print("#"*15,"SELECT YOUR CATEGORY OF ILLLNESS","#"*15)
    print("1. Eye related issues")
    print("2. Ear related issues")
    print("3. Nose related issues")
    print("4. Throat related issues")
    print("5. Hormones related issues")
    print("6. Mouth related issues")
    print("7. Surgical related issues")
    print("8. Bone related issues")
    print("9. Diabetes related issues")
    print("10. Skin related issues")
    print("11. Stomach related issues")
    print("12. other issues")
    print("13. To go back ")
    
    ch=input("enter the choice:")
    if ch=="1":
        q="Eye"
        app(q)
    elif ch=="2":
        q="ear"
        app(q)
    elif ch=="3":
        q="nose"
        app(q)
    elif ch=="4":
        q="throat"
        app(q)
    elif ch=="5":
        q="hormones"
        app(q)
    elif ch=="6":
        q="mouth"
        app(q)
    elif ch=="7":
        q="surgical"
        app(q)
    elif ch=="8":
        q="bone"
        app(q)
    elif ch=="9":
        q="diabetes"
        app(q)
    elif ch=="10":
        q="Skin"
        app(q)
    elif ch=="11":
        q="stomach"
        app(q)
    elif ch=="12":
        q="other"
        app(q)
    elif ch=="13":
        patient()
        
    else:
        print("invalid choice\n")           
        appointment()

def app(q):
    a="select department from symptoms_and_dept where symptoms like'%{}%'".format(q)
    mycursor.execute(a)
    b=mycursor.fetchall()
    b=b[0][0]                      # b is name of department
    #print("department ",b)
    
    c="select * from doctor where department='{}'".format(b)
    mycursor.execute(c)
    c=mycursor.fetchall() # c is list of doctors
    #print("doctor name ",c)
    d=len(c)
    print("There are ",d,"doctor(s)")
    
    for i in c:
        print("")                                               
        print("Doctor ID:",i[0]) 
        print("Doctor Name:",i[1]) 
        print("Department:",i[2])
        print("Gender:",i[3])
        print("Work Experience:",i[4])
        print("")
        
    y="y"
    while y=="y":
        book=input("Do you want to book an appointment? (y/n):")
        if book=="y":
            
            ID=input("\n Enter the  Doctor ID:")
            if ID.isdigit():
                e="select * from doctor where doctorid={}".format(ID)   
                mycursor.execute(e)
                e=mycursor.fetchall()   #e is details of a particular doctor
                #print(e)    
                if len(e)<1:
                    print("INVALID DOCTOR ID")
                    app(q)
                else:
                    select="select doctorid from doctor where doctorid like'%{}%'".format(ID) 
                    mycursor.execute(select)
                    select=mycursor.fetchall() # select is doctor id
                    #print("DOCTOR ID :", select)
                    #print(select)
                    L=[]
                    for i in select:
                        L.append(i[0])
                    #print(L)
                    for ID in L:
                        p=0
                        name=input("Enter your name:")
                        for item in name: 
                            if item.isdigit()==True: 
                                p=p+1
                            else:
                                pass
                        
                        if p==0:
                            age=input("Enter your age:")
                            if age.isdigit()!=True:
                                print("\n!!!!...invalid age...!!!!")
                                print("Please try again")
                            else:
                                print("If you are male then press 1")
                                print("If you are female then press 2")
                                choice=int(input("Enter the number corresponding to your gender"))
                                if choice==1:
                                    gender="male"
                                else:
                                    gender="female"
                                    pass
                                mobile_number=input("Enter your mobile number:")
                                if len(mobile_number):
                                    insert=" insert into appointment values('{}',{},'{}',{},{},'{}')".format(name
                                               , age, gender, mobile_number, ID,b)

                                    mycursor.execute(insert)
                                    obj.commit()
                                    print("\n Appointment booked Successfully!")
                                    print("")
                                    patient()

                                else:
                                    print("invalid mobile number")
                        else:
                            print("\n!!!!...invalid name...!!!!")
                            print(" Please try again!")
                # else:
                        # print("\nDoctor of this ID", ID, "is not related to", q,"problem\n")
            else:
                print("INVALID DOCTOR ID")
                app(q)
        elif book=="n":
            patient()
        else:
            print("!"*12,"INVALID CHOICE","!"*12)
            y=input("Do you want to book more appointments? (y/n):")
                        
        
# for introduction
def front_page():
    print("")
    print("_"*58)
    print("@"*15,"COMPUTER SCIENCE PROJECT","@"*15)
    print("."*18,"SESSION: 2024-2025","."*16)
    print("."*25,"WELCOME","."*25)
    print("."*28,"TO","."*27)
    print("."*18,"HOSPITAL MANAGEMENT SYSTEM","."*13)
    print("."*21,"MADE BY: Jeevan Jossy","."*16)
    print("."*24,"CLASS: XII-D ","."*10)
    print("_"*58)
    print("")
    
while True:
    
    front_page()
    print("")
    print(" "*10,"*"*70)
    print(" ")
    print("WELCOME TO HOSPITAL MANAGEMENT SYSTEM".center(80))
    print(" ")
    print(" "*10,"*"*70)
    print(" ")
    print("        _______________________________________")
    print("        |         press 1 for ADMIN:          |")        
    print("        ---------------------------------------")
    print("        |          press 2 for PATIENT:       |")
    print("        ---------------------------------------")
    print("        |         press 3 for EXIT:           |")        
    print("        _______________________________________")
    
    ch=input("Enter your choice:- ")
    
    if ch=="1":
        admin()
    elif ch=="2":
        patient()
    elif ch=="3":
        print("*"*16,"THANK YOU","*"*16)
        break
    else:
        print("!"*10,"INVALID CHOICE","!"*10)
        
        
    
        
        
        
        
        
                        
                        
                        
                        
                        
                        
                        
        
        
