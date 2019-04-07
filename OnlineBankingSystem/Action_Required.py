from tkinter import *

def action_deposit():
    import Deposit
    Deposit.deposit()

def action_withdraw():
    import Withdraw
    Withdraw.withdraw()

def action_transactions():
    import Transaction
    Transaction.transaction()

def action():

    action_required = Tk()
    action_required.title('Choose an option to proceed')
    action_required.geometry('640x320')

    action_required.columnconfigure(0, weight=1)
    action_required.columnconfigure(1, weight=1)
    action_required.columnconfigure(2, weight=1)
    action_required.columnconfigure(3, weight=3)
    action_required.columnconfigure(4, weight=3)
    action_required.rowconfigure(0, weight=5)
    action_required.rowconfigure(1, weight=5)
    action_required.rowconfigure(2, weight=5)
    action_required.rowconfigure(3, weight=3)
    action_required.rowconfigure(4, weight=3)

    button_deposit = Button(action_required, text='Deposit',command=lambda: action_deposit()).grid(row=0, column=1, columnspan=3, stick='nsew')
    button_withdraw = Button(action_required, text='Withdraw',command=lambda: action_withdraw()).grid(row=1, column=1, columnspan=3, sticky='nsew')
    button_transaction = Button(action_required, text='Transactions',command=lambda: action_transactions()).grid(row=2, column=1, columnspan=3, sticky='nsew')
    action_required.mainloop()


