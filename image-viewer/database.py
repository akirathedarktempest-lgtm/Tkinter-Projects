import sqlite3
from tkinter import *
from pathlib import Path

connect=sqlite3.connect("image_address.db")
cursor=connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS data(
               address text)""")
root=Tk()
root.title("Image Add!")
myLab=Label(root,text="...")
myLab.pack()

def imagePath():
    e=str(entry.get())
    if "\\" in e:
        e=e.replace("\\","/")
    path=Path(e)
    cursor.execute("SELECT * FROM data")
    info=cursor.fetchall()
    for i in info:
        if e==i[0]:#i once added the twice, and it wasn't looking good so I am adding this, this will stop duplicate files
            entry.delete(0,END)
            return myLab.config(text="The file is already there! No duplicates are allowed!")
    if path:
        if ".jpg" in e or ".png" in e or ".jpeg" in e or ".gif" in e or ".webp" in e:
            cursor.execute("INSERT INTO data VALUES (?)",[e])
            connect.commit()
            entry.delete(0,END)
            myLab.config(text="Saved!")
        else:
            myLab.config(text="No such image file is there! The image extension can jpg, jpeg, png, webp, gif")
    else:
        myLab.config(text="There's no file like that :(")

entry=Entry(root)
entry.pack()

button=Button(root,text="Save!",command=imagePath)
button.pack()

root.mainloop()
#this is now an application to save the image adresses, a small app will open, and you will put the location, if it has similar extensions like jpg etc, and if it's present then it will save it to the database
#keep in mind, if you put something like, C:\Images\image don't forget to add the extension, if you find and see there's no extension, look at properties and the extension it mentions, that should be added like
#C:\Images\image.png this is an example and you can get the extension by looking at the properties of the file
