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
from Deque_linked import Deque

D1 = Deque()
D2 = Deque()

D1.insert_rear(0)
D1.insert_rear(1)
D1.insert_rear(2)
D1.insert_rear(3)
#D1.insert_rear(5)
#D1.insert_rear(3)

# front node (0)

l = D1._front

# rear node (-1)

r = D1._rear

print(list(D1))
D1._swap(l,r)
#print(D1 == D2)

print(list(D1))

print(D1.peek_rear())


