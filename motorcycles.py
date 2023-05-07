# make your list variable names plural
motorcycles = ['honda', 'yamaha', 'suzuki', 'harley davidson']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)

bikes = []
bikes.append('indian')
bikes.append('harley')
bikes.append('triumph')
print(bikes)
print(bikes[-2].upper())
print(bikes[-1].title())

furnishings = ['desk', 'chair', 'table', 'floor lamp']
furnishings.insert(0, 'chaise lounge')
print(furnishings)

del furnishings[0]
print(furnishings)

# This is a new list with element 0 already removed. Does not use \
# the original furnishings list. furnishings list from line 24 
del furnishings[2]
print(furnishings)

print("\nThe original motorcycles list.")
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print("\nThe new motorcycles list.")
print(motorcycles)
print("\nThe popped list of motorcycles.")
print(popped_motorcycles)

last_owned = motorcycles.pop()
print(f"\nThe last motorcycle I owned was a {last_owned.title()}.")
first_owned = motorcycles.pop(0)
print(f"\nThe first motorbike I owned was a {first_owned.title()}. Honestly!")

# for lists you can use del, .pop(), .remove()
print(motorcycles)
#print(f"\nThe current motorcycles list after popping items off: {motorcycles.title()}.")

print(f"\nThe list of popped motorcycles is {popped_motorcycles}.")
motorcycles.remove('suzuki')
print(motorcycles)

motorcycles = ['yamaha', 'suzuki', 'ducati']
print(f'\nReinitializing the values of the "motorcycles list" {motorcycles}.')
doesnt_fit = 'ducati'
print(motorcycles)
print(f"\nA {doesnt_fit.title()} does not fit in this category of motorcycles.")