cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

# sort() and sorted() of list. sort() is permanent whereas \
# sorted() is temporary

#reinitialize cars list for this next exercise
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

print("\nHere is the list in reverse order:")
print(sorted(cars,reverse=True))

print("\nOne more time here is the original list again:")
print(cars)

print("\nNow here is the list in reverse order.")
cars.reverse() 
print(cars)

# reverse() only reverses the list from its original order it does \ 
# not put it reverse alphabetical order. this is permanent, but you can \ 
# apply reverse() a 2nd time to get the original. 

#reinitialize the cars[]
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)
print("\nThe length or number of cars in the cars list is", + len(cars))

# python counts the len() function starting at one (1). indexing \ 
# still starts from zero (0)