from tkinter import *

transaction = Tk()
transaction.title('Transactions')
transaction.geometry('640x320')

transaction.columnconfigure(0,weight=1)
transaction.columnconfigure(1,weight=1)
transaction.columnconfigure(2,weight=3)
transaction.columnconfigure(3,weight=3)
transaction.columnconfigure(4,weight=3)
transaction.rowconfigure(0,weight=3)
transaction.rowconfigure(1,weight=3)
transaction.rowconfigure(2,weight=1)
transaction.rowconfigure(3,weight=3)
transaction.rowconfigure(4,weight=3)

label_transaction=Label(transaction,text='Transactions').grid(row=0,column=1, columnspan=3, sticky='nsew')

transaction.mainloop()
