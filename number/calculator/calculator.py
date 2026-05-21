from tkinter import *

root=Tk()
root.title("Yuzui~chan's Calculator!")
y=""

def ButtonConfig():#i am using global because I am afraid if the def can have that or not
    global Buttonadd
    global Buttonequal
    global Buttonminus
    global Buttonmultiply
    global Buttondivide
    global Button0#and there is reason we are bringing 0 here as well
    Buttonadd.config(state=NORMAL)
    Buttonminus.config(state=NORMAL)
    Buttonmultiply.config(state=NORMAL)
    Buttondivide.config(state=NORMAL)
    Buttonequal.config(state=NORMAL)
    Button0.config(state=NORMAL)
def ButtonDisable():
    global Buttonadd
    global Buttonequal
    global Buttonminus
    global Buttonmultiply
    global Buttondivide
    global Button0
    Buttonadd.config(state=DISABLED)
    Buttonminus.config(state=DISABLED)
    Buttonmultiply.config(state=DISABLED)
    Buttondivide.config(state=DISABLED)
    Buttonequal.config(state=DISABLED)
    Button0.config(state=DISABLED)
def Change():
    global y
    global myLabel
    myLabel.config(text=y)
def one():
    global y
    y+="1"
    Change()
    ButtonConfig()
def two():
    global y
    y+="2"
    Change()
    ButtonConfig()
def three():
    global y
    y+="3"
    Change()
    ButtonConfig()
def four():
    global y
    y+="4"
    Change()
    ButtonConfig()
def five():
    global y
    y+="5"
    Change()
    ButtonConfig()
def six():
    global y
    y+="6"
    Change()
    ButtonConfig()
def seven():
    global y
    y+="7"
    Change()
    ButtonConfig()
def eight():
    global y
    y+="8"
    Change()
    ButtonConfig()
def nine():
    global y
    y+="9"
    Change()
    ButtonConfig()
def zero():
    global y
    y+="0"
    Change()
    ButtonConfig()
    if y=="0":#and we are doing this so the the number wouldn't be like 01+2 or 01+02, it will cause an error by eval function
        ButtonDisable()
    else:
        pass
def add():
    global y
    y+="+"
    Change()
    ButtonDisable()
def equal():
    global y
    y=eval(y)
    #print(y)
    y=str(y)
    Change()#we are making it a string because it transforms into int after eval, and if we try adding int to str, it will cause an error...haha, smart akira
    if y=="0":
        ButtonDisable()
        y=""#here, I don't want a number start with 0, and do this again, 01+01 for example, the eval function will cause an error for that, best, 1+2
    else:
        pass
def minus():
    global y
    y+="-"
    Change()
    ButtonDisable()
def multiply():
    global y
    y+="*"
    Change()
    ButtonDisable()
def divide():
    global y
    y+="/"
    Change()
    ButtonDisable()

myLabel=Label(root,text=y)
Button0=Button(root,text="0",command=zero,height=2,width=2,state=DISABLED)
Button0.grid(row=0,column=1)
Button1=Button(root,text="1",command=one,height=2,width=2)
Button1.grid(row=0,column=2)
Button2=Button(root,text="2",command=two,height=2,width=2)
Button2.grid(row=0,column=3)
Button3=Button(root,text="3",command=three,height=2,width=2)
Button3.grid(row=1,column=1)
Button4=Button(root,text="4",command=four,height=2,width=2)
Button4.grid(row=1,column=2)
Button5=Button(root,text="5",command=five,height=2,width=2)
Button5.grid(row=1,column=3)
Button6=Button(root,text="6",command=six,height=2,width=2)
Button6.grid(row=2,column=1)
Button7=Button(root,text="7",command=seven,height=2,width=2)
Button7.grid(row=2,column=2)
Button8=Button(root,text="8",command=eight,height=2,width=2)
Button8.grid(row=2,column=3)
Button9=Button(root,text="9",command=nine,height=2,width=2)
Button9.grid(row=3,column=1)
Buttonadd=Button(root,text="+",command=add,state=DISABLED,height=2,width=2)#we are making it disable from the beginning, so that it wouldn't start like +1+2, no
Buttonadd.grid(row=3,column=2)#we need to only activate it when a number is there and the last value wasn't +,-,*,/
Buttonequal=Button(root,text="=",command=equal,state=DISABLED,height=2,width=2)
Buttonequal.grid(row=3,column=3)
Buttonminus=Button(root,text="-",command=minus,state=DISABLED,height=2,width=2)
Buttonminus.grid(row=4,column=1)
Buttonmultiply=Button(root,text="*",command=multiply,state=DISABLED,height=2,width=2)
Buttonmultiply.grid(row=4,column=2)
Buttondivide=Button(root,text="/",command=divide,state=DISABLED,height=2,width=2)
Buttondivide.grid(row=4,column=3)
myLabel.grid(row=5,column=4)#changed row and column as 
#the problem was at grid at every button, I had written Button0=Button().grid(), it should be Button0=Button()\nButton0.grid() and this is the correct way...huff
#it wasn't showing myLabel without that
root.mainloop()#and that's it, I am not a designer and don't know much about tkinter, I just learned about button, entry, label, grid, and pack and I made it by that only :)
