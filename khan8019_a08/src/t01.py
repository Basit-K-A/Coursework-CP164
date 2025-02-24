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

B1 = BST()
B2 = BST()

B1.insert(3)
B1.insert(0)
B1.insert(4)
B1.insert(1)
B1.insert(2)
B1.insert(6)
B1.remove(3)

print(B1.inorder())
print(B1.preorder())
print(B1.postorder())
print(B1.levelorder())
