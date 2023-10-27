my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] # must include the [:] the slice to get unique and separate lists. 

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy new list of favorite foods now include:")
print(my_foods)

print("\nMy friend's food is updated to include:")
print(friend_foods)
