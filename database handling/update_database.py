import pymysql as p

myconnection=p.connect(host='localhost',user='root',passwd='',database='pyhton')

mycur=myconnection.cursor()

mycur.execute("update employee set salary=5000 where empid=101")
myconnection.commit()#saving record permanetly
print("update record inserted....")

myconnection.close()