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
from Stack_array import Stack
#from functions import stack_combine

source1 = Stack()

v = [8,12,8,5]
for i in range(len(v)):
    source1.push(v[i])


source2 = Stack()

b = [14,9,7,1,6,3]
for i in range(len(b)):
    source2.push(b[i])

cat = Stack()

cat.combine(source1,source2)

for ca in cat:
    print(ca)
