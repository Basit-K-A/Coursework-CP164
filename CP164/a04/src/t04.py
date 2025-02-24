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

Q1 = Queue()
for i in range(11):
    Q1.insert(i)
    
target1,target2 = Q1.split_alt()

print("target1:", list(target1), "target2", list(target2))