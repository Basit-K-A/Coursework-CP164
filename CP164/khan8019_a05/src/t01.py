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
from List_array import List

L1 = List()
L2 = List()
L3 = List()
L4 = List()
L5 = List()

print("append 0 and 1 in loop for L1 and L2 5 times")
for i in range(5):
    L1.append(0)
    L1.append(1)
    L2.append(0)
    L2.append(1)
print("is l1 equal to l2?:",L1 == L2)
L2.append(0)
print("Append 0(L2): 0")
L1.append(1)
print("Append 1(L1): 1")
L1.prepend(1)
print("Prepend 1(L1): 1")
L1.prepend(1)
print("Prepend 1(L1): 1")

print(list(L1),list(L2))
L3.intersection(L1,L2)
L4.union(L1, L2)
print("L3 intersection of L1 and L2:",list(L3))
print("L4 union of L1 and L2:",list(L4))
#L2.clean()
#print(list(L1))
L1.remove_front()
print("L1 front removed: ",list(L1))
L1.remove_many(0)
print("L1 many removed(0): ",list(L1))


L1.prepend(5)
print("Prepend (L1): 5")
L1.append(15)
print("append (L1): 15")

t1 = L1[-1]
t2 = L1[0]

print("t1 = L1[-1],t2 = L1[0]",t1,t2)

L5.combine(L1, L2)
print("L5.combine(L1,L2):",list(L5))

L5.clean()
print("L5 cleaned:",list(L5))

target1,target2 = L5.split()
print("target1,target2 = L5.split()")
print(list(target1),list(target2))

"""
print(list(L1))
target1,target2 = L1.split_alt()
print(list(L1))
print(list(target1),list(target2))"""