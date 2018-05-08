from tkinter import *
from tkinter import ttk
import math
import sys

myApp = Tk()
myApp.title(" Program ")                         
myApp.geometry("1000x1200")

tasktabs=ttk.Notebook(myApp)

NewWorkLab=Label(myApp,text="Name: ")
NewWorkLab.grid(row=0,column=2, sticky="W", padx=5,pady=5)

NewWorkEntry=Entry(myApp)
NewWorkEntry.grid(row=0,column=3,sticky="W", padx=5,pady=5)

def AddNewWork():

    TabName=NewWorkEntry.get()

    NewWorkTab=ttk.Frame(tasktabs)
    tasktabs.add(NewWorkTab,text=NewWorkEntry.get())

    NewTree= ttk.Treeview(TabName,height=40)
    NewTree['show'] = 'headings'

    NewTree["columns"]=("1","2","3","4","5","6")

    NewTree.column("1", width=20)
    NewTree.column("2", width=320)
    NewTree.column("3", width=40)
    NewTree.column("4", width=80)
    NewTree.column("5", width=80)
    NewTree.column("6", width=80)

    NewTree.heading("1", text="ID")
    NewTree.heading("2", text="Activities")
    NewTree.heading("3", text="Unit")
    NewTree.heading("4", text="Quantity")
    NewTree.heading("5", text="Unit Cost")
    NewTree.heading("6", text="Total Cost")

    NewTree.grid(row=2,column=0,pady=10,padx=0)

AddWorkButton=Button(myApp,text=' Add ', command=AddNewWork)
AddWorkButton.grid(row=0,column=4, sticky="W", padx=5, pady=5)


tasktabs.grid(row=1,column=0,columnspan=4,padx=5)   

myApp.mainloop()