from tkinter import *
from urllib.request import urlopen
from PIL import Image, ImageTk
import io

title_re='\<title\>\<\!\[CDATA\[(.+)\]\]\>'
description_re1='hspace=\'10\'\>(.+)\.'
description_re2='\<description\>\<\!\[CDATA\[(.+)\.'
link_re='\<link\>\<\!\[CDATA\[(.+)\]\]\>\</link\>'
pubdata_re='\<pubDate\>(.+)\</pubDate\>'
photo_re='\<img\ssrc=\'(.+.jpg)\''


def LatestNews() :
    URL_LatestNews="http://rss.donga.com/total.xml"
    urlopener=urlopen(URL_LatestNews).read().decode('utf-8')
    toptitle=(re.findall(title_re,urlopener))
    datetext=(re.findall(pubdata_re,urlopener))
    descripttext1=(re.findall(description_re1,urlopener))
    descripttext2=(re.findall(description_re2,urlopener))
    linktext=(re.findall(link_re,urlopener))
    photo=(re.findall(photo_re,urlopener))
    date.config(text=datetext[0])
    title.config(text=toptitle[0])

    photoopen=urlopen(photo[0]).read()
    p=io.BytesIO(photoopen)
    photo_opener=Image.open(p)

    new_width=300
    new_height=300
    photo_opener=photo_opener.resize((new_width,new_height),Image.ANTIALIAS)
    
    newphoto=ImageTk.PhotoImage(photo_opener)
    image.config(image=newphoto)
    image.image= newphoto
    

    if descripttext2[0]==descripttext1[0]:       
        description.config(text=descripttext2[0]+'.')
    else :
        description.config(text=descripttext1[0]+'.')
    link.config(text=linktext[0]+"\n")
    
def Entertainment():
    
    URL_ENews="http://rss.donga.com/culture.xml"
    urlopener=urlopen(URL_ENews).read().decode('utf-8')
    toptitle=(re.findall(title_re,urlopener))
    datetext=(re.findall(pubdata_re,urlopener))
    descripttext1=(re.findall(description_re1,urlopener))
    descripttext2=(re.findall(description_re2,urlopener))
    linktext=(re.findall(link_re,urlopener))
    
    photo=(re.findall(photo_re,urlopener))
    photoopen=urlopen(photo[0]).read()
    p=io.BytesIO(photoopen)
    photo_opener=Image.open(p)

    new_width=300
    new_height=300
    photo_opener=photo_opener.resize((new_width,new_height),Image.ANTIALIAS)
    
    newphoto=ImageTk.PhotoImage(photo_opener)
    image.config(image=newphoto)
    image.image= newphoto
    
    date.config(text=datetext[0])
    title.config(text=toptitle[0])
    
    if descripttext2[0]==descripttext1[0]:       
        description.config(text='\n'+descripttext2[0]+'.')
    else :
        description.config(text='\n'+descripttext1[0]+'.')
        
    link.config(text=linktext[0]+"\n")
    
def World():
    URL_WNews="http://rss.donga.com/international.xml"
    urlopener=urlopen(URL_WNews).read().decode('utf-8')
    toptitle=(re.findall(title_re,urlopener))
    datetext=(re.findall(pubdata_re,urlopener))
    descripttext1=(re.findall(description_re1,urlopener))
    descripttext2=(re.findall(description_re2,urlopener))
    linktext=(re.findall(link_re,urlopener))
    photo=(re.findall(photo_re,urlopener))
    date.config(text=datetext[0])
    title.config(text=toptitle[0])

    photoopen=urlopen(photo[0]).read()
    p=io.BytesIO(photoopen)
    photo_opener=Image.open(p)

    new_width=300
    new_height=300
    photo_opener=photo_opener.resize((new_width,new_height),Image.ANTIALIAS)
    
    newphoto=ImageTk.PhotoImage(photo_opener)
    image.config(image=newphoto)
    image.image= newphoto
    
    
    if descripttext2[0]==descripttext1[0]:       
        description.config(text=descripttext2[0]+'.')
    else :
        description.config(text=descripttext1[0]+'.')
    link.config(text=linktext[0]+"\n")
    
def Economy():
    URL_BNews="http://rss.donga.com/economy.xml"
    urlopener=urlopen(URL_BNews).read().decode('utf-8')
    toptitle=(re.findall(title_re,urlopener))
    datetext=(re.findall(pubdata_re,urlopener))
    descripttext1=(re.findall(description_re1,urlopener))
    descripttext2=(re.findall(description_re2,urlopener))
    linktext=(re.findall(link_re,urlopener))
    photo=(re.findall(photo_re,urlopener))
    date.config(text=datetext[0])
    title.config(text=toptitle[0])

    photoopen=urlopen(photo[0]).read()
    p=io.BytesIO(photoopen)
    photo_opener=Image.open(p)

    new_width=300
    new_height=300
    photo_opener=photo_opener.resize((new_width,new_height),Image.ANTIALIAS)
    
    newphoto=ImageTk.PhotoImage(photo_opener)
    image.config(image=newphoto)
    image.image= newphoto
    
    if descripttext2[0]==descripttext1[0]:       
        description.config(text=descripttext2[0]+'.')
    else :
        description.config(text=descripttext1[0]+'.')
    link.config(text=linktext[0]+"\n")

root= Tk()

URL_Background="http://i558.photobucket.com/albums/ss24/bissniss/icon-news.png"
urlopener=urlopen(URL_Background).read()
f=io.BytesIO(urlopener)
image_opener=Image.open(f)

new_width=400
new_height=300
image_opener=image_opener.resize((new_width,new_height),Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image_opener)


lbl1=Label(root,text="Julie's News Feed",font=('대한',45))
lbl1.grid(row=0,column=0, columnspan=4)

lbl2=Label(root,text="All the contents are extracted from\nwww.donga.com\n",font=('대한',10))
lbl2.grid(row=1,column=0, columnspan=4)

date=Label(root, font=('대한',10))
date.grid(row=2,column=0, columnspan=4)

title=Label(root,font=('대한',20),wraplength=600)
title.grid(row=3,column=0, columnspan=4)

image=Label(root,image=photo)
image.photo=photo
image.grid(row=4,column=0, columnspan=4)

description=Label(root,text="\nSelect the news from the bottom\n",font=('대한',13), wraplength=700)
description.grid(row=5,column=0, columnspan=4)

link=Label(root,font=('대한',10),wraplength=500)
link.grid(row=6,column=0,columnspan=4)

btn1=Button(root,text="Latest news",font=('대한'), command = LatestNews)
btn1.grid(row=7,column=0)

btn2=Button(root,text="Entertainment news",font=('대한'),command= Entertainment)
btn2.grid(row=7,column=1)

btn3=Button(root,text="World news",font=('대한'), command=World)
btn3.grid(row=7,column=2)

btn4=Button(root,text="Economy news",font=('대한'), command=Economy)
btn4.grid(row=7,column=3)


root.mainloop()

