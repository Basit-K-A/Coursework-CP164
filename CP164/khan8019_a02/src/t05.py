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
from Food import Food
from Food_utilities import food_search

food1 = Food('Mango',2,True,2000)
food2 = Food('Chicken',1,False,2000)
food3 = Food('Grape',2,False,1000)
food4 = Food('Lavender',6,False,89)

foods = [food1,food2,food3,food4]

searched = food_search(foods, -1, 1111, False)

for f in searched:
    print(f)