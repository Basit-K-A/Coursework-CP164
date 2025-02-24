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
from Sorted_List_array import Sorted_List

S1 = Sorted_List()
S2 = Sorted_List()
S3 = Sorted_List()
S4 = Sorted_List()
#S5 = Sorted_List()
S1.insert(6)
for i in range(5):
    pass
    S1.insert(11)
    S1.insert(2)
    
S2.insert(2)
S2.insert(6)
S2.insert(7)
S2.insert(12)
S2.insert(1)
S2.insert(3)
print("List1",list(S1))
print("List2",list(S2))
print("2 in list 1:",(2 in S1))
print("List1 and 2 equal?:",(S1==S2))
Sget = S1[0]
print("Sget = S1[0]",Sget)
Sget = S1[-1]
print("Sget = S1[-1]",Sget)
print("count 11 in S1",S1.count(11))
print("Find 11 in S1",S1.find(11))
print("Find 13 in S1",S1.find(13))
print("Index 6 in S1",S1.index(6))
S3.intersection(S1,S2)
print("S3 = Intersection(S1,S2)",list(S3))
print("max S1",max(S1))
print("min S1",min(S1))
print("peek S2",S2.peek())
S2.remove(3)
print("remove 3 from S2",list(S2))
S2.remove_front()
print("remove from S2",list(S2))
S1.remove_many(11)
print("remove many 11 from S1",list(S1))
S4.union(S1,S2)
t1,t2 = S1.split()
print("t1,t2 = S1.split()",list(t1),list(t2))
g1,g2 = S2.split_alt()
print("g1,g2 = S2.split_alt()",list(g1),list(g2))
print("S4 = Union(S1,S2)",list(S4))

target1, target2 = S4.split_key(3)
print("target1, target2 = S4.split_key(3)",list(target1),list(target2))
#S1.clean()
"""
S1.remove_many(9)
print(list(S1))

print("max",max(S1))
print("min",min(S1))
print("find 9 (index):",S1.find(9))
print("peek:",S1.peek())"""