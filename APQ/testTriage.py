from tkinter import BOTTOM,TOP,Canvas,Tk,Button,RAISED,PhotoImage
from tkinter.messagebox import showerror, showinfo
from Names import Names
from AddEntryGUI import AddEntry
from UpdateKeyGUI import UpdateKey
from UpdateValueGUI import UpdateValue
from RemoveEntryGUI import RemoveEntry

## class HospitalTriage
class HospitalTriage():

    class _item:
        ## Lightweight composite to store priorirty queue items
        __slots__ = '_key','_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __It__(self,other):
            return self._key < other._key

        def is_Empty(self):
            ## return true if priority queue is empty
            return len(self) == 0

    class Locator1(_item):
        ## token for locating an entry of the priority queue
        ## adding index as an additional field
        __slots__ = '_index'

        def __init__(self, k, v,j):
            super().__init__(k, v)
            self._index = j

    ## constructor
    def __init__(self, window: Tk):

        self.img2 = PhotoImage(file="img2.png")
        self.img1 = PhotoImage(file="img1.png")

        self.text = "Key:\n{key}\n\nValue:\n{value}\n\nIndex:\n{index}"
        ## Storing instances of the Patients
        self.Patients=[]
        self.Details = []
        ## Names class constructor
        self.getNames = Names()

        self.window = window
        ## creating an empty apq
        self.APQ =[]
        ## top side is the APQ
        self.top_panel = Canvas(self.window,width=(window_width),height=(window_height/2))
        self.top_panel.pack(side=TOP)
        ## bottom side is the buttons: len(), isEmpty(), min(), add(), updateKey(), updateValue(), remove(), removeMin()
        self.bottom_panel = Canvas(self.window,width=(window_width),height=(window_height/2))
        self.bottom_panel.pack(side=BOTTOM)
        ## Buttons
        Button(self.bottom_panel, text="size", fg="white", bg="blue", font=("Purissa", 14, "italic"),
           relief=RAISED,bd=7,command=self.sizeInfo).place(x=40, y=140)
        Button(self.bottom_panel, text="add", fg="white", bg="blue", font=("Purissa", 14, "italic"),
           relief=RAISED,bd=7,command=self.addToQueue).place(x=150, y=140)
        Button(self.bottom_panel, text="min", fg="white", bg="blue", font=("Purissa", 14, "italic"),
           relief=RAISED,bd=7,command=self.min).place(x=260, y=140)
        Button(self.bottom_panel, text="isEmpty", fg="white", bg="blue", font=("Purissa", 14, "italic"),
           relief=RAISED,bd=7, command=self.isEmptyInfo).place(x=360, y=140)
        Button(self.bottom_panel, text="removeMin", fg="white", bg="blue", font=("Purissa", 14, "italic"),
           relief=RAISED,bd=7,command=self.removeMin).place(x=500, y=140)
        Button(self.bottom_panel, text="updateKey", fg="white", bg="blue", font=("Purissa", 14, "italic"),
           relief=RAISED,bd=7,command=self.updateKeyInfo).place(x=660, y=140)
        Button(self.bottom_panel, text="updateValue", fg="white", bg="blue", font=("Purissa", 14, "italic"),
           relief=RAISED,bd=7, command=self.updateValInfo).place(x=820, y=140)
        Button(self.bottom_panel, text="remove", fg="white", bg="blue", font=("Purissa", 14, "italic"),
           relief=RAISED,bd=7,command=self.removeInfo).place(x=1000, y=140)
        ## Top panel elements
        self.top_panel.create_line(10,0,10,800,width=20,smooth=True)
        self.top_panel.create_line(200,0,200,800,width=20,smooth=True)
        self.top_panel.create_text(100,80,text="Caring Hospital",font=("Purissa",14,"italic"))
        self.top_panel.create_line(240,490, 1150, 490, width=20,smooth=True)
        
    def parent(self,j):
        return (j-1)//2

    def leftChild(self, j):
        return 2*j + 1

    def rightChild(self,j):
        return 2*j + 2

    def has_left(self,j):
        ## is index beyond end of the list
        return self.leftChild(j) < len(self.APQ)

    def has_right(self,j):
        return self.rightChild(j) < len(self.APQ)

    def swap(self,i,j):

        ## swap the elements at indices i and j of the array
        self.APQ[i], self.APQ[j] = self.APQ[j], self.APQ[i]
        self.APQ[i]._index = i
        self.APQ[j]._index = j

    def upheap(self,j):
        parent = self.parent(j)
        loc = self.APQ[j]
        loc2 = self.APQ[parent]
        if j > 0 and loc._key < loc2._key:
            
            self.SwapPatients(j,parent)
            self.UpheapPatients(parent)
            self.swap(j,parent)
            self.UpdatePos(j,parent)
            self.upheap(parent)

    def downheap(self,j):
        if self.has_left(j):
            left = self.leftChild(j)
            small_child = left
            loc1 = self.APQ[small_child]
            loc3 = self.APQ[j]
            if self.has_right(j):
                right = self.rightChild(j)
                loc = self.APQ[right]
                loc2 = self.APQ[left]
                if loc._key < loc2._key:
                    small_child = right
            if loc1._key < loc3._key:
                self.SwapPatients(j,small_child)
                self.DownHeapPatients(small_child)
                self.swap(j,small_child)
                self.UpdatePos(small_child,j)
                self.downheap(small_child)

    def add(self,key,value):
        ## adding the key-value pairs to the PQ
        if key < 0 and value == "":
            return -1
        token = self.Locator1(key,value,len(self.APQ))
        self.APQ.append(token)
        ## upheap newly added position
        self.DrawPatient(value,len(self.APQ)-1)
        self.upheap(len(self.APQ)-1)

       

    def min(self):
        ## return the pair with minimum key, but dont remove. Raise an exception if the PQ is empty
        if len(self.APQ)==0:
            showerror("Empty Queue", "The queue is empty")

        item = self.APQ[0]
        showinfo( "Minimum Entry ",str((item._key,item._value)))

    def removeMin(self):

        if len(self.APQ) == 0:
            showerror("Error", "Queue is empty" )
        self.SwapPatients(0,len(self.APQ)-1)
        self.DownHeapPatients(0)
        self.swap(0,len(self.APQ)-1)
        item = self.APQ.pop()
        patient = self.Patients.pop()
        details = self.Details.pop()
        self.top_panel.delete(patient)
        self.top_panel.delete(details)
        self.top_panel.update()
        self.downheap(0)
        showinfo("Removed minimum", str((item._key,item._value))) 
    
    def bubble(self,j):
        loc1 = self.APQ[j]
        loc2 = self.APQ[self.parent(j)]
        if j>0 and loc1._key < loc2._key:
            self.upheap(j)
        else:
            self.downheap(j)

    def updateKey(self,loc,newkey):
        ## replacing key
        j = int(loc)
        if j < 0:
            return -1
        k = self.APQ[j]
        m = self.Details[j]  
        if not(0<=j<len(self.APQ) and k._index is j):
            return "Invalid locator"
        k._key = int(newkey)
        self.top_panel.delete(self.Details[j])
        self.Details.pop(j)
        self.Details.insert(j,self.top_panel.create_text(300 + (j * 60), 300, text=self.text.format(key=k._key,value=k._value,index=k._index),font="Purissa"))
        self.top_panel.update()
        self.bubble(j)

    def updateVal(self,loc,newval):
        ## replacing key
        j = int(loc)
        if j < 0:
            return -1
        k = self.APQ[j]
        if not(0<=j<len(self.APQ) and k._index is j):
            return "Invalid locator"
        k._value = str(newval)
        self.top_panel.delete(self.Details[j])
        self.Details.pop(j)
        self.Details.insert(j,self.top_panel.create_text(300 + (j * 60), 300, text=self.text.format(key=k._key,value=k._value,index=k._index),font="Purissa"))
        self.top_panel.update()
        self.bubble(j)

    def remove(self,loc): 
        if not (0 <= loc <= len(self.APQ)):
            return "Invalid locator"
        k = self.APQ[loc]
        if (loc) == len(self.APQ) - 1:
            self.APQ.pop()
            a =self.Details.pop()
            b =self.Patients.pop()
            self.top_panel.delete(a)
            self.top_panel.delete(b)
            self.top_panel.update()
        else:
            self.SwapPatients((loc),len(self.APQ)-1)
            self.swap((loc),len(self.APQ)-1)
            self.UpdatePos(len(self.APQ)-1,loc)
            self.APQ.pop()
            n =self.Details.pop()
            m =self.Patients.pop()
            self.top_panel.delete(m)
            self.top_panel.delete(n)
            self.bubble((loc))  
        return (k._key, k._value)

    def size(self):
        return len(self.APQ)

    def DrawPatient(self,name,j):
        if name in self.getNames.boyNames:
            self.Patients.append(self.top_panel.create_image((300 + (j*60),425),image=self.img1))
            self.Details.append(self.top_panel.create_text(300 + (j*60),300,font="Purissa", text=self.text.format(key=self.APQ[j]._key,value=self.APQ[j]._value,index = self.APQ[j]._index)))
        elif name in self.getNames.girlNames:
            self.Patients.append(self.top_panel.create_image((300 +(j*60),425),image=self.img2))
            self.Details.append(self.top_panel.create_text(300 + (j*60),300,font="Purissa", text=self.text.format(key=self.APQ[j]._key,value=self.APQ[j]._value,index = self.APQ[j]._index)))
        else:
            return -1

    def SwapPatients(self,a,b):
        self.Patients[a],self.Patients[b] = self.Patients[b], self.Patients[a]
        self.Details[a],self.Details[b] = self.Details[b], self.Details[a]
        self.top_panel.coords(self.Patients[a], 300+ (a * 60), 425)
        self.top_panel.coords(self.Patients[b], 300 +(b * 60), 425)
        self.top_panel.coords(self.Details[a], 300+ (a * 60), 300)
        self.top_panel.coords(self.Details[b], 300 +(b * 60), 300)
        self.top_panel.update()

    def UpheapPatients(self,j):
        parent = self.parent(j)
        loc = self.APQ[j]
        loc2 = self.APQ[parent]
        if j > 0 and loc._key < loc2._key:
            self.SwapPatients(j,parent)
            self.UpheapPatients(parent)

    def DownHeapPatients(self,j):
        if self.has_left(j):
            left = self.leftChild(j)
            small_child = left
            loc1 = self.APQ[small_child]
            loc3 = self.APQ[j]
            if self.has_right(j):
                right = self.rightChild(j)
                loc = self.APQ[right]
                loc2 = self.APQ[left]
                if loc._key < loc2._key:
                    small_child = right
            if loc1._key < loc3._key:
                self.SwapPatients(j,small_child)
                self.DownHeapPatients(small_child)

    def UpdatePos(self,a,b):
        parent = self.Details[a]
        child = self.Details[b]
        loc1 = self.APQ[a]
        loc2 = self.APQ[b]
        self.top_panel.delete(parent)
        self.top_panel.delete(child)
        self.Details.pop(a)
        self.Details.pop(b)
        self.Details.insert(b,self.top_panel.create_text(300 + (b * 60), 300, text=self.text.format(key=loc2._key,value=loc2._value,index=loc2._index),font="Purissa"))
        self.Details.insert(a,self.top_panel.create_text(300 + (a * 60), 300, text=self.text.format(key=loc1._key,value=loc1._value,index=loc1._index),font="Purissa"))
        self.top_panel.update()

    def addToQueue(self):
        c = AddEntry(root)
        key = c.newKey
        val = c.newVal
        self.add(int(key),str(val))
        c.newKey = -1
        c.newVal = ""

    ## size()
    def sizeInfo(self):
        msg = self.size()
        showinfo("Length",str(msg))
    
    def removeInfo(self):
        c = RemoveEntry(root)
        loc = c.loc
        showinfo("Remove Entry   ", "Removed entry is: \n"+str(self.remove(loc=int(loc))))  

    def updateKeyInfo(self):
        c = UpdateKey(root)
        loc = c.loc
        newKey = c.newKey
        self.updateKey(loc,newKey)
       
    def updateValInfo(self):
        c = UpdateValue(root)
        loc = c.loc
        newVal = c.newVal
        self.updateVal(loc,newVal)
                  
    def isEmptyInfo(self):
        if(len(self.APQ)== 0):
            info = "True"
        else:
            info = "False"
        showinfo("isEmpty()", info)
        
if __name__ == '__main__':
    window_height = 1000
    window_width = 1200

    root = Tk()

    root.title('APQ implementation in Python')
    root.maxsize(window_width, window_height)
    root.minsize(window_width, window_height)
    HospitalTriage(root)
    root.mainloop()
