from tkinter import *
import sqlite3
import tkinter as tk
import Action_Required

mainWindow=Tk()
mainWindow.title("Login Screen")
mainWindow.geometry('640x320')

db=sqlite3.connect("login.sqlite3")
db.execute("create table if not exists loginscreen (username text primary key NOT NULL, password integer) ")
# db.execute("insert into loginscreen values ('avneet',123)")
cursor = db.cursor()

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=3)
mainWindow.columnconfigure(3, weight=3)
mainWindow.columnconfigure(4, weight=3)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)

def func2(user,checkPIN):
    cursor = db.execute("select username, password from loginscreen where (username=?)", (str(user.get()),))
    row = cursor.fetchone()

    if row:
        user, pass2 = row
        if (pass2 == str(checkPIN.get())):
            print("Login Successful!")
            Action_Required.action()
            mainWindow.quit
        else:
            print("Incorrect password or Username.")

label_account = Label(mainWindow,text='Account number:')
label_account.grid(row=0, column=0, columnspan=2, sticky='ne')

label_PIN=Label(mainWindow, text='Enter PIN:')
label_PIN.grid(row=1, column=0, columnspan=2, sticky='ne')

PIN=StringVar()
Account=StringVar()
entry_account = Entry(mainWindow,textvariable=Account).grid(row=0, column=1, columnspan=2, sticky='ne')
entry_PIN = Entry(mainWindow,textvariable=PIN).grid(row=1, column=1, columnspan=2, sticky='ne')

button_login = tk.Button(mainWindow, text='LOGIN', command=lambda: func2(Account,PIN)). \
            grid(row=1, column=0, columnspan='2', sticky='se')

button_cancel = Button(mainWindow, text='CANCEL', command=quit). \
                    grid(row=1, column=1, columnspan='2', sticky='se')

db.commit()
mainWindow.mainloop()
