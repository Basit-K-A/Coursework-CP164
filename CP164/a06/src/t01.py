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
from Queue_linked import Queue

Q1 = Queue()
Q2 = Queue()
Q3 = Queue()

#Q1.insert(11)
#Q1.insert(22)
#Q1.insert(33)
Q2.insert(44)
Q2.insert(99)
Q2.insert(999)
#Q1.insert(44)
#Q1.insert(99)
#Q.insert(999)
#Q1._append_queue(Q2)
#print(list(Q1),list(Q2))

print(Q1 == Q2)
#print(Q1._front._next,Q1._rear._next)

Q2.insert(3)
Q2.insert(4)
Q2.insert(5)

print(Q1.is_empty())
print(Q1.is_full())
Q1.insert(3)
Q1.insert(4)
Q1.insert(5)
Q1.remove()

print("peek:",Q1.peek())
Q1.remove()
Q1.remove()
print(list(Q1),list(Q2))
Q1._move_front_to_rear(Q2)
Q1._move_front_to_rear(Q2)

#Q1._append_queue(Q2)
print(list(Q1),list(Q2))

Q3.combine(Q2, Q1)
print(list(Q3))
print(list(Q1),list(Q2))
#Q3,Q4 = Q2.split_alt()

#print("Q3,Q4 = Q2.split_alt()",list(Q3,list(Q4)))
