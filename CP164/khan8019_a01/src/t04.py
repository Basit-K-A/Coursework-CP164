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
from functions import file_analyze

fh = open("filefortest.txt","r",encoding="utf-8")

print(f"{file_analyze(fh)}")

fh.close()