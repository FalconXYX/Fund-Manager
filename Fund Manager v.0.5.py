#--------------------
#Import stuff
#--------------------
import sys
import random
import tkinter as tk
import time
from tkinter import *
import os
from pathlib import Path
#print('Welcome to Fund Manager lets set you up with a usser name and Password')
#--------------------
#Login stuff
#--------------------
data = "Data"
users = "Users"
#Net_Worth = Bank_Balance[id] + Assets[id] - Debt[id]
Assets = [66121,968128,1575,9847]
class App(tk.Tk):

    def __init__(self):
        selfdow_x = 1280
        selfdow_y = 720
        global user_entry
        global password_entry
        global labelpassword
        global loginbutton
        global user_entry
        global password_entry
        global NewUserButton
        global Title
        global message
        global CreateUserButton
        global BackButton
        tk.Tk.__init__(self)
        self.title("Fund Manager")
        self.geometry("1280x720") #Width x Height of selfdow
        Title = tk.Label(self, text="Fund Manager", fg="Black",font=("Courier", 44))
        message = tk.Label(self, text="", fg="Black",font=("Courier", 12))
        user_entry = tk.Entry(self)
        password_entry = tk.Entry(self)
        loginbutton = tk.Button(self, text="Login", command=self.Login)
        NewUserButton = tk.Button(self, text="New User", command=self.New)
        labeluser = tk.Label(self, text="Username:",fg="Black",font=("Courier", 12))
        labelpassword = tk.Label(self, text="Password:",fg="Black",font=("Courier", 12))
        CreateUserButton = tk.Button(self, text="New User", command=self.NewUser)
        BackButton = tk.Button(self, text="Back", command=self.__init__)

        Title.place(x=425, y=0)
        labeluser.place(x=500, y=250)
        labelpassword.place(x=500, y=280)
        loginbutton.place(x=590, y=325)
        NewUserButton.place(x=590, y=625)
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
    def New(self):

        loginbutton.place_forget()
        Title.configure(text="New User")
        Title.place(x=525, y=0)
        subtitle = tk.Label(self, text="Enter a New Password and New Username", fg="Black",font=("Courier", 18))
        subtitle.place(x=365, y=55)
        NewUserButton.place_forget()

        CreateUserButton.place(x=590, y=325)
    def NewUser(self):
        NewPassword = password_entry.get()
        NewUser = user_entry.get()
        UsersFile = open(Path.cwd() / data / users / 'Users.txt')
        homeFolder = Path.cwd()
        out = homeFolder / data / users / 'Users.txt'
        UserContent = UsersFile.read()
        UsernamesThatExist = []
        UsernamesThatExist = UserContent.splitlines()
        userexists = False
        complete = True

        l = len(UsernamesThatExist)
        i = 0

        while(i < l):
            if (NewUser == UsernamesThatExist[i]):
                userexists = True
                break
            i += 1

        length = len(NewPassword)
        if (length < 8):
            message.place(x=400, y=355)
            message.configure(text="That Password is to short enter one that is at least 8 characters")
            complete = False
        length = len(NewUser)
        if (length < 5):
            message.place(x=400, y=355)
            message.configure(text="That Username is to short enter one that is at least 5 characters")
            complete = False
        if (userexists == True):
            message.place(x=500, y=355)
            message.configure(text="That Username already exists")
            complete = False

        if(complete == True):
            message.place(x=555, y=355)
            message.configure(text="Your Acount has been created")
            UsersFile = open(Path.cwd() / data / users / 'Users.txt', 'w')
            UsersFile.write(NewUser + '\n')
            out = homeFolder / data / users / NewUser
            os.makedirs(out)
            newfile = out / 'password.txt'
            passwordfile = open(newfile, "w")
            passwordfile.write(NewPassword)
            BackButton.place(x=590, y=625)




    def Login(self):
        global user_entry
        global password_entry

        display = Label(self, text="") #  need this Label as a variable!
        display.place(x=580, y=390)
        user_entry.get()
        password_entry.get()
        Password = password_entry.get()
        User = user_entry.get()
        Password = int(Password)



w = App()
w.mainloop()
