import pymysql as p

myconnection=p.connect(host='localhost',user='root',passwd='',database='pyhton')

mycur=myconnection.cursor()

query="insert into employee(empid,name,salary,DOB) values (%s,%s,%s,%s)"

values=[(101,'Niraj',90000.00,'1999-02-23'),(102,'Girish',10000.00,'1996-12-10'),(103,'Prasad',15000.00,'2000-06-16')]

mycur.executemany(query,values)  #to insert mutiple records

print(mycur.rowcount,"Record Inserted Successfully")

myconnection.commit()

myconnection.close()