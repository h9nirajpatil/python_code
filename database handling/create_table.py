import pymysql as p

myconnection=p.connect(host='localhost',user='root',passwd='',database='pyhton')
# print(myconnection)

mycur=myconnection.cursor()

mycur.execute("create table employee(empid int primary key , name varchar(30) , salary float , DOB date)")
print("table created")

myconnection.close()