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
#from Hash_Set_array import Hash_Set
from functions import hash_table
from Food_utilities import read_foods

f1 = open("foods.txt","r",encoding="utf-8")
Foo1 = read_foods(f1)

hash_table(7, Foo1)

f1.close()



