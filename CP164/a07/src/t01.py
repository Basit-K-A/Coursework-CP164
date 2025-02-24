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

L1.append(11)
L1.append(22)
L1.append(33)
L1.append(44)
L1.append(44)
print(list(L1))
L,J = L1.split()
print(list(L),list(J))

