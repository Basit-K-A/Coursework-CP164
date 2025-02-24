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
from Letter import Letter

def do_comparisons(file_variable, bst):
    """
    -------------------------------------------------------
    Retrieves every letter in file_variable from bst. Generates
    comparisons in bst objects. Each Letter object in bst contains
    the number of comparisons found by searching for that Letter
    object in file_variable.
    Use: do_comparisons(file_variable, bst)
    -------------------------------------------------------
    Parameters:
        file_variable - the already open file containing data to evaluate (file)
        bst - the binary search tree containing 26 Letter objects
            to retrieve data from (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    
    data = file_variable.read()
    
    for c in data:
        if c.isalpha():
            tmp_letter = Letter(c.upper())
            bst.retrieve(tmp_letter)
    
    return
    

def comparison_total(bst):
    """
    -------------------------------------------------------
    Sums the comparison values of all Letter objects in bst.
    Use: total = comparison_total(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        total - the total of all comparison fields in the bst
            Letter objects (int)
    -------------------------------------------------------
    """
    temp = bst.inorder()
    total = 0
    
    for letter in temp:
        total+=letter.comparisons
        
    return total

def letter_table(bst):
    """
    -------------------------------------------------------
    Prints a table of letter counts for each Letter object in bst.
    Use: letter_table(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    total = 0
    letters = bst.inorder()
    
    for L in letters:
        total += L.count
    
    print(f"""
Letter Count/Percent Table

Total Count: {total:,}

Letter  Count       %
---------------------""")

    for L in letters:
        pc = L.count/total*100
        print(f"{L.letter:<1s}{L.count:>15,d}{pc:>8.2f}")
    
    return
    
        
    