'''
Created on 27 de abr de 2016

@author: Anderson Macedo
'''
import random
import unittest

from DataStruct.PriorityQueue import PriorityQueue


class Test(unittest.TestCase):
    
    def setUp(self):
        self.int_list = [ i for i in range(1, 100)]
        self.expected = list(self.int_list) 
        random.shuffle(self.int_list)
        self.queue = PriorityQueue(self.int_list)


    def testQueue(self):
        
        
        ordered_list = []
        self.expected.sort(cmp=None, key=None, reverse=False)
        
        while not self.queue.empty():
            ordered_list.append(self.queue.pop())
        
        self.assertListEqual(self.expected, ordered_list, 'expected : ' +str(self.expected) + ' ' + str(ordered_list) )
        pass
    
    def tearDown(self):
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testQueue']
    unittest.main()