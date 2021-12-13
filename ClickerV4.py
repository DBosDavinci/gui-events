from tkinter import *

root = Tk()

root.title("Clicker")
root.config(bg="gray")

total = 0
recent = ['first item']

def Up(self):
    global total
    total+=1
    Number.config(text=total)
    updateBackground()
    recent.pop(0)
    recent.append("up")

def Down(self):
    global total
    total-=1
    Number.config(text=total)
    updateBackground()
    recent.pop(0)
    recent.append("down")

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

def doubleClick(self):
    global total
    if recent[0] == "up":
        total = total*3
    elif recent[0] == "down":
        total = total/3
    Number.config(text=total)

buttonUp = Button(root, command=Up)
buttonUp.config(text="Up", bd=0, bg="white", width=25)
buttonUp.pack(padx=15, pady=20, side=TOP)

Number = Label(root, text=total, bg="white", width=25)
Number.bind('<Enter>',yellowBackground)
Number.bind('<Leave>',normalBackground)
Number.bind('<Double-Button>',doubleClick)
Number.pack(padx=15, pady=.5, side=TOP)

buttonDown = Button(root, command=Down)
buttonDown.config(text="Down", bd=0, bg="white", width=25)
buttonDown.pack(padx=15, pady=20, side=TOP)

root.bind('<+>',Up)
root.bind('<Up>',Up)
root.bind('<minus>',Down)
root.bind('<Down>',Down)
root.bind('<space>',doubleClick)

root.mainloop()