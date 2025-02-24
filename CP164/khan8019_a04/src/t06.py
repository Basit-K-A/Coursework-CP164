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
from Priority_Queue_array import Priority_Queue
from functions import pq_split_key

P1 = Priority_Queue()

for i in range(10):
    P1.insert(i)

target1, target2 = P1.split_key(5)

print("target1:",list(target1),"target2:",list(target2))