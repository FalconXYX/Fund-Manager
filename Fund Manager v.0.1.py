#--------------------
#Import stuff
#--------------------
import sys
import random
import tkinter as tk
import time
from tkinter import *
#print('Welcome to Fund Manager lets set you up with a usser name and Password')
#--------------------
#Login stuff
#--------------------
L1_user = "momma"
L1_Pass = "1111"
L2_user = "parth"
L2_Pass = "6666"
L3_user = "shreya"
L3_Pass = "3333"
L4_user = "daddy"
L4_Pass = "2222"
L5_user = "guest"
L5_Pass = "0000"



class App(tk.Tk):

    def __init__(win):
        window_x = 1280
        window_y = 720
        global user_entry
        global password_entry
        tk.Tk.__init__(win)
        win.title("Fund Manager")
        win.geometry("1280x720") #Width x Height of window
        Title = tk.Label(win, text="Fund Manager", fg="Black",font=("Courier", 44))
        user_entry = tk.Entry(win)
        password_entry = tk.Entry(win)
        loginbutton = tk.Button(win, text="Login", command=win.Login)
        labeluser = tk.Label(win, text="Username:",fg="Black",font=("Courier", 12))
        labelpassword = tk.Label(win, text="Password:",fg="Black",font=("Courier", 12))
        Title.place(x=425, y=0)
        labeluser.place(x=500, y=250)
        labelpassword.place(x=500, y=280)
        loginbutton.place(x=575, y=350)
        user_entry.place(x=625, y=250)
        password_entry.place(x=625, y=280)
        Label(win, text="").grid(row=5, column=1)
        display = Label(win, text="") # we need this label as a variable for live display
        display.grid(row=5, column=1)


    def Login(win):
        global user_entry
        global password_entry
        display = Label(win, text="") #  need this Label as a variable!
        display.grid(row=5, column=1)
        user_entry.get()
        password_entry.get()
        Password = password_entry.get()
        User = user_entry.get()

        User = User.lower()
        if User == L1_user:
            if Password == L1_Pass:
                display.configure(text="Welcome Sal")
            else:
                display.configure(text="Invalid Credentails", fg="red")
        elif User == L2_user:
            if Password == L2_Pass:
                display.configure(text="Welcome FalconXYX")
            else:
                display.configure(text="Invalid Credentails", fg="red")
        elif User == L3_user:
            if Password == L3_Pass:
                display.configure(text="Welcome Sheyu")
            else:
                display.configure(text="Invalid Credentails", fg="red")
        elif User == L4_user:
            if Password == L4_Pass:
                display.configure(text="Welcome Bob")
            else:
                display.configure(text="Invalid Credentails", fg="red")
        elif User == L5_user:
            if Password == L5_Pass:
                print("Hello",L5_user)
                display.configure(text="Welcome Guest")
            else:
                display.configure(text="Invalid Credentails", fg="red")
        else:
            display.configure(text="Invalid Credentails", fg="red")



w = App()
w.mainloop()
