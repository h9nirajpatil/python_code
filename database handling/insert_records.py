import pymysql as p

myconnection=p.connect(host='localhost',user='root',passwd='',database='pyhton')

mycur=myconnection.cursor()

mycur.execute("insert into employee values(101,'Niraj',2000.000,'2021-01-12')")
myconnection.commit()
print("record inserted")

myconnection.close()

