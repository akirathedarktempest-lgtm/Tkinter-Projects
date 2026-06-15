from tkinter import *
import sqlite3

connect=sqlite3.connect("log-in-page.db")
cursor=connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS login(
               email_add text,
               password text,
               userid text,
               username text)""")

root=Tk()
wrongL=Label(root,text="")
myLabel=Label(root,text="User ID or email:")
e1=Entry(root)
myLabel2=Label(root,text="Password")
e2=Entry(root)

def login():
    global e1
    global e2
    global wrongL
    e_u=str(e1.get())
    pw=str(e2.get())
    if e_u == "":
        return wrongL.config(text="Please put your user id or email address please")
    if pw == "":
        return wrongL.config(text="Please give your password")
    cursor.execute("SELECT * FROM login")
    info=cursor.fetchall()
    for i in info:
        if e_u==i[0]:
            if pw==i[1]:
                wrongL.config(text="You have made a login!")
                return
            elif pw!=i[1]:
                wrongL.config(text="Wrong password!")
                return
            else:
                print("Something's wrong there at line 40!")
        elif e_u==i[2]:
            if pw==i[1]:
                wrongL.config(text="You have made a login!")
                return
            elif pw!=i[1]:
                wrongL.config(text="Wrong password!")
                return
            else:
                print("Something's wrong there at line 48!")
        else:
            pass
    return wrongL.config(text="There's no such userid or email, you wouldn't have sign up here :(")


button=Button(root,text="Log-in!",command=login)
wrongL.pack()
myLabel.pack()
e1.pack()
myLabel2.pack()
e2.pack()
button.pack()
root.mainloop()

#I don't know how to decorate Tkinter applications :( unfortunately, I couldn't become a designer of UI/UX, but tell me if there are some videos explaining to decorate apps
#and this thing, I have made it as much I could think of, I guess the passwords are made even more strong at databases then your actual password, and like in Discord, there are token (if you would have saw making bots, there are tokens to use as the bot you want and many thing)
#I don't know much about the behind the scene of the application and all that, but I will try to learn and know, maybe, but yes, that's all for today :)
