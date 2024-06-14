from tkinter import *
from tkinter import  messagebox
win=Tk()
win.geometry('500x500')
win.title("ButtonClick")

def click():
    # messagebox.showinfo('show','Hello!')
    # messagebox.showerror('error','click on wrong button!')
    # messagebox.showwarning('warning','not allowed!')
    # messagebox.askokcancel('error','its error')
    # messagebox.askquestion('which one','ask question')
    messagebox.showinfo('show','Hello!')

b1=Button(text='CLick Me',width=10,bg='yellow',fg='red',bd=12,command=click)
b1.place(x=50,y=50)

win.mainloop()
