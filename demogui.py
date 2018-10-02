from tkinter import *
import dumbster
window = Tk()
window.title("Welcome to stat predicition")
window.geometry('540x540')
lbl = Label(window,text="Note : Updating the data takes some time Donot close the app\n",bg='',f)
lbl.grid(column=5, row=6)
upda=Label(window,text="")
def clicked():
    dumbster.workit()
    upda.configure(text="Updated the data")
    upda.grid(column=6, row=2)
btn = Button(window, text="UPDATE", command=clicked)
btn.grid(column=5, row=5,sticky=SE)

window.mainloop()