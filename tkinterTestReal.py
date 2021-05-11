from tkinter import * #simple way to import only what we need, low memory

top = Tk()
groceryList = []


def results():
    result = E1.get()
    print(groceryList)
   



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
    B2Main = Button(text ="  Week 2  ", bg= "blue", command = week2)
    B2Main.grid(colum =0, row =2)
    B3Main = Button(text ="  Week 3  ", bg= "blue",)
    B3Main.grid(colum =0, row =3)

""""
export doesn't work and window doesn't show up.
""""
def week1():
    
    def addToList():
        newItem = E1.get()
        groceryList.append(newItem)
        E1.delete(0, END)
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

    Bclear = Button( text = "Main Menu", bg = "blue", command = mainMenu)
    Bclear.grid(column = 3, row =3)

    mainloop is an initialization statement, a way to start. But for tkinter, this statement has to be the last line

def week2():
    clearWindow()
    L1W2 = Label(top, text= "Dice Roller Program")
    L1W2.grid(column =3 , row =0 )
    
    L2W2 = Label(top, text= "How many sides?")
    L2W2.grid(column =1 , row =3 )
    
    L3W2 = Label (text = "How many rolls?")
    L3W2.grid(column = 5, row = 3)
    
    E1W2 = Entry(top,bd=5)
    E1W2.grid(column = 1, row =4 )
    
    E2W2 = Entry(top,bd=5)
    E2W2.grid(column = 5, row =4 )
    
    B1W2 = Button(top, text = "Roll dice!!", bg = 'green', command = rolldice)
    B1W2.grid(column = , row = )

    #to add: roll function and exit button

if __name__=="__main__":
    mainMenue()
    top.mainloop()


