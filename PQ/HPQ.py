from queue import Empty
from PriorityQueueBase import PriorityQueueBase


class HPQ(PriorityQueueBase):
    
    def _parent(self,j):
        return (j-1)//2

    def _leftChild(self, j):
        return 2*j + 1

    def _rightChild(self,j):
        return 2*j + 2

    def _has_left(self,j):
        ## is index beyond end of the list
        return self._leftChild(j) < len(self._data)

    def _has_right(self,j):
        return self._rightChild(j) < len(self.data)

    def _swap(self,i,j):
        ## swap th elements at indices i and j of the array
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self,j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j,parent)
            self._upheap(parent)

    def _downheap(self,j):
        if self._has_left(j):
            left = self._leftChild(j)
            small_child = left
            if self._has_right(j):
                right = self._rightChild(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(j,small_child)
                self._downheap(small_child)

    # public methods for the HPQ

    def __init__(self):
        ## creating a new empty Priority Queue
        self._data = []

    def __len__(self):
        ## return the size of the PQ
        return len(self._data)

    def add(self,key,value):
        ## adding the key-value pairs to the PQ
        self._data.append(self._item(key,value))
        ## upheap newly added position
        self._upheap(len(self._data)-1)

    def min(self):
        ## return the pair with minimum key, but dont remove. Raise an exception if the PQ is empty
        if self.__len__:
            raise Empty('Priority Queue is empty')

        item = self._data[0]
        return(item._key, item._value)

    def removeMin(self):

        if self.__len__:
            raise Empty('Priority Queue is empty')
        self._swap(0,len(self._data)-1)
        item = self._data.pop()
        self._downheap(0)
        return (item._key,item._value)

    def size(self):
        return len(self._data)

c = HPQ()
c.add(0,"njoroge")
c.add(2,"kenya")

        



    

