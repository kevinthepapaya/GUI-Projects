from tkinter import * #simple way to import only what we need, low memory

top = Tk()
groceryList = []


def results():
    result = E1.get()
    print(groceryList)
   

def addToList():
    newItem = E1.get()
    groceryList.append(newItem)
    E1.delete(0, END)

def exportList():
    with open('test.txt', 'w') as f:
        for item in groceryList:
            f.write("%s\n" % item)

def clearWindow():
    for widgets in top.winfo_children():
        widgets.destroy()

def mainMenu():
    clearWindow()
    LMain = Label(top, text = "Block 5 GUI Projects")
    LMain.grid(column = 0, row = 0)
    B1Main = Button(text ="  Week 1  ", bg= "blue", command = week1)
    B1Main.grid(colum = 0, row =1)
    B2Main = Button(text ="  Week 2  ", bg= "blue")
    B2Main.grid(colum =0, row =2)
    B3Main = Button(text ="  Week 3  ", bg= "blue")
    B3Main.grid(colum =0, row =3)

""""
export doesn't work and window doesn't show up.
""""
def week1():
    clearWindow()    
    #This is a Label widget
    L1 = Label(top, text="Grocery List")
    L1.grid(column= 0 , row= 1)

    #This is a Entry widget
    E1 = Entry(top, bd = 5)
    E1.grid(column = 0, row = 2)

    #This is a button widget
    B1 = Button(text = "    Print List    ", bg = "green", command = results )
    B1.grid(column = 0, row = 3)

    B2 = Button(text = " + ", bg="pink", command = addToList)
    B2.grid(column = 1, row = 2)

    B3 = Button(text = "Export List", bg= "red", command = exportList)
    B3.grid(column = 2, row = 3)

    #Bclear = Button( text = "Clear Window", bg = "blue", command = clearWindow)
    #Bclear.grid(column = 3, row =3)

    #mainloop is an initialization statement, a way to start. But for tkinter, this statement has to be the last line
if __name__=="__main__":
    mainMenue()
    top.mainloop()


