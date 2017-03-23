import sys
import MySQLdb
import pymsgbox
import Tkinter as tkinter
#import urllib
import tkMessageBox

top = tkinter.Tk()
var = tkinter.StringVar()
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

L1 = tkinter.Label(top, text="User Name")
L1.pack( side = tkinter.LEFT)

E1 = tkinter.Entry(top, textvariable=var)

E1.pack(side = tkinter.RIGHT)
var.trace("w", callback)
B = tkinter.Button(top,text ="Hello",command=helloCallBack)
B.pack()
top.mainloop()
