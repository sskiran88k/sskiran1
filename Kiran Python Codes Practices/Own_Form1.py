from tkinter import *

window=Tk()

window.title("First Python Form")
window.geometry("200x200")

##def close():
##    window.destroy()
    
Button(window,text="Submit",command=window.destroy).grid()


window.mainloop()

