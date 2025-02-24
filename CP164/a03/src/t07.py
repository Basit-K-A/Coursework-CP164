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
from Stack_array import Stack
from functions import stack_maze

maze = {'Start': ['A'], 'A':['B', 'C'], 'B':[], 'C':['D', 'E'],
            'D':[], 'E':['F', 'X'], 'F':['G', 'H'], 'G':[], 'H':[]}

maze = {'Start': ['H'], 'H':['B', 'C'], 'B':[], 'C':['D', 'E'],
    'D':[], 'E': ['X', 'F'], 'F':['G'], 'G':['C']}

#maze = {'Start': ['A'], 'A':[]}

stack_maze(maze)
