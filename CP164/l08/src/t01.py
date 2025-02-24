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
from morse import ByLetter, ByCode, fill_letter_bst, fill_code_bst, encode_morse, DATA1,\
    decode_morse
from BST_linked import BST

B = ByCode('B', '-...')
C = ByCode('C', '-.-.')
BS = BST()
values = DATA1
text = ("This is a string")
morsetest = ("... --- ...")

fill_code_bst(BS, values)

#mors = encode_morse(BS,text)
#print(mors)

print(decode_morse(BS,morsetest))

