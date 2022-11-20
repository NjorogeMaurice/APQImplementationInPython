class PriorityQueueBase:

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
