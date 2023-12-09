# 6-1 Person (p. 98)
person = {'first_name': 'Dante', 'last_name': 'Alighieri', 'city': 'Florence'}
print(person['first_name'])
print(person['last_name'])
print(person['city'])


# 6-2 Favorite Numbers
fav_nums = {'douglas': 42, 
            'abraham': 1849, 
            'herald': 1124, 
            'pyramid': 88,
            'robins': 100,
            }

for name, numb in fav_nums.items():
    print(f"{name.title()}'s favorite number is {numb}.")


# 6-3 Glossary
glossary = {'for': 'a key word for looping',
            'while': 'another way to loop',
            'enumerate': 'a built-in method to get index and value in a list',
            'list': 'also called an array in other languages',
            'dictionary': 'also a hash table, makes sense if you know what a hash is',
            }

for k_word, meaning in glossary.items():
    print(f"{k_word.capitalize()}: {meaning}.\n")