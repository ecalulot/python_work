#5-8. Hello Admin
more_users = ['Alice', 'Adam', 'Eve', 'Hecate', 'Admin', 'Bob', 'Zeus']

# more_users = [] # Empty array or list to test 5-9
#5-9. No Users (incorporated into initial code)
if more_users:
    for user in more_users:
        if user == 'Admin':
            print("Hello Admin, would you like to see a status report?\n")
        else:
            print(f"Salutations {user}, thank you for logging in again.\n")
else:
    print("We need to find more users!")

# Initial coding idea for 5-9 
#5-9. No Users
# hello_admins = []
# if hello_admins:
#     for admin in hello_admins:
#         print("Hello admin, would you like to see a status report?\n")
# else:
#     print('We need to find more users!')

#5-10 Checking Usernames
current_users = ['Cronus', 'Rhea', 'Atlas', 'Prometheus', 'Helios']
new_users = ['Oceanus', 'Tethys', 'Phoebe', 'Atlas', 'Theia', 'Selene', 'Rhea']
for user in new_users:
    if user in current_users:
        print(f"The {user} name is unavailable. Enter a new username.\n")
    else:
        print(f"The username {user} is available.\n")

