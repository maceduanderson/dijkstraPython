'''
Created on 27 de abr de 2016

@author: Anderson Macedo
'''
import heapq

class PriorityQueue:
    
    def __init__(self, queue=[]):
        self._queue = queue
        heapq.heapify(self._queue)      
        self.index = 0
        
    def push(self, obj):
        heapq.heappush(self._queue, obj)
    
    def pop(self):
        return heapq.heappop(self._queue)
    
    def get_queue(self):
        return self._queue
    
    def empty(self):
        if len(self._queue):
            return False
        return True
    
    def update(self, obj):
        for i  in range(len(self._queue)):
            if self._queue[i].get_id() == obj.get_id():
                self._queue[i] = obj 
                heapq.heapify(self._queue)   
                return
