from tkinter import *

top = Tk()

L1 = Label(top, text="Hello, world!")

L1.grid(column= 0 , row= 1)

E1 = Entry(top, bd = 5)

E1.grid(column = 0, row = 2)



#mainloop is an initialization statement, a way to start. But for tkinter, this statement has to be the last line
top.mainloop()


