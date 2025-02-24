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
from Letter import DATA1,DATA2,DATA3,fill_letter_bst
from BST_linked import BST
from functions import do_comparisons, comparison_total, letter_table

B1 = BST()
B2 = BST()
B3 = BST()

file_variable = open("miserables.txt","r",encoding="utf-8")

#Fill BST's
fill_letter_bst(B1, DATA1)
fill_letter_bst(B2, DATA2)
fill_letter_bst(B3, DATA3)

do_comparisons(file_variable, B1)
c1 = comparison_total(B1)

do_comparisons(file_variable, B2)
c2 = comparison_total(B2)

do_comparisons(file_variable, B3)
c3 = comparison_total(B3)

file_variable.close()

print(f"""
Comparing by order: ABCDEFGHIJKLMNOPQRSTUVWXYZ
Total Comparisons: {c1:,}
------------------------------------------------------------
Comparing by order: MFTCJPWADHKNRUYBEIGLOQSVXZ
Total Comparisons: {c2}
------------------------------------------------------------
Comparing by order: ETAOINSHRDLUCMPFYWGBVKJXZQ
Total Comparisons: {c3}
""")


print(letter_table(B1))



"""
test print to see BST's
for b in B1:
    print(b)
print("-"*40)
for b in B2:
    print(b)
print("-"*40)
for b in B3:
    print(b)
print("-"*40)
"""