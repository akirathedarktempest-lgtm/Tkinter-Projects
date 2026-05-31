from tkinter import *
from PIL import ImageTk,Image
import sqlite3#we will use sqlite3 to stare the address of the images

root=Tk()
root.title("Image Viewer!")

connect=sqlite3.connect("image_address.db")
cursor=connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS data(
               address text)""")
cursor.execute("SELECT * FROM data")
images=cursor.fetchall()#we will use fetchall, all the image addresses

y=0#this will work as indexing, like the first image would be 0 and so on
myImg=ImageTk.PhotoImage(Image.open(images[y][0]))#in sqlite, we are doing double indexing, why? y is the indexing of the image and will give (image_address.png,), why "," because a tuple having one statement is treated like that
myLab=Label(root,image=myImg)
myLab.grid(row=0,column=1,columnspan=5)

def leftside():#this will make a button and keep on changing images here
    global y
    global myImg#use myImg, same name because it will be a trouble, the image wouldn't show if it's not a global variable
    y-=1#this moves the image a little bit behind
    if y<-(len(images)):#now why this? because indexing can have error, if you keep on moving back, 0 will appear by default, then, -1,-2 and so on, but the first one will come one day and if you try to move back once again, error
        y=len(images)-1
        myImg=ImageTk.PhotoImage(Image.open(images[y][0]))
        myLab.config(image=myImg)
    else:
        myImg=ImageTk.PhotoImage(Image.open(images[y][0]))
        myLab.config(image=myImg)
    
def rightside():#same as the leftside, but it was making it minus behind, but this will show of ahead, like, 0 index, 1, then 2
    global y
    global myImg
    y+=1
    if y==len(images):
        y=0
        myImg=ImageTk.PhotoImage(Image.open(images[y][0]))
        myLab.config(image=myImg)
    else:
        myImg=ImageTk.PhotoImage(Image.open(images[y][0]))
        myLab.config(image=myImg)

left_button=Button(root,text="<-",command=leftside)#buttons to move left or right
right_button=Button(root,text="->",command=rightside)
left_button.grid(row=1,column=0)#packing is important
right_button.grid(row=1,column=6)#this is now for better UX...i am not good at ui/ux, but i am trying to be better

root.mainloop()
