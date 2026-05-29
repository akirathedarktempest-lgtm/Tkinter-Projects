import sqlite3

connect=sqlite3.connect("image_address.db")
cursor=connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS data(
               address text)""")

ads=input()

cursor.execute("INSERT INTO data VALUES (?)",[ads])
connect.commit()
connect.close()
#we will insert the addresses of images available in your device, and if the images are in same folder where the files are, then just write the name of the image, like, image.png or any extension the image file has
