import pymysql as p

myconnection=p.connect(host='localhost',user='root',passwd='',database='pyhton')

mycur=myconnection.cursor()

vsal=input("Enter the salary:")

mycur.execute("update employee set salary='"+vsal+"' where empid=101")
print('updated...')

myconnection.commit()

myconnection.close()