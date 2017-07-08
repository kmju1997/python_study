class Point :
    
    x = 0
    y = 0

    
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def setx(self,x):
        self.x=x

    def sety(self,y):
        self.y=y

    def get(self):
        t=(self.x,self.y)
        print(t)

    def move(self,dx,dy):
        self.x+=dx
        self.y+=dy

point=Point(1,2)
point.get()
point.setx(3)
point.sety(4)
point.get()
point.move(1,1)
point.get()
