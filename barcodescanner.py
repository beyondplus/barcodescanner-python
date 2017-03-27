import sys
import MySQLdb
#import pymsgbox
import tkinter as tk
from PIL import Image, ImageTk
#import urllib
import tkinter.messagebox

window = tk.Tk()
window.title("Awasome POS Ticket System")
window.geometry("300x300")
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0,background='white',foreground='white',activebackground='#004c99', activeforeground='white')
filemenu.add_command(label="Exit", command=window.destroy)
menubar.add_cascade(label="File", menu=filemenu)

var = tk.StringVar()
def helloCallBack():
    tk.messagebox.showinfo( "Hello Python", "Hello World")


def callback(*args):
    if len(var.get()) == 8:
        if(len(var.get()) > 7):
            inputStr = var.get()
            query = "SELECT * FROM products where barcode='"+inputStr+"' and status=0"
            conn = MySQLdb.connect( host="localhost",user="root",passwd="user123",db="pos",port=3306)
            cur = conn.cursor()
            try:
                status = 1
                # print inputStr
                cur.execute(query)
                if len(cur.fetchall()) == 1:
                    for row in cur:
                        status =row[2]
                else:
                    status = 1
                if status == 1:
                    tk.messagebox.showinfo( "Not Valid", "Card is not valid!")
            finally:
                conn.close()
                var.set("")
        else:
            var.set("")
            tk.messagebox.showinfo( "Not Valid", "Card is not valid!")

title = tk.Label(window, text="Welcome to POS Ticket System")
title.pack()

L1 = tk.Label(window, text="Mouse cursor here!")
L1.pack()

E1 = tk.Entry(window, textvariable=var)

E1.pack()
var.trace("w", callback)
#B = tk.Button(window,text ="Hello",command=helloCallBack)
#B.pack()
img = ImageTk.PhotoImage(Image.open("app.png"))
imglabel = tk.Label(window, image=img)
imglabel.pack()

window.config(bg='#2A2C2B', menu=menubar)
window.configure(background='white')
window.mainloop()