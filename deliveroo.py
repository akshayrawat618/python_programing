expectedOutput = """\
==== Just Falafs ====
      ~ Menu ~
Starters
dumplings, peanuts or salad
Mains
bento, sushi, pasta or rice
Desserts
apples, strawberries or cheese
"""

food_categories = {
    "starters": [
        "peanuts", "bread", "salad", "dumplings"
    ],
    "mains": [
        "steak", "bento", "chicken", "pizza", "sandwich", "taco", "sushi",
        "burger", "hotdog", "pasta", "wrap", "rice"
    ],
    "desserts": [
        "apples", "strawberries", "cheese", "icecream", "pie", "cake"
    ]
}

chef_dishes = [
    "strawberries", "dumplings", "pasta", "rice", "apples", "salad", "peanuts",
    "cheese", "bento", "sushi"
]
'''
1. 3 empty list 
2. iterates through the chef dishes and comapre it with the food food_categories
3. if we find the matching dishes we will append it to the particular empty list.
'''

def comapre_dishes(chef_dishes,food_categories):
    starter = []
    mains= []
    dessert = []
    for dish in chef_dishes:
        if dish in food_categories["starters"]:
            starter.append(dish)
        elif dish in food_categories["mains"]:
            mains.append(dish)
        elif dish in food_categories["desserts"]:
            dessert.append(dish)
    
    print("starters")
    print(",".join(starter))
    print("mains")
    print(",".join(mains))
    print("Desserts")
    print(",".join(dessert))

def print_food_items():
    pass
       

comapre_dishes(chef_dishes, food_categories)