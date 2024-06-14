import pymysql as p
myconnection=p.connect(host='localhost',user='root',passwd='',database='school')
mycur=myconnection.cursor()
def createtable():
    mycur.execute("create table student(rollno int primary key , name varchar(30) , marks float , DOB date)")#creating table
    print("table created")
def insertrecords():
    vroll = input("Enter the Rollno.:")#for user
    vname = input("Enter the Name:")#for user
    vmark = input("Enter the Marks:")#for user
    vdate = input("Enter the Date:")#for user
    mycur.execute("insert into student values('" + vroll + "','" + vname + "','" + vmark + "','" + vdate + "')")#user defined
    print('record inserted...')
    myconnection.commit()# saving record permanetly
def fetchrecords():
    mycur.execute("select * from student")
    data = mycur.fetchall()#student table all values fetchall in one varable that is data
    for d in data:
        print(d)
    print(mycur.rowcount, "Record Inserted Successfully")
    myconnection.commit()# saving record permanetly
def updaterecords():
    vroll = input("Enter the Rollno.:")  # for user
    vmark = input("Enter the Marks:")  # for user
    mycur.execute("update student set marks='"+vmark+"' where rollno='"+vroll+"'")
    myconnection.commit()  # saving record permanetly
    print("update record inserted....")

def deleterecords():
    vroll = input("Enter the Rollno.:")  # for user
    mycur.execute("delete from student where rollno='"+vroll+"'")
    myconnection.commit()  # saving record permanetly
    print(" record deleted....")
# tablecreated=createtable()
# valueinserted=insertrecords()
# fechingdata=fetchrecords()
# recordsupdated=updaterecords()
# recordsdeleted=deleterecords()
# myconnection.close()

while(True):

    print("1.insert\n2.showData\n3.update\n4.delete\n5.exit")
    choice=int(input('enter the choice:'))

    if choice==1:
        insertrecords()
    elif choice==2:
        fetchrecords()
    elif choice==3:
        updaterecords()
    elif choice==4:
        deleterecords()
    elif choice==5:
        exit()
    else:
        print('invalid choice')


