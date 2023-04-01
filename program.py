from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Combo Box")    
root.geometry("450x350+600+500")


Label(text="Address",font=20).grid(row=0,column=0)
choice =StringVar(value= "Select you city")
combo = ttk.Combobox(textvariable=choice)
combo["values"]=("London","Manchester","Leeds","Newcastle")
combo.grid(row=0,column=1)

def selectCity():
    Label(text="You have selected = "+choice.get(),font=20).grid(row=2,column=1)
    


btn=Button(text="Sent",command=selectCity)
btn.grid(row=1,column=1,)
root.mainloop()