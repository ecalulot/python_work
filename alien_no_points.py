alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points']) 
# we do not have a 'points' key so it will return an error (KeyError) because this key does not exist in this specific dictionary

point_value = alien_0.get('points', 'No point value assigned') # this second arguement is optional and will display when the Key does not exist (DNE) as a default value
print(point_value)
