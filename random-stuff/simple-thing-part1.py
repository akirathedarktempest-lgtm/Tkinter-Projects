from tkinter import *

a="\uc218\uc544"

root=Tk()

myLabel=Label(root,text=f"Who is \"{a}\"?")
myLabel.pack()

def b1():
    myLabel.config(text="Yes, it's Sua")

def b2():
    myLabel.config(text="Yup! It's Sua!")

def b3():
    myLabel.config(text="Yes, right! It's Sua!")

def b4():
    myLabel.config(text="Aw, you know Sua? Yes, it's Sua!")

button1=Button(root,text="Sua?",command=b1)
button2=Button(root,text="It's Sua",command=b2)
button3=Button(root,text="Sua",command=b3)
button4=Button(root,text="Sua!!!",command=b4)

button1.pack()
button2.pack()
button3.pack()
button4.pack()

root.mainloop()

#...misuse of tkinter, haha...I was just making this for fun, and it just came in mind to make it so I made it! Yay...and yes, I am a big fan of Sua, I actually am
