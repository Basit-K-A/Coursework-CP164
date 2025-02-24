"""
Lab 1, testing
------------------------------------------------------------------------
------------------------------------------------------------------------
Author: Basit Khan
ID:     169058019
Email:  khan8019@mylaurier.ca
__updated__ = "2023-01-11"
------------------------------------------------------------------------
"""
from Food import Food
from Food_utilities import get_food, read_food, read_foods, write_foods, get_vegetarian

food1 = Food('Mango',2,True,200)
#food2 = Food('Chicken',3,False,2000)

print(food1.origins())
print(food1)

#foods = [food1,food2]
#print(read_food('Butter Chicken|2|False|490'))
#f1 = open("foods.txt","r",encoding="utf-8")
#f2 = open("new-foods.txt","w",encoding="utf-8")

#print(read_foods(f1))
#print(get_vegetarian(foods))
#f1.close()
#f2.close()