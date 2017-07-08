#writedata.py
from tkinter import *
root = Tk()


def submission ():
    f=open("C:/Users/강민주/Desktop/대학/동아리/포리프/파이썬 스터디/submission.txt",'w')
    data="성명: %s 회사: %s 특징: %s" %(txt1.get(), txt2.get(), txt3.get())
    f.write(data)
    f.close()

lbl=Label(root,text="고객정보입력")
lbl.grid(row=0,column=0,columnspan=2)

lbl=Label(root,text="성명")
lbl.grid(row=1,column=0)

lbl=Label(root,text="회사")
lbl.grid(row=2,column=0)

lbl=Label(root,text="특징")
lbl.grid(row=3,column=0)

txt1=Entry(root)
txt1.grid(row=1,column=1)

txt2=Entry(root)
txt2.grid(row=2,column=1)

txt3=Entry(root)
txt3.grid(row=3,column=1)

btn=Button(root,text="제출하기",command=submission)
btn.grid(row=4,column=0,columnspan=2)

root.mainloop()

