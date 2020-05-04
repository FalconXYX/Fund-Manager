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
L1_user = "mommy"
L1_Pass = "1111"
L2_user = "parth"
L2_Pass = "6666"
L3_user = "shreya"
L3_Pass = "3333"
L4_user = "daddy"
L4_Pass = "2222"
L5_user = "guest"
L5_Pass = "0000"
id = "none"
Bank_Balance = [1000,1000,1000,1000,1000]
Debt = [3245,999,7543,8647]
#Net_Worth = Bank_Balance[id] + Assets[id] - Debt[id]
Assets = [66121,968128,1575,9847]
class App(tk.Tk):

    def __init__(self):
        selfdow_x = 1280
        selfdow_y = 720
        global user_entry
        global password_entry
        tk.Tk.__init__(self)
        self.title("Fund Manager")
        self.geometry("1280x720") #Width x Height of selfdow
        Title = tk.Label(self, text="Fund Manager", fg="Black",font=("Courier", 44))
        user_entry = tk.Entry(self)
        password_entry = tk.Entry(self)
        loginbutton = tk.Button(self, text="Login", command=self.Login)
        labeluser = tk.Label(self, text="Username:",fg="Black",font=("Courier", 12))
        labelpassword = tk.Label(self, text="Password:",fg="Black",font=("Courier", 12))

        Title.place(x=425, y=0)
        labeluser.place(x=500, y=250)
        labelpassword.place(x=500, y=280)
        loginbutton.place(x=590, y=325)
        user_entry.place(x=625, y=250)
        password_entry.place(x=625, y=280)
    def clear(self):
        time.sleep(0.5)
        list = self.place_slaves()
        for l in list:
            l.destroy()

    def mainmenue(self):
        self.clear()
        what = tk.Label(self, text="What would you like to do?", fg="Black",font=("Courier", 14))
        what.place(x=450, y=150)
        Title = tk.Label(self, text="Fund Manager", fg="Black",font=("Courier", 44))
        Title.place(x=425, y=0)
        atm = tk.Button(self, text="Deposit or Withdtraw Money", command=self.autoteller)
        atm.place(x=250, y=280)
        finace = tk.Button(self, text="Check Your Finances", command=self.finances)
        finace.place(x=550, y=280)
        bill = tk.Button(self, text="Check Your Finances", command=self.bills)
        bill.place(x=850, y=280)
    def autoteller(self):
        self.clear()
    def finances(self):
        self.clear()
    def bills(self):
        self.clear()

#parth




    def welcome():
        display.configure(text="Welcome")

    def Login(self):
        global user_entry
        global password_entry

        display = Label(self, text="") #  need this Label as a variable!
        display.place(x=580, y=390)
        user_entry.get()
        password_entry.get()
        Password = password_entry.get()
        User = user_entry.get()

        User = User.lower()
        if User == L1_user:
            if Password == L1_Pass:
                display.configure(text="Welcome")
                id = 0
                self.mainmenue()
            else:
                display.configure(text="Invalid Credentails", fg="red")
        elif User == L2_user:
            if Password == L2_Pass:
                display.configure(text="Welcome")
                id = 1
                self.mainmenue()
            else:
                display.configure(text="Invalid Credentails", fg="red")
        elif User == L3_user:
            if Password == L3_Pass:
                display.configure(text="Welcome")
                id = 2
                self.mainmenue()
            else:
                display.configure(text="Invalid Credentails", fg="red")
        elif User == L4_user:
            if Password == L4_Pass:
                display.configure(text="Welcome")
                id = 3
                self.mainmenue()
            else:
                display.configure(text="Invalid Credentails", fg="red")
        elif User == L5_user:
            if Password == L5_Pass:
                print("Hello",L5_user)
                display.configure(text="Welcome")
                id = 4
                self.mainmenue()
            else:
                display.configure(text="Invalid Credentails", fg="red")
        else:
            display.configure(text="Invalid Credentails", fg="red")



w = App()
w.mainloop()
