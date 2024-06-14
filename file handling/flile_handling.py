#create empty files

# myfile=open("abc.txt",'x')
#
# myfiles=open('c://yash//abc.txt','x')


#create and write same content to the files

# myfile=open('test.txt','w')
# myfile.write("Hello how r you...")
# print('file created with same contents')
# myfile.close()

#create and append same content to the files modify


# myfile=open('test.txt','a')
# myfile.write("good evening...")
# print('file created with same contents')
# myfile.close()

#create and read same content to the files


# myfile=open('test.txt','r')
# data=myfile.read()
# print(data)
# myfile.close()



# myfile=open('test.txt','r')
# data=myfile.read() #read(2) readlines() ---> list formate
# print(data)
# for i in data:
#     print(i,end='')
# myfile.close()



#note:--->>>w will overwrite the contents
        #-->>> a it will modify nad print the content with old data



# import  os
# #
# # os.rename('abc.txt','new.txt')
# os.remove('new.txt')


# create directories and subdirectories ....

# import  os
# os.mkdir('new')  #make new directory
# print(os.getcwd())  #get the current working directory
# os.chdir('new')
# print(os.getcwd())
# os.mkdir('dhhgf')


#TO remove directory ------->>>> lets remove abc directory

# os.rmdir('new/abc')

#TASK


import  os
# # os.mkdir('Employee')
# print(os.getcwd())
# os.chdir('Employee')
# print(os.getcwd())
# os.mkdir("Tester")
# os.mkdir("Developer")

# myfile=open("Employee//Tester//Manual.txt",'x')
# myfile1=open("Employee//Tester//Automation.txt",'x')
# myfile2=open("Developer//Python.txt",'x')
# myfile3=open("Developer//Java.txt",'x')