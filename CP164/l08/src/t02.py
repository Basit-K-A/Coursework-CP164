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
from morse import ByCode, ByLetter

B = ByCode('-...','B')
C = ByCode('-.-.','C')

print(B < C)

B = ByLetter('B','-...')
C = ByLetter('C','-.-.')

print(B < C)