from tkinter import *
from tkinter import messagebox,ttk
import pymysql

win=Tk()
win.geometry('800x600')
win.title("Employee Database Management System")


def insert():
    veid=e_id.get()
    vename=e_name.get()
    vsalary=e_salary.get()

    myconn=pymysql.connect(host="localhost",user="root",passwd="",database='tkinter')
    cur=myconn.cursor()

    cur.execute("insert into employee values('"+veid+"','"+vename+"','"+vsalary+"')")
    myconn.commit()

    messagebox.showinfo("Data Status","Inserted Successfully")
    myconn.close()

def delete():
    if(e_id.get()==""):
        messagebox.showinfo("delete status","ID is compulsory to delete")

    else:
        myconn = pymysql.connect(host="localhost", user="root", passwd="", database='tkinter')
        cur = myconn.cursor()

        veid = e_id.get()
        cur.execute("delete from employee where empid='" + veid + "'")
        myconn.commit()

        messagebox.showinfo("Data Details", "Deleted Successfully")
        myconn.close()

def showData():
    myconn = pymysql.connect(host="localhost", user="root", passwd="", database='tkinter')
    cur = myconn.cursor()

    cur.execute("select * from employee")
    data = cur.fetchall()

    tv=ttk.Treeview(win,columns=(1,2,3) ,show="headings",height="10")
    tv.place(x=10 ,y=300)

    tv.heading(1,text="Employee ID")
    tv.heading(2,text="Employee Name")
    tv.heading(3,text="Employee Salary")

    for d in data:
        tv.insert('','end',value=d)

def update():
    if(e_id.get()==""):
        messagebox.showinfo("Update status","ID is compulsory to Update")

    else:
        myconn = pymysql.connect(host="localhost", user="root", passwd="", database='tkinter')
        cur = myconn.cursor()

        veid = e_id.get()
        vsalary = e_salary.get()

        cur.execute("update employee set salary='"+vsalary+"' where empid='"+veid+"'")
        myconn.commit()

        messagebox.showinfo("Data Details", "Updated Successfully")
        myconn.close()

empid=Label(win,text='Enter The Empid')
empid.place(x=20,y=100)

e_id=Entry(win)
e_id.place(x=120,y=100)

name=Label(win,text='Enter The Name')
name.place(x=20,y=140)

e_name=Entry(win)
e_name.place(x=120,y=140)

salary=Label(win,text='Enter The Salary')
salary.place(x=20,y=180)

e_salary=Entry(win)
e_salary.place(x=120,y=180)

ins=Button(win,text='INSERT',command=insert)
ins.place(x=20,y=240)

de=Button(win,text='DELETE',command=delete)
de.place(x=80,y=240)

update=Button(win,text='UPDATE',command=update)
update.place(x=140,y=240)

getdata=Button(win,text='GET DATA')
getdata.place(x=200,y=240)

showall=Button(win,text='SHOW ALL',command=showData)
showall.place(x=280,y=240)

clear=Button(win,text='CLEAR')
clear.place(x=360,y=240)

win.mainloop()