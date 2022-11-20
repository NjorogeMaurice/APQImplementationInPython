from tkinter import W, Entry, Label
from tkinter.messagebox import showerror
from tkinter.simpledialog import Dialog



class RemoveEntry(Dialog):
    
    loc = -1

    def body(self, master):
        self.title("Remove Existing Entry")
        Label(master, text='Patient index:').grid(row=0, sticky=W)
        self.keyEntry= Entry(master, width = 16)

        self.keyEntry.grid(row=0, column=1, sticky=W)
        

    def apply(self):
        RemoveEntry.loc = self.keyEntry.get()