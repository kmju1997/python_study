from tkinter import *
from urllib.request import urlopen
from PIL import Image, ImageTk
import io


root= Tk()

photo_re='\<img\ssrc=\'(.+.jpg)\''

URL_ENews="http://rss.donga.com/culture.xml"
urlopener=urlopen(URL_ENews).read().decode('utf-8')
photo=(re.findall(photo_re,urlopener))
print(photo[0])

photoopen=urlopen(photo[0]).read()
p=io.BytesIO(photoopen)
photo_opener=Image.open(p)
photo=ImageTk.PhotoImage(photo_opener)


image=Label(root,image=photo)
image.photo=photo
image.grid(row=0,column=0 )

root.mainloop()
