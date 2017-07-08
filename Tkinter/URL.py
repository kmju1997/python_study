from tkinter import *
from urllib.request import urlopen
from PIL import Image, ImageTk
import io

hehe="\<title\>\<\!\[CDATA\[(.+)\]\]\>"
URL_TopNews="http://rss.donga.com/total.xml"
urlopener=urlopen(URL_TopNews).read().decode('utf-8')
text=(re.findall(hehe,urlopener))
print(text) 
