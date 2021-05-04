from tkinter import * #simple way to import only what we need, low memory

top = Tk()
groceryList = []


def results():
    result = E1.get()
    print(groceryList)
   

def addToList():
    newItem = E1.get()
    groceryList.append(newItem)
    
#This is a Label widget
L1 = Label(top, text="Grocery List")
L1.grid(column= 0 , row= 1)

#This is a Entry widget
E1 = Entry(top, bd = 5)
E1.grid(column = 0, row = 2)

#This is a button widget
B1 = Button(text = "    Print List    ", bg = "green", command = results )
B1.grid(column = 0, row = 3)

B2 = Button(text = " Add To List ", bg="pink", command = addToList)
B2.grid(column = 1, row = 2)

#mainloop is an initialization statement, a way to start. But for tkinter, this statement has to be the last line
top.mainloop()


