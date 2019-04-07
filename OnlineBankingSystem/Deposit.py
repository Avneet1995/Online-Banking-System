from tkinter import *

def deposit():
    deposit = Tk()
    deposit.title('Deposit Section')
    deposit.geometry('640x320')

    deposit.columnconfigure(0, weight=1)
    deposit.columnconfigure(1, weight=1)
    deposit.columnconfigure(2, weight=3)
    deposit.columnconfigure(3, weight=3)
    deposit.columnconfigure(4, weight=3)
    deposit.rowconfigure(0, weight=3)
    deposit.rowconfigure(1, weight=3)
    deposit.rowconfigure(2, weight=1)
    deposit.rowconfigure(3, weight=3)
    deposit.rowconfigure(4, weight=3)

    deposit_savings = Button(deposit, text='Savings').grid(row=0, column=1, columnspan='3', sticky='nsew')
    deposit_checking = Button(deposit, text='Checkings').grid(row=1, column=1, columnspan=3, sticky='nsew')

    deposit.mainloop()
