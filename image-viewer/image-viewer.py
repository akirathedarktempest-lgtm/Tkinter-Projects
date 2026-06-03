from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root=Tk()
root.title("Image Viewer!")

connect=sqlite3.connect("image_address.db")
cursor=connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS data(
               address text)""")
cursor.execute("SELECT * FROM data")
images=cursor.fetchall()

status=Label(root,text=f"Image 1 of {len(images)}")#this will be like the number of image, like if you view image 2, it will show at below "Image 2 of 5" if total are 5

y=0
myImg=ImageTk.PhotoImage(Image.open(images[y][0]))
myLab=Label(root,image=myImg)
myLab.grid(row=0,column=1,columnspan=5)

def leftside():
    global y
    global myImg
    global status
    y-=1
    if y<-(len(images)):
        y=len(images)-1
        myImg=ImageTk.PhotoImage(Image.open(images[y][0]))
        myLab.config(image=myImg)
        rowid=row_id(images[y][0])
        status.config(text=f"Image {rowid} of {len(images)}")
    else:
        myImg=ImageTk.PhotoImage(Image.open(images[y][0]))
        myLab.config(image=myImg)
        rowid=row_id(images[y][0])
        status.config(text=f"Image {rowid} of {len(images)}")
    
def rightside():
    global y
    global myImg
    global status
    y+=1
    if y==len(images):
        y=0
        myImg=ImageTk.PhotoImage(Image.open(images[y][0]))#you all may ask, I am using the function there but not here, why, because that will start showing in negative and wrong index, but it wouldn't happen in positive index
        myLab.config(image=myImg)#if you click on image 5 and move on, it will turn 1 again, because y will turn 0 and we are doing y+1 here
        status.config(text=f"Image {y+1} of {len(images)}")#in case of negative indexing, it works like this, Image 1, 0+1=y+1, if you click back, it will show 0, and then more negative, so just to keep it simple and as much I could use my logic, I have done and used rowid
    else:
        myImg=ImageTk.PhotoImage(Image.open(images[y][0]))
        myLab.config(image=myImg)
        status.config(text=f"Image {y+1} of {len(images)}")

def row_id(img_adr):
    cursor.execute(f"SELECT rowid FROM data WHERE address=\"{img_adr}\"")
    number=cursor.fetchone()
    return number[0]

left_button=Button(root,text="<-",command=leftside)
right_button=Button(root,text="->",command=rightside)
left_button.grid(row=1,column=0)
right_button.grid(row=1,column=6)

status.grid()

root.mainloop()
