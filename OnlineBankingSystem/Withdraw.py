from tkinter import *

withdraw = Tk()
withdraw.title('Withdraw Section')
withdraw.geometry('640x320')

withdraw.columnconfigure(0,weight=1)
withdraw.columnconfigure(1,weight=1)
withdraw.columnconfigure(2,weight=3)
withdraw.columnconfigure(3,weight=3)
withdraw.columnconfigure(4,weight=3)
withdraw.rowconfigure(0,weight=3)
withdraw.rowconfigure(1,weight=3)
withdraw.rowconfigure(2,weight=1)
withdraw.rowconfigure(3,weight=3)
withdraw.rowconfigure(4,weight=3)

withdraw_savings= Button(withdraw, text='Savings').grid(row=0, column=1, columnspan='3', sticky='nsew')
withdraw_checking= Button(withdraw, text='Checkings').grid(row=1,column=1, columnspan=3,sticky='nsew')


withdraw.mainloop()
