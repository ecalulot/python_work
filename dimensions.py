# tuples are immutable lists (immutable means they cannot be changed)
# (in object-oriented programming) of or noting an object with a fixed structure and properties whose values cannot be changed.
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
#dimensions[0] = 250 # just to see that tuples are unchanging
# line 6 will cause the program to exit out. 

# tuples are actually defined by the , but the () make it look neater
# tuples can be single value/item too
my_t = (3,)
print(my_t)

for dimension in dimensions:
    print(dimension)

print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

# tuples are simple data structures. iirc this means they take up less memory. 