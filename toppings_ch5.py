#pg 82. using multiple "if" statements to test multiple cases. \
#we do this because an "if-elif" only test one case and exits \
#out of the "if-elif" block. 
#mulitple "if" used to test for multiple "True" statements. 

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

