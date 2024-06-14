import pymysql as p

myconnection=p.connect(host='localhost',user='root',passwd='',database='pyhton')

mycur=myconnection.cursor()

mycur.execute("delete from employee where empid=101")
myconnection.commit()#saving record permanetly
print(" record deleted....")

myconnection.close()