pantry_stock ={
 "Chicken_packet" : 0,
 "Roast_masala" : 1,
 "Onion" : 10,
 "Ginger_paste" : True,
 "Garlic_paste" : True,
 "Onion_paste" : True,
 "Cashew nut" : True,
 "Yogurt" : False,
 "Sugar" : False,
 "Oil" : True,
 "Garam_masala": True,
 "Rice" : 0
}

chicken_roast_recipe = {
    "Chicken_packet" : 1,
    "Roast_masala" : 1,
    "Onion" : 10,
    "Ginger_paste" : True,
    "Garlic_paste" : True,
    "Onion_paste" : True,
    "Cashew nut" : True,
    "Yogurt" : True,
    "Sugar" : True,
    "Oil" : True,
    "Garam_masala": True
}

ingredient_shopping_list = []


for ingredient, quantity in chicken_roast_recipe.items():
    if ingredient in pantry_stock and pantry_stock[ingredient] < quantity:
        ingredient_shopping_list.append(ingredient)

if len(ingredient_shopping_list) == 0 :
    print("You have all ingredients!")
else:
    print(f"You need to buy the following items:{ingredient_shopping_list}")