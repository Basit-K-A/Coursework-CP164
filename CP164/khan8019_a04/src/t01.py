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
from Queue_circular import Queue

Q1 = Queue()
Q2 = Queue()

print(f"is_empty expects True: {Q1.is_empty()}")

print(f"is_full expects False: {Q1.is_full()}")

print(f"insert(5)"),Q1.insert(5)
print(f"insert(6)"),Q1.insert(6)

print(f"insert(5)(Q2)"),Q2.insert(5)
print(f"insert(6)(Q2)"),Q2.insert(6)

print(f"is_equal Q1 and Q2 expects true: {Q1 == Q2}")

print(f"peek expects 5: {Q1.peek()}")

print(f"is_empty expects False: {Q1.is_empty()}")
print("Q1 as list:",list(Q1))
print(f"remove expects 5: {Q1.remove()}")

print("Q1 as list:",list(Q1))

print("insert i in range(1,9)")
for i in range(1,9): Q1.insert(i)

print("Q1 as list:",list(Q1))
print(f"is_full expects True: {Q1.is_full()}")
print(f"remove expects 6: {Q1.remove()}")



print("Q1 as list:",list(Q1))
print(f"length: {len(Q1)}")

print("removing all")
for i in range(1,9): Q1.remove()
print("Q1 as list:",list(Q1))

print(f"is_equal Q1 and Q2 expects false: {Q1 == Q2}")
