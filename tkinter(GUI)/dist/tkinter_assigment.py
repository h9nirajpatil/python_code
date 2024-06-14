from tkinter import *
from tkinter import  messagebox

win=Tk()
win.geometry('400x400')
win.title("REGISTER FROM")
win.resizable(False,False)

def Click():
    messagebox.showinfo('Details','Your From is Submitted Succesfully!')

register_from=Label(win,text='Register From',font=('arial',20),bg='red')
register_from.pack(side=TOP)

first_name=Label(win,text='Name',font=('arial',16))
first_name.place(x=40,y=100)

name_textfield=Entry(win,bd=5,font=('arial',12),bg='lightpink')
name_textfield.place(x=120,y=105)

Gender=Label(win,text='Gender',font=('arial',16))
Gender.place(x=35,y=160)

var=IntVar()

male_radio=Radiobutton(win,text='Male',value=1,variable=var,font=('arial',16))
male_radio.place(x=120,y=160)

female_radio=Radiobutton(win,text='Female',value=2,variable=var,font=('arial',16))
female_radio.place(x=200,y=160)

Hobbies=Label(win,text='Hobbies',font=('arial',16))
Hobbies.place(x=35,y=220)

sing=Checkbutton(win,text='Sing',font=('arial',16))
sing.place(x=130,y=220)

dance=Checkbutton(win,text='Dance',font=('arial',16))
dance.place(x=220,y=220)

country=Label(win,text='Country',font=('arial',16))
country.place(x=30,y=280)

mylist=('India','USA','Germany','Canada')
obj=StringVar()
optionM=OptionMenu(win,obj,*mylist)
obj.set('Select Country')
optionM.place(x=110,y=280)

submit=Button(win,text='SUBMIT',font=('arial',16),bg='lightblue',bd=5,command=Click)
submit.pack(side=BOTTOM)

win.mainloop()