#By this app, you can give a link address of an image, and download it in your device

from tkinter import *
import requests

root=Tk()
root.title("Image Downloader!")
root.iconbitmap("animec.ico")

wrongLab=Label(root,text="")

label=Label(root,text="Download a link image!")
myLab=Label(root,text="Image Link Address")
e1=Entry(root)
myLab2=Label(root,text="Name the file (please also add which extension you want, jpg,jpeg,png,webp or gif)")
e2=Entry(root)

def download():
    global wrongLab
    link=str(e1.get())
    image=str(e2.get())
    if link == "":
        return wrongLab.config(text="Please give a image link address")
    if image == "":
        return wrongLab.config(text="Please give a name to the file, and also extension")
    response=requests.get(link)
    if image.endswith(".jpg") or image.endswith(".jpeg") or image.endswith(".png") or image.endswith(".webp") or image.endswith(".gif"):
        if response.status_code==200:
            with open(image,"wb") as f:
                f.write(response.content)
            e1.delete(0,END)
            e2.delete(0,END)
            wrongLab.config(text="Downloaded!")
        else:
            return wrongLab.config("The link doesn't exist :(")
    else:
        return wrongLab.config(text="Please add extension below in Name, jpg, jpeg, png, webp, and gif only works.\nIf the image has any animation, use webp or gif\nExample: image.webp")

button=Button(root,text="Download!",command=download)

wrongLab.pack()
label.pack()
myLab.pack()
e1.pack()
myLab2.pack()
e2.pack()
button.pack()

root.mainloop()
