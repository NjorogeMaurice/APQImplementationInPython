

from tkinter import W, Entry, Label
from tkinter.messagebox import showerror
from tkinter.simpledialog import Dialog



class AddEntry(Dialog):
    
    newKey = -1
    newVal = ""

    def body(self, master):
        self.title("Add new Entry")
        Label(master, text='Priority Key:').grid(row=0, sticky=W)
        self.keyEntry= Entry(master, width = 16)
        Label(master, text='Patient Name:').grid(row=2, sticky=W)
        self.valEntry= Entry(master, width = 16)

        self.keyEntry.grid(row=0, column=1, sticky=W)
        self.valEntry.grid(row=2, column=1, sticky=W)

    def apply(self):
        AddEntry.newKey = self.keyEntry.get()
        AddEntry.newVal = self.valEntry.get()
    def exit(self):
        AddEntry.newKey = -1
        AddEntry.newVal = ""
    