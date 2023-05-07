places_to_go = ['japan', 'santorini', 'new zealand', 'italy', 'sweden', 'bora bora', 'thailand']
print(places_to_go)
print(sorted(places_to_go))
print(f"\nThe original list is: {places_to_go}.")
print("\nThe destination list in reverse order:")
print(sorted(places_to_go, reverse=True))

print("\nBut the original list is still intact.")
print(places_to_go)

places_to_go.reverse()
print(f"\nThe list in reverse using revese() method: {places_to_go}.")
#print(places_to_go)
places_to_go.reverse()
print(f"\nThe reverse list back to its original order: {places_to_go}.")

places_to_go.sort()
print(f"\nThe list in alphabetical order using the sort() method: {places_to_go}.")

places_to_go.sort(reverse=True)
print(f"\nThe list in reverse order using 'sort(reverse=True)' method: {places_to_go}.")
