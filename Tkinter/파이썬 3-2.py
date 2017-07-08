#writedata.py
from tkinter import *
root = Tk()

var1=IntVar()
var2=IntVar()
var3=IntVar()

def red ():
    lbl['fg']='red'

def blue ():
    lbl['fg']='blue'

def green ():
    lbl['fg']='green'



lbl=Label(root,text='Choose a text color',font=(16))
lbl.grid(row=0,column=0)


rb1=Radiobutton(root,text="Red",command=red,value=1)
rb1.grid(row=1,column=0)


rb2=Radiobutton(root,text="Blue",command=blue,value=2)
rb2.grid(row=2,column=0)

rb3=Radiobutton(root,text="Green",command=green,value=3)
rb3.grid(row=3,column=0)


root.mainloop()

