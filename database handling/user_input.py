import pymysql as p

myconnection=p.connect(host='localhost',user='root',passwd='',database='pyhton')

mycur=myconnection.cursor()

vid=input("Enter the Empid:")
vname=input(("Enter the Name:"))
vsal=input("Enter the Salary:")
vdate=input("Enter the Date:")

mycur.execute("insert into employee values('"+vid+"','"+vname+"','"+vsal+"','"+vdate+"')")
print('record inserted...')

myconnection.commit()

myconnection.close()