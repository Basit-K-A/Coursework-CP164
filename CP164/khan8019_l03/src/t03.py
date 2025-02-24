"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Basit Khan
ID:     169058019
Email:  khan8019@mylaurier.ca
__updated__ = "2023-09-10"
------------------------------------------------------------------------
"""
from Queue_array import Queue
from utilities import array_to_queue, queue_to_array

q1 = Queue()

a = [1,2,3,4]

array_to_queue(q1, a)

b = []

queue_to_array(q1, b)

print(b)
#for q in q1:
#    print(q)

