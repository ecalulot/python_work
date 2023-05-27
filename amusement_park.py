age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")


age = 21
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")
#this is more efficient.

#exercise in using multiple elif blocks p.81

age = 95
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65: 
    price = 40
else:
    price = 20

print(f"Your admission price is ${price}")

#exercie in NOT using the final "else" statement \
#because Python does not require it

age = 65
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your admission price is ${price}")
