"""
------------------------------------------------------------------------
Assignment 2, task 3
------------------------------------------------------------------------
Author: Basit Khan
ID:     169058019
Email:  khan8019@mylaurier.ca
__updated__ = "2023-09-10"
------------------------------------------------------------------------
"""
from Food import Food
from Food_utilities import calories_by_origin

food1 = Food('Mango',2,True,2000)
food2 = Food('Chicken',1,False,2000)
food3 = Food('Grape',2,False,1000)

foods = [food1,food2,food3]

print(calories_by_origin(foods, 2))