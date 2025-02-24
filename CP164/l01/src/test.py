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

def stringlen(string):
    if string == "":
        ans = 0
    else:
        ans = 1 + stringlen(string[1:])
    return ans

print(stringlen("Food"))