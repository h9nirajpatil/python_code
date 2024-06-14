#step 1 : Establish connection between python on Mysql

import  pymysql as p

myconnection=p.connect(host="localhost",user='root',passwd='')
print(myconnection)

#Step 2: Create Cursor---> is a memory area to writr sql queries.

mycursor=myconnection.cursor()

#Step 3: Execute sql quaries..
mycursor.execute("create database pyhton")
print("Database created")

#Step 4: Close the connection
myconnection.close()