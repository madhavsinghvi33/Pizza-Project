from tkinter import *
import tkinter.messagebox
import sqlite3

top=Tk()
top.geometry('600x500')
FullName=StringVar()
Email=StringVar()
var=IntVar()
c=StringVar()
b=StringVar()
var1=IntVar()
var2=IntVar()
i=1

def database():
    name1=FullName.get()
    email=Email.get()
    Veg/Non-Veg==var.get()
    pizza=c.get()
    toppings=b.get()
    conn=sqlite3.connect('Form.db')
    with conn:
        cursor=conn.cursor()
    #cursor.execute('CREATE TABLE IF NOT EXISTS Student (Full Name TEXT,Email TEXT, Veg/Non-Veg TEXT,Country TEXT,Programming TEXT)')
    cursor.execute('INSERT INTO Student (Full Name,Email,Veg/Non-Veg,Pizza Types,Programming) VALUES(?,?,?,?,?)',(name1,email,Veg/Non-Veg,pizza,prog))
    conn.commit()
    tkinter.messagebox.showinfo("Login","Successfully logged in")

L1=Label(top,text="Full Name")
L1.place(x=80,y=130)
E1=Entry(top,textvar=FullName)
E1.place(x=240,y=130)


L2=Label(top,text="Email")
L2.place(x=80,y=180)
E2=Entry(top,textvar=Email)
E2.place(x=240,y=180)

L3=Label(top,text="Veg/Non-Veg")
L3.place(x=70,y=230)
Radiobutton(top,text="Vegetarian",variable=var,value=1).place(x=235,y=230)
Radiobutton(top,text="Non-Vegetarian",variable=var,value=2).place(x=335,y=230)

L4=Label(top,text="Pizza Types")
L4.place(x=70,y=280)
List1=['Margherita','Cheese-burst','Formaggi','Farm-House','Paneer','Pasta-Pizza']
droplist=OptionMenu(top,c,*List1)
c.set('Select your pizza type')
droplist.place(x=240,y=280)


L5=Label(top,text="Extra Toppings")
L5.place(x=70,y=330)
List2=['Olives','Tomatoes','Jalapenos','Mushrooms','Onions','Extra Cheese']
droplist=OptionMenu(top,b,*List2)
b.set('Select your toppings, if any')
droplist.place(x=240,y=330)

L6=Label(top,text="Thank you")
L6.place(x=200,y=400)

B1=tkinter.Button(top,text="Enter",command=database)
B1.pack(side=BOTTOM)

top.mainloop()