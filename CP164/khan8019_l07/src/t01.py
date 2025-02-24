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
from List_linked import List

L1 = List()
L2 = List()
L1.append(2)
L1.append(4)
L1.append(2)
L1.append(4)
print(list(L1))
#L1.reverse_r()
#print(list(L1))
t1,t2 = L1.split_alt_r()
print(list(t1),list(t2))