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
from BST_linked import BST

B = BST()

B.insert(11)
B.insert(7)
B.insert(15)
B.insert(6)
B.insert(9)
B.insert(12)
B.insert(18)
B.insert(8)
B.insert(13)
print("BST in levelorder:")
print(B.levelorder())

print("-"*40)
print("Node counts:")
print(B.node_counts())

print("-"*40)
print("7 in BST:")
print(7 in B)
print("77 in BST:")
print(77 in B)
print("13 in BST:")
print(13 in B)

print("-"*40)
print("parent of 15 (iterative):")
print(B.parent(15))
print("parent of 8 (iterative):")
print(B.parent(8))
print("parent of 99 (iterative):")
print(B.parent(99))

print("-"*40)
print("parent of 15 (recursive):")
print(B.parent_r(15))
print("parent of 8 (recursive):")
print(B.parent_r(8))
print("parent of 99 (recursive):")
print(B.parent_r(99))
