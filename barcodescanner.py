import sys
import MySQLdb
import pymsgbox
import Tkinter as tk
from PIL import ImageTk, Image
#import urllib
import tkMessageBox
app_root = tk.Tk()
top = tk.Tk()
var = tk.StringVar()
def helloCallBack():
    tkMessageBox.showinfo( "Hello Python", "Hello World")


def callback(*args):
    if len(var.get()) > 12:
        inputStr = ""
        inputStr += var.get()
        query = "SELECT * FROM products where barcode='"+inputStr+"' and status=0"
        conn = MySQLdb.connect( host="localhost",user="root",passwd="user123",db="pos",port=3306)
        cur = conn.cursor()
        try:
            cur.execute(query)
            if len(cur.fetchall()) == 1:
                for row in cur.fetchall():
                    status=row[2]
                    print status
                    #tkMessageBox.showinfo( "Not Valid", "Card is not valid!")
            else :
                tkMessageBox.showinfo( "Not Valid", "Card is not valid!")
            status = 0
            var.set("")
        finally:
            conn.close()

L1 = tk.Label(top, text="User Name")
L1.pack( side = tk.LEFT)

E1 = tk.Entry(top, textvariable=var)

E1.pack(side = tk.RIGHT)
var.trace("w", callback)
#B = tk.Button(top,text ="Hello",command=helloCallBack)
#B.pack()
img = ImageTk.PhotoImage(Image.open("app.png"))
imglabel = tk.Label(app_root, image=img).grid(row=1, column=1)
top.mainloop()
