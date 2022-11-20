

from tkinter import W, Entry, Label
from tkinter.messagebox import showerror
from tkinter.simpledialog import Dialog



class UpdateValue(Dialog):
    
    newVal = ""
    loc = -1

    def body(self, master):
        self.title("Update Entry Value")
        Label(master, text='Patient index:').grid(row=0, sticky=W)
        self.keyEntry= Entry(master, width = 16)
        Label(master, text='New Value:').grid(row=2, sticky=W)
        self.valEntry= Entry(master, width = 16)

        self.keyEntry.grid(row=0, column=1, sticky=W)
        self.valEntry.grid(row=2, column=1, sticky=W)

    def apply(self):
        UpdateValue.loc = self.keyEntry.get()
        UpdateValue.newVal = self.valEntry.get()
    