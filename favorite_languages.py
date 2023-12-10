favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python', # adding a , (comma) after the last entry is just good practice
    } # this closing dictionary brace '}' is indented - PEP8 standard? 


language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

favorite_languages['edward']


for name, language in favorite_languages.items():
    print(f"\n{name.title()}'s favorite language is {language.title()}.")


for name in favorite_languages.keys():
    print(name.title())
# looping through the keys is default behavior in Python
# can easily be done with the following code

for name in favorite_languages: 
    print(f"{name}")
    print(name) # this works the same just "more efficient"

