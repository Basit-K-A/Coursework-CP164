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
from Sorts_List_linked import Sorts
from List_linked import List
a = List()
b = [999, 832, 5673, 787, 118, 72,0,2,1]
for i in b:
    a.append(i)
    
print(list(a))
Sorts.radix_sort(a)
print("-"*40)
print(list(a))