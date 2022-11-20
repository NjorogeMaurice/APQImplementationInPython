

from tkinter import W, Entry, Label
from tkinter.messagebox import showerror
from tkinter.simpledialog import Dialog



class UpdateKey(Dialog):
    
    newKey = -1
    loc = -1

    def body(self, master):
        self.title("Update Priority Key")
        Label(master, text='Patient Index:').grid(row=0, sticky=W)
        self.keyEntry= Entry(master, width = 16)
        Label(master, text='New Key:').grid(row=2, sticky=W)
        self.valEntry= Entry(master, width = 16)

        self.keyEntry.grid(row=0, column=1, sticky=W)
        self.valEntry.grid(row=2, column=1, sticky=W)

    def apply(self):
        UpdateKey.loc = self.keyEntry.get()
        UpdateKey.newKey = self.valEntry.get()
    