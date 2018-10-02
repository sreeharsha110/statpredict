from tkinter import *
import dumbster
window = Tk()
window.title("Welcome to stat predicition")
window.geometry('540x540')
lbl = Label(window,text="Note : Updating the data takes some time Donot close the app\n",bg='red',fg="white").pack(anchor=NE)
upda=Label(window,text="")
def clicked():
    dumbster.workit()
    upda.configure(text="Updated the data")
    upda.pack(anchor=CENTER)
btn = Button(window, text="UPDATE", command=clicked)
btn.pack(anchor=NE)
a=["England","Australia","SouthAfrica","NewZealand","westindies","India","Pakistan","Srilanka"]
b=["ODI","TEST","T20"]
c=["Batsmen","Bowler"]

team=Label(window,text="Select  Two  Teams ",font=("Courier", 16)).pack(anchor=CENTER)

for i in range(0,8):
    ch=Label(window,text=a[i]).pack(anchor=CENTER)
tea=Label(window,text="Select  Format to be played ",font=("Courier", 16)).pack(anchor=CENTER)
for i in range(0,3):
    chc=Label(window,text=b[i]).pack(anchor=CENTER)
te=Label(window,text="Select  Format to be played ",font=("Courier", 16)).pack(anchor=CENTER)
for i in range(0,2):
    cdd=Label(window,text=c[i]).pack(anchor=CENTER)

window.mainloop()