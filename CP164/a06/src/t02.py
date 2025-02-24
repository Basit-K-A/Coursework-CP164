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
from Priority_Queue_linked import Priority_Queue

PQ1 = Priority_Queue()

PQ1.insert(11)
PQ1.insert(22)
PQ1.insert(33)
PQ1.insert(44)
#PQ1.insert(1)
print(list(PQ1))

"""
PQ2,PQ3 = PQ1.split_alt()
print(list(PQ2),list(PQ3))
"""
PQ2,PQ3 = PQ1.split_key(33)
print(list(PQ2),list(PQ3))