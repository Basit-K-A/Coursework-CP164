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

def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """
    target = Stack()
    tar = []
    oneEmpt = False
    twoEmpt = False
    
    while not oneEmpt or not twoEmpt:
        
        if not source1.is_empty():
            enter = source1.pop()
            #print(enter)
            target.push(enter)
            
        else: oneEmpt = True
        
        if not source2.is_empty():
            enter = source2.pop()
            target.push(enter)
        else: twoEmpt = True
        
    #target.push(tar)
    
    return target

def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    tempList = []
    
    while not source.is_empty():
        val = source.pop()
        tempList.append(val)
    
    while tempList:
        vale = tempList.pop(0)
        source.push(vale)
    
    #for s in source:
    #    print(s)
    
    return

def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    stac = Stack()
    palindrome = True
    
    for i in range(len(string)):
        if string[i].isalpha():
            stac.push(string[i].lower())
    #for s in stac:
    #    print(s)
        
    for i in range(len(string)):
        if string[i].isalpha():
            val = stac.pop()
            if val != string[i].lower():
                palindrome = False
    
    return palindrome

# Constants
OPERATORS = "+-*/"

def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    values = Stack()
    #values.push(OPERATORS)
    #strer = OPERATORS.split()
    #print(strer)
    
    splitted = string.split()
    
    for i in range(len(splitted)):
        if splitted[i].isnumeric():
            values.push(splitted[i])
        if splitted[i] in OPERATORS:
            temp1 = int(values.pop())
            temp2 = int(values.pop())
                
            if splitted[i] == "+":
                values.push(temp2+temp1)
            elif splitted[i] == "*":
                values.push(temp2*temp1)
            elif splitted[i] == "-":
                values.push(temp2-temp1)
            else:
                values.push(temp2/temp1)
                
                
            
    for v in values:
        print(v)
    return

def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points visited before the exit is reached,
            does not include 'Start', but does include 'X'.
            Return None if there is no exit (list of str)
    -------------------------------------------------------
    """
    ended = False
    stack = Stack()
    path = []
    
    key = 'Start'
    value = maze[key]
    
    for c in value:
        stack.push(c)
    
    while ended == False:
        if 'X' in value:
            path.append('X')
            ended = True
            break
        
        if not stack.is_empty():
            popped = stack.pop()
            path.append(popped)
        else: 
            path = None
            break
        
        if popped == 'X':
            ended = True
            break

        value = maze[popped]
        
        for c in value:
            stack.push(c)

    #print(path)
    return path
    