from tkinter import *

root = Tk()

root.title("Clicker")
root.config(bg="gray")

total = 0

def Up():
    global total
    total+=1
    Number.config(text=total)
    updateBackground()

def Down():
    global total
    total-=1
    Number.config(text=total)
    updateBackground()

def yellowBackground(self):
    root.config(bg="yellow")

def normalBackground(self):
    if total == 0:
        root.config(bg="gray")
    elif total >= 1:
        root.config(bg="green")
    elif total <= -1:
        root.config(bg="red")

def updateBackground():
    if total == 0:
        root.config(bg="gray")
    elif total >= 1:
        root.config(bg="green")
    elif total <= -1:
        root.config(bg="red")

buttonUp = Button(root, command=Up)
buttonUp.config(text="Up", bd=0, bg="white", width=25)
buttonUp.pack(padx=15, pady=20, side=TOP)

Number = Label(root, text=total, bg="white", width=25)
Number.bind('<Enter>',yellowBackground)
Number.bind('<Leave>',normalBackground)
Number.pack(padx=15, pady=.5, side=TOP)

buttonDown = Button(root, command=Down)
buttonDown.config(text="Down", bd=0, bg="white", width=25)
buttonDown.pack(padx=15, pady=20, side=TOP)

root.mainloop()