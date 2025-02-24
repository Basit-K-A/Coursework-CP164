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
from utilities import array_to_list, list_to_array, list_test
from Food import Food
from Food_utilities import read_foods

f1 = open("foods.txt","r",encoding="utf-8")

source = []
llist = List()


llist.append(4)
llist.append(5)
llist.append(6)
llist.append(7)

#print(llist.is_empty())
list_to_array(llist, source)
#array_to_list(llist, source)


print(source)
#list_test(source)
#for l in llist:
#    print(l)