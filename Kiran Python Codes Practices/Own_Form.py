from tkinter import *
from tkinter.ttk import Combobox


window=Tk()


window.title("My First Form")
window.geometry("300x200")

Label(window,text="Enter a Value: ").grid(row=0,column=0)
Entry(window).grid(row=0,column=1)

Label(window,text="Enter b Value: ").grid(row=1,column=0)
Entry(window).grid(row=1,column=1)

Radiobutton(window, text="Male").grid(row=2,column=0)
Radiobutton(window, text="Male").grid(row=2,column=1)

Checkbutton(window, text="Male").grid(row=3,column=0)
Checkbutton(window, text="Male").grid(row=3,column=1)

data="21KD1A0467","21KD1A0468","21KD1A0469","21KD1A0470"

Combobox(window,values=data).grid(row=4,column=0)

Button(window,text="Sum").grid(row=5,column=0)
t3=Entry(window).grid(row=5,column=1)





