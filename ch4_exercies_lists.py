# 4-10 Slices
more_food = ['spinach dip', 'popcorn shrimp', 'old fashion cocktail', 'chicken noodle soup', 'cheese cake', 'espresso', 'cherry pie']
print("\nThe first three items on my new food list are:")
print(more_food[:3])
print("\nThe middle three food items are:")
print(more_food[2:5])
print("\nThe last three times on my updated food list are:")
print(more_food[-3:])

# 4-11 My Pizzas, Your Pizzas
my_pizzas = ['pepperoni', 'hawaiian', 'supreme']
friends_pizza = my_pizzas[:]

my_pizzas.append("meat lover's")
print("\nMy favorite pizzas are:")
for pizza in my_pizzas[:len(my_pizzas)+1]:
    print(pizza.title())

friends_pizza.append('double pepperoni')
print("\nMy friend's favorite pizzas are:")
for fpizza in friends_pizza[:len(friends_pizza)+1]:
    print(fpizza.title())

# 4-12 More Loops
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_food = my_foods[:]
my_foods.append('spaghetti')
friends_food.append('sweet potato fries')
print("\nMy all time favorite foods are:")
for food in my_foods[:len(my_foods)+1]:
    print(food.title())

print("\nMy friend prefers these foods:")
for ffood in friends_food[:len(friends_food)+1]:
    print(ffood.title())

