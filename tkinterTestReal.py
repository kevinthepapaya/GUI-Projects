from tkinter import * #simple way to import only what we need, low memory
import random

top = Tk()
groceryList = []
unique_list = []
myList = []
myRolls = []
rollTimes = 0
dieType = 0

#SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4'

def results():
    #result = E1.get()
    print(groceryList)
    L5W3 = Label (top, text = "Here is your list:")
    L5W3.grid(column = 3, row = 1)
    L4W3 =Label(top, text = "{}".format(groceryList))
    L4W3.grid(column = 3, row = 2)
    
 

def printList():
    L6W3 = Label (top, text = "Here is your list:")
    L6W3.grid(column = 3, row = 1)
    L7W3 =Label(top, text = "{}".format(unique_list))
    L7W3.grid(column = 3, row = 2)
#find way to wrap text
    

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
    B1Main = Button(text ="  Week 1  ", bg= "SkyBlue1", command = week1)
    B1Main.grid(column = 0, row =1)
    B2Main = Button(text ="  Week 2  ", bg= "SkyBlue3", command = week2)
    B2Main.grid(column =0, row =2)
    B3Main = Button(text ="  Week 3  ", bg= "SkyBlue4", command = week3)
    B3Main.grid(column =0, row =3)


def week1():
    clearWindow()
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
    B1 = Button(text = "    Print List    ", bg = "light slate blue", command = results )
    B1.grid(column = 0, row = 3)

    B2 = Button(text = " + ", bg="lime green", command = addToList)
    B2.grid(column = 1, row = 2)

    B3 = Button(text = "Export List", bg= "slate blue", command = exportList)
    B3.grid(column = 2, row = 3)
#make it so that user knows where to find exported list, pop up window?
    Bclear = Button( text = "Main Menu", bg = "blue", command = mainMenu)
    Bclear.grid(column = 3, row =3)

    #mainloop is an initilization statement, a way to start. But for tkinter, this statement has to be the last line

def week2():
    def rollDice():
        dieType = E1W2.get()
        rollTimes = E2W2.get()
        
        #clear window AFTER pulling Entry data
        clearWindow()
        
        #calculate dice rolls
        for x in range(0, int(rollTimes)):
            myRolls.append(random.randint(1, int(dieType)))
            
        #display dice rolls and present an exit button
        L4W2 = Label(top, text = "Here are your rolls!")
        L4W2.grid(column = 0, row = 1)

        #modify this grid so the list prints in a good way
        L5W2 =Label(top, text = "{}".format(myRolls))
        L5W2.grid(column = 0, row = 2)
        
        B2W2 =Button(top, text = "Main Menu", bg = "blue", font = ("Helvetica"), command = mainMenu)
        B2W2.grid(column = 0, row = 3)
    
    clearWindow()
    L1W2 = Label(top, text= "Dice Roller Program")
    L1W2.grid(column =0 , row =0 )
    
    L2W2 = Label(top, text= "How many sides?")
    L2W2.grid(column =1 , row =3 )
    
    L3W2 = Label (text = "How many rolls?")
    L3W2.grid(column = 1, row = 5)
    
    E1W2 = Entry(top,bd=5)
    E1W2.grid(column = 1, row =4 )
    
    E2W2 = Entry(top,bd=5)
    E2W2.grid(column = 1, row =6 )
    
    B1W2 = Button(top, text = "Roll dice!!", bg = 'green', command = rollDice)
    B1W2.grid(column = 0, row = 7)

    B1clear = Button( text = "Main Menu", bg = "blue", command = mainMenu)
    B1clear.grid(column = 3, row =2)

def week3():

    def addABunch():
        numToAdd = E1W3.get()
        numRange = E2W3.get()

        for x in range (0, int(numToAdd)):
            myList.append(random.randint(0, int(numRange)))
        for x in myList:
            if x not in unique_list:
                unique_list.append(x)
        unique_list.sort()
        E1W3.delete(0, END)
        E2W3.delete(0, END)
        
    clearWindow()
    L1W3 = Label (top, text = "We're gonna add a bunch of numbers.")
    L1W3.grid(column =1 , row =0 )

    L2W3 = Label (top, text = "How many integers do you want to add?  ")
    L2W3.grid(column =1 , row =1 )
        
    E1W3 = Entry(top, bd = 5)
    E1W3.grid(column =1 , row =2 )

    L3W3 = Label (top, text = "How high would you like these numbers to go?  ")
    L3W3.grid(column =1 , row =4 )
        
    E2W3 = Entry(top, bd = 5)
    E2W3.grid(column =1 , row =5 )

    B2W3 = Button (top, text = "  +  ", bg = "lime green", command = addABunch)
    B2W3.grid(column =2 , row =2 )
        
    B1W3 = Button (top, text = "Print List", bg = "light slate blue", command = printList)
    B1W3.grid(column =2 , row =3 )
    
    B2clear = Button( text = "Main Menu", bg = "blue", command = mainMenu)
    B2clear.grid(column = 1, row =6)
#fix print, fix formatting, make so entry clears when + is pressed   

    
if __name__=="__main__":
    mainMenu()
    top.mainloop()


