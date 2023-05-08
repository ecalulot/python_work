# 4-13 Buffet
menu_items = ('chicken wings', 'pizza bites', 'roast beef', 'burgers', 'french fries')
#menu_items[2] = 'hot dogs' #works! program exits because it cannot alter a tuple

menu_items = ('chicken wings', 'pizza bites', 'turkey legs', 'tater tots', 'french fries') # modified menu items
print("\nThe new menu now includes:")
for item in menu_items:
    print(item)

# cannot use .title() or string modifiers, because that alters the tuple. program will exit. 
