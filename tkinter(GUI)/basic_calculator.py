
from tkinter import *
win = Tk()
win.geometry('400x400')

obj=StringVar()#class which display the content in the Label,textbox etc

def add():
    n1=int(e1.get())#get the values from textbox and convert to integer
    n2=int(e2.get())
    sum=n1+n2
    obj.set(sum)#set the result in Label

def sub():
    n1 = int(e1.get())  # get the values from textbox and convert to integer
    n2 = int(e2.get())
    sub = n1 - n2
    obj.set(sub)  # set the result in Label

def mul():
    n1 = int(e1.get())  # get the values from textbox and convert to integer
    n2 = int(e2.get())
    mul = n1 * n2
    obj.set(mul)  # set the result in Label

def div():
    n1 = int(e1.get())  # get the values from textbox and convert to integer
    n2 = int(e2.get())
    sum = n1 / n2
    obj.set(sum)  # set the result in Label

def clear():
    e1.delete(0,'end')
    e2.delete(0,'end')


lb1=Label(win, text='Number1',bd=5)
lb1.place(x=30,y=40)

lb2=Label(win, text='Number2',bd=5)
lb2.place(x=30,y=70)

e1 = Entry(win,width=10,bg='lightpink')
e1.place(x=100,y=40)

e2 = Entry(win,width=10,bg='lightpink')
e2.place(x=100,y=70)

b1=Button(win,text='ADD',bd=10,command=add)
b1.place(x=90,y=100)

b2=Button(win,text='SUB',bd=10,command=sub)
b2.place(x=140,y=100)

b3=Button(win,text='MUL',bd=10,command=mul)
b3.place(x=200,y=100)

b4=Button(win,text='DIV',bd=10,command=div)
b4.place(x=260,y=100)

clear=Button(win,text='Clear',bd=10,command=clear)
clear.place(x=320,y=100)

result=Label(win,text='Result')
result.place(x=80,y=150)

lb4=Label(win,bg='cyan',width=5,textvariable=obj,disabled=True)
lb4.place(x=120,y=150)

mainloop()