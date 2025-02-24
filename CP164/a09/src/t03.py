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
from Hash_set_BST import Hash_Set
from functions import comparison_total, insert_words

fv = open("otoos610.txt","r",encoding="utf-8")
hash_set = Hash_Set(20)

insert_words(fv, hash_set)
total,mWord = comparison_total(hash_set)

print(f"""
Using linked BST Hash_set

Total Comparisons: {total:,}
Word with maximum comparisons '{mWord.word}': {mWord.comparisons:,}
""")