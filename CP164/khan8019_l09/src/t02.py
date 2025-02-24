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
from Hash_Set_array import Hash_Set

H = Hash_Set(5)

H.insert(99)
H.insert(99)
H.insert(4)
H.insert(7)
H.insert(5)
H.insert(42)

H._rehash()
#H.remove(4)
#H.insert(4)

#print(H._count)
for f in H:print(f)

#H.debug()