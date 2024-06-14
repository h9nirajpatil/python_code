
from tkinter import *
win = Tk()
win.geometry('350x350')
win.title("Calculator")
win.resizable(False,False)

val=" "#empty variable
data=StringVar()#create object of string var class

def btnclick(number):
    global val
    val=val+str(number)
    data.set(val)

def btnClear():
    global  val
    val=" "
    data.set(" ")

def btnEquals():
    global  val
    val=str(eval(val))
    data.set(val)

e1 = Entry(win,width=20,bd=20,bg='lightpink',textvariable=data,font=('arial',20),justify='right')
e1.grid(row=0, columnspan=4)


# display=Entry(win,textvariable=data,bd=10,bg='p',justify='right',font=('arial',10))
# display.grid(row=0,columnspan=4)

b9=Button(win,text='7',bd=10,font=('arial',12,'bold'),width=6,height=2 ,command=lambda:btnclick(7))
b9.grid(row=1,column=0)

b8=Button(win,text='8',bd=10,font=('arial',12,'bold'),width=6,height=2,command=lambda:btnclick(8))
b8.grid(row=1,column=1)

b7=Button(win,text='9',bd=10,font=('arial',12,'bold'),width=6,height=2,command=lambda:btnclick(9))
b7.grid(row=1,column=2)

b77=Button(win,text='+',bd=10,font=('arial',12,'bold'),width=6,height=2,command=lambda:btnclick('+'))
b77.grid(row=1,column=3)

b6=Button(win,text='4',bd=10,font=('arial',12,'bold'),width=6,height=2,command=lambda:btnclick(4))
b6.grid(row=2,column=0)

b5=Button(win,text='5',bd=10,font=('arial',12,'bold'),width=6,height=2,command=lambda:btnclick(5))
b5.grid(row=2,column=1)

b4=Button(win,text='6',bd=10,font=('arial',12,'bold'),width=6,height=2,command=lambda:btnclick(6))
b4.grid(row=2,column=2)

b44=Button(win,text='*',bd=10,font=('arial',12,'bold'),width=6,height=2,command=lambda:btnclick('*'))
b44.grid(row=2,column=3)

b3=Button(win,text='1',bd=10,font=('arial',12,'bold'),width=6,height=2,command=lambda:btnclick(1))
b3.grid(row=3,column=0)

b2=Button(win,text='2',bd=10,font=('arial',12,'bold'),width=6,height=2,command=lambda:btnclick(2))
b2.grid(row=3,column=1)

b1=Button(win,text='3',bd=10,font=('arial',12,'bold'),width=6,height=2,command=lambda:btnclick(3))
b1.grid(row=3,column=2)

b11=Button(win,text='-',bd=10,font=('arial',12,'bold'),width=6,height=2,command=lambda:btnclick('-'))
b11.grid(row=3,column=3)

b12=Button(win,text='CE',bd=10,font=('arial',12,'bold'),width=6,height=2,command=btnClear)
b12.grid(row=4,column=0)

b13=Button(win,text='0',bd=10,font=('arial',12,'bold'),width=6,height=2,command=lambda:btnclick(0))
b13.grid(row=4,column=1)

b14=Button(win,text='/',bd=10,font=('arial',12,'bold'),width=6,height=2,command=lambda:btnclick('/'))
b14.grid(row=4,column=2)

b15=Button(win,text='=',bd=10,font=('arial',12,'bold'),width=6,height=2,command=btnEquals)
b15.grid(row=4,column=3)

mainloop()
