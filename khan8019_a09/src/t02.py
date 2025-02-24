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
from Hash_set_sorted import Hash_Set
from functions import comparison_total, insert_words

fv = open("otoos610.txt","r",encoding="utf-8")
hash_set = Hash_Set(20)

insert_words(fv, hash_set)
total,mWord = comparison_total(hash_set)

print(f"""
Using array-based Sorted List Hash_Set

Total Comparisons: {total:,}
Word with maximum comparisons '{mWord.word}': {mWord.comparisons:,}
""")