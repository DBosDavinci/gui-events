from tkinter import *
from random import randrange
from tkinter.messagebox import askyesno

root = Tk()
root.configure(bg="gray")
root.geometry("400x200")
challengeLabel = ""
challenge = ""
score=0
keys = ["w","a","s","d","space","Button","Double-Button","Triple-Button"]

def startFunc():
    global score,time
    score=0
    time=21
    start.destroy()
    countdown()
    createChallenge()

def countdown():
    global time,score
    time-=1
    if time >= 1:
        label.config(text=f'Time remaining: {time}')
        root.after(1000, countdown)
    else:
        answer = askyesno(message=f"Congratulations you have {score} points, do you want to play again?")
        if answer:
            startFunc()
        else:
            root.destroy()

def createChallenge():
    global challenge, challengeLabel
    challenge = keys[randrange(0,8)]
    challengeLabel = Label(root,text=f"Press: {challenge}")
    root.bind(f"<{challenge}>",deleteLabel)
    challengeLabel.place(x=randrange(0,290),y=randrange(20,180))

def deleteLabel(self):
    global score,challengeLabel,challenge
    challengeLabel.destroy()
    root.unbind(f"<{challenge}>")
    if keys.index(challenge) in range(0,5):
        score+=1
        label1.configure(text=f'{score} points')
    elif keys.index(challenge) in range(5,8):
        score+=2
        label1.configure(text=f'{score} points')
    createChallenge()


start = Button(text="press here to start",bd=0,command=startFunc)
start.place(relx = 0.5, rely = 0.5, anchor=CENTER)

top = Frame(root)
top.pack(side=TOP,fill=X)

label = Label(text="Time remaining: 20",bg="black",fg="white",width=30,height=1)
label.pack(in_=top,side=LEFT)
label1 = Label(text="0 points",bg="black",fg="white",width=30,height=1)
label1.pack(in_=top,side=LEFT)

root.mainloop()