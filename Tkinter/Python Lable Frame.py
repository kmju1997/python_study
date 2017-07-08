from tkinter import *


class Window:

    def __init__(self):
        self.root = Tk()

        self.sensorTable = Frame(master=self.root)
        self.sensorNameColumn = LabelFrame(self.sensorTable, text="Name", padx=5, pady=5).grid(row = 0, column = 0)
        self.sensorValueColumn = LabelFrame(self.sensorTable, text="Value", padx=5, pady=5).grid(row = 0, column = 1)

        w = Label(master=self.sensorNameColumn, text="Hello")
        w.pack()

        w2 = Label(master=self.sensorValueColumn, text="World")
        w2.pack()

        #self.sensorTable.pack() # commenting this out should mean that the two entries are not seen on the window but they are for some reason

        quit_button = Button(self.root, text="Quit", command=self.quit)
        quit_button.pack(side=BOTTOM)

    def begin(self):
        mainloop()

    def quit(self):
        self.root.quit()     # stops mainloop
        self.root.destroy()


if __name__=="__main__":
    Window().begin()
