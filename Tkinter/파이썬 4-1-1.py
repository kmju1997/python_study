from tkinter import *
from urllib.request import urlopen
from PIL import Image, ImageTk
import re
import io

root=Tk()

URL="http://i558.photobucket.com/albums/ss24/bissniss/icon-news.png"
urlopener=urlopen(URL).read()
f=io.BytesIO(urlopener)
image_opener=Image.open(f)
photo=ImageTk.PhotoImage(image_opener)


lbl1=Label(root,text="Julie's News Feed",font=('대한',45))
lbl1.grid(row=0,column=0, columnspan=4)

lbl2=Label(root,text="All the contents are extracted from\nwww.news.naver.com",font=('대한',10))
lbl2.grid(row=1,column=0, columnspan=4)


lf=LabelFrame(root,text="News", font=('대한',20))
lf.grid(row=2,column=0,columnspan=4)

image=Label(lf,image=photo)
image.photo=photo
image.grid(row=2,column=0, columnspan=4)

lbl3=Label(root,text="\nSelect the news from the bottom\n",font=('대한',15))
lbl3.grid(row=3,column=0, columnspan=4)

btn1=Button(root,text="Top news",font=('대한'))
btn1.grid(row=4,column=0)

btn2=Button(root,text="Entertainment news",font=('대한'))
btn2.grid(row=4,column=1)

btn3=Button(root,text="World news",font=('대한'))
btn3.grid(row=4,column=2)

btn4=Button(root,text="Business news",font=('대한'))
btn4.grid(row=4,column=3)


root.mainloop()
