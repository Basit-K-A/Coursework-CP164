2"""
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
from utilities import array_to_stack, stack_to_array, stack_test
from Food_utilities import read_foods

#f1 = open("foods.txt","r",encoding="utf-8")

a = [0,3,3,2,1,0]
s = Stack()
#print(a)

s.push(3)
s.push(2)
s.push(4)
s.push(-3)

#print(stack_test(a))


#print(f"{stack_to_array(s,a)}")

#print(a[-1])

#s.push(7)

#print(s.peek())

#s.pop()

#print(s.is_empty())

#f1.close()