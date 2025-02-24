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
from Letter import fill_letter_bst,DATA2
from functions import letter_table,comparison_total,do_comparisons

B2 = BST()
file_variable = open("miserables.txt","r",encoding="utf-8")
#Fill BST's
fill_letter_bst(B2, DATA2)

do_comparisons(file_variable, B2)
c2 = comparison_total(B2)



letter_table(B2)

file_variable.close()