#5-3. Alien Colors #1
alien_color = 'green'

if alien_color == 'green':
    print("You earned 5 points!")

if alien_color == 'yellow':
    None


#5-4. Alien Colors #2
alien_color = 'yellow'

if alien_color == 'green':
    points = 5
#if alien_color != 'green':
#    points = 10
else:
    points = 10


print(f"You've earned {points} points!")


#5-5. Alien Colors #3
alien_color = 'red'

if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
else:
    points = 15

print(f"Congratulations player you've earned {points}!")


#5-6. Stages of Life. 
age = 12

if age < 2:
    stage = 'baby'
elif age >=2 and age < 4:
    stage = 'toddler'
elif age >=4 and age < 13:
    stage = 'kid'
elif age >= 13 and age < 20:
    stage = 'teenager'
elif age >= 20 and age < 65:
    stage = 'adult'
else:
    stage = 'elder'

print(f"You are a {stage}.")


#5-7. Favorite Fruit. 
favorite_fruits = ['strawberries', 'black berries', 'cherries', 'bananas']

if 'bananas' in favorite_fruits:
    print("Bananas are staple for breakfast.")
if 'cherries' in favorite_fruits:
    print("I really enjoy cherries!")
if 'black berries' in favorite_fruits:
    print("I like black berries in my yogurt!")
if 'strawberries' in favorite_fruits:
    print("I like strawberries drenched in heavy cream!")
if 'tomatoes' not in favorite_fruits:
    print("I dislike tomatoes.")


