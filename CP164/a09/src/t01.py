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
from Hash_Set_array import Hash_Set
from functions import comparison_total, insert_words

fv = open("otoos610.txt","r",encoding="utf-8")
hash_set = Hash_Set(20)

insert_words(fv, hash_set)
total,mWord = comparison_total(hash_set)

for h in hash_set:print(h)

print(f"""
Using array-based list Hash_Set

Total Comparisons: {total:,}
Word with maximum comparisons '{mWord.word}': {mWord.comparisons:,}
""")