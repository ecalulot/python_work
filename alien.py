alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} pointss!")

# adding new key-value pairs
print(alien_0)
alien_0['x_position'] = 0 
alien_0['y_position'] = 25
alien_0['speed'] = 'medium'
print(alien_0)
print(alien_0['y_position'])
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")
print(f"Original position: {alien_0['x_position']}")

# p. 95 speed and position of alien

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"The new alien position: {alien_0['x_position']}")

# how to remove a key and with it its value in a dictionary
del alien_0['points'] 