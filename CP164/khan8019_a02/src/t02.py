"""
------------------------------------------------------------------------
Assignment 2, task 2
------------------------------------------------------------------------
Author: Basit Khan
ID:     169058019
Email:  khan8019@mylaurier.ca
__updated__ = "2023-09-10"
------------------------------------------------------------------------
"""
from Food import Food
from Food_utilities import average_calories

food1 = Food('Mango',2,True,2000)
food2 = Food('Chicken',2,False,2000)
food3 = Food('Grape',2,False,1000)

foods = [food1,food2,food3]

print(average_calories(foods))