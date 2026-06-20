#this is the sign up the page, you can add valid email, and it will be added in the database ^^
#and I have also made a userid one...in old Discord it was present, something like akira#0101, but # is removed...but what does it matter? I will add it anyways...discord lover...(although i joined discord on 2025 and it was gone earlier than that)

from tkinter import *
import validators
import sqlite3
import random

def userid(user,li:list):
    while True:
        use=f"{user}#{random.randint(100,999)}"
        if user in li:
            continue
        else:
            return use

connect=sqlite3.connect("Account-DB.db")
cursor=connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS accdata(
               email text,
               password text,
               userid text,
               name text)""")

root=Tk()
root.title('Sign up!')

wrongLabel=Label(root,text="")

label=Label(root,text="Sign up!")
label1=Label(root,text="Email")
e1=Entry(root)
label2=Label(root,text="Name")
e2=Entry(root)
label3=Label(root,text="Password")
e3=Entry(root)

def signup():
    email=str(e1.get())
    name=str(e2.get())
    password=str(e3.get())
    if email=="":
        return wrongLabel.config(text="Please give your email")
    if password=="":
        return wrongLabel.config(text="Please make a password")
    if "@" not in email or "." not in email:
        return wrongLabel.config("The email is not valid!")
    if validators.email(email):
        if name=="":
            em=email.split("@")
            em=em[0]
        else:
            em=name
        cursor.execute("SELECT * FROM accdata")
        info=cursor.fetchall()
        l=[]
        for i in info:
            if i[0]==email:
                return wrongLabel.config(text="The email has already sign up! You can log in instead!")
            else:
                pass
            l.append(i[2])
        e=userid(em,l)
        cursor.execute("INSERT INTO accdata VALUES (?,?,?,?)",[email,password,e,em])
        connect.commit()
        cursor.execute(f"SELECT * FROM accdata")
        data=cursor.fetchall()
        for d in data:
            if d[0]==email:
                e1.delete(0,END)
                e2.delete(0,END)
                e3.delete(0,END)
                return wrongLabel.config(text=f"Email: {d[0]}\nPassword:{d[1]}\nUser ID:{d[2]}\nName:{d[3]}")
            else:
                pass
        wrongLabel.config(text="Something went wrong!")
    elif validators.email(email) is False:
        wrongLabel.config("The email is not valid!")#this is to handle the error, but unfortunately, the error is still causing there, I don't know why, it is coming here only but causing an error, I will see for it later for now
    else:#but for conext, the error is happening when you give an invalid email address, I even added "@" or "." not in email, but it still causes the error, I don't know why
        wrongLabel.config("The email is not valid!")

button=Button(root,text="Sign Up",command=signup)
wrongLabel.pack()
label.pack()
label1.pack()
e1.pack()
label2.pack()
e2.pack()
label3.pack()
e3.pack()
button.pack()

root.mainloop()
