import pymysql as p

myconnection=p.connect(host='localhost',user='root',passwd='',database='pyhton')

mycur=myconnection.cursor()

# mycur.execute("select * from employee")
# mycur.execute("select  name , empid from employee where salary > 10000")
mycur.execute("select empid,salary from employee where name='prasad'")
data=mycur.fetchone()

for d in data:
    print(d)

print(mycur.rowcount,"Record Inserted Successfully")

myconnection.commit()

myconnection.close()