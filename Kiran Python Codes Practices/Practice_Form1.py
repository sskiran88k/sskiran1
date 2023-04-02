from tkinter import *
from tkinter import ttk

window=Tk()

window.title("First Form Submission")
window.geometry("200x200")

Label(window, text="Name").grid(row=0,column=0)
Entry(window).grid(row=0,column=1)

Label(window, text="Phone Number").grid(row=1,column=0)
Entry(window).grid(row=1,column=1)

Label(window, text="Address").grid(row=2,column=0)
Entry(window).grid(row=2,column=1)

Label(window, text="Email ID").grid(row=3,column=0)
Entry(window).grid(row=3,column=1)

ttk.Button(window, text="Button").grid(row=4,column=0)


window.mainloop()
