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
from Sorts_Deque_linked import Sorts
from Deque_linked import Deque

a = Deque()
b = [4,3333,1,5,22]

for i in b:
    a.insert_rear(i)
    
print(list(a))
Sorts.gnome_sort(a)
print(list(a))