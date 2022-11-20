from xml.sax.xmlreader import Locator
from HPQ import HPQ
class AdaptablePriorityQueue(HPQ):
    ## a locator-based priority queue implemented with a binary heap
    ## ----------nested locator class-------------##
    class Locator1(HPQ._item):
        ## token for locating an entry of the priority queue
        ## adding index as an additional field
        __slots__ = '_index'

        def __init__(self, k, v,j):
            super().__init__(k, v)
            self._index = j

    ##--------protected class methods------------##
    ## override swap method to record new indices
    def _swap(self, i, j):
        ## perform the swap
        super()._swap(i, j)
        ## reset locator index (post-swap)
        self._data[i]._index = i
        self._data[j]._index = j

    def _bubble(self,j):
        if j>0 and self._data < self._data[self._parent(j)]:
            self._upheap(j)
        else:
            self._downheap(j)

    def add(self,key,value):
        ## add a key-value pair
        ## initialize locator index
        token = self.Locator1(key,value,len(self._data))
        self._data.append(token)
        self._upheap(len(self._data)-1)
        return token

    def update(self,loc,newkey,newval):
        ## replacing key and value
        j = loc._index
        if not(0<=j<len(self) and self._data[j] is loc):
            raise ValueError('invalid locator')
        loc._key = newkey
        loc._value = newval
        self._bubble(j)

    def remove(self,loc):
        j = loc._index
        if not (0 <= j < len(self) and self._data[j] is loc):
            raise ValueError('Invalid locator')
        if j == len(self) - 1:
            self._data.pop()
        else:
            self._swap(j,len(self)-1)
            self._data.pop()
            self._bubble(j)
        return (loc._key, loc._value)


c = AdaptablePriorityQueue()

print(c.min())    


    

