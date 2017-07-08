from tkinter import *
root = Tk()

def plus():
    total="Result : "+ str(int(entry1.get())+int(entry2.get()))
    lbl3.config(text=total)
    
def minus():
    total="Result : "+ str(int(entry1.get())-int(entry2.get()))
    lbl3.config(text=total)
    


lbl1=Label(root,text='더하기 or 빼기!',font=('궁서',13))
lbl1.grid(row=0,columnspan=3)
           
lbl2=Label(root,text='?')
lbl2.grid(row=1,column=1)

entry1=Entry(root,bd=3,width=7)
entry1.grid(row=1, column=0)

entry2=Entry(root,bd=3,width=7)
entry2.grid(row=1,column=2)

btn1=Button(root,text='더하기',command=plus)
btn1.grid(row=2,column=0,columnspan=2)

btn2=Button(root,text='빼기',command=minus)
btn2.grid(row=2,column=1,columnspan=2)


lbl3=Label(root)
lbl3.grid(row=3,column=0,columnspan=3)



root.mainloop()

