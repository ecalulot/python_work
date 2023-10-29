print('# 5-8. Hello Admin and # 5-9 No Users\n')
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

print('# 5-10 Checking Usernames\n')
current_users = ['Cronus', 'Rhea', 'Atlas', 'Prometheus', 'Helios']
new_users = ['Oceanus', 'Tethys', 'Phoebe', 'Atlas', 'Theia', 'Selene', 
             'Rhea', 'HELIOS', 'cronUS']

# test for case insensitivity
icase_current_users = [] # initialize an empty array
for cur_user in current_users:
    # lowercase each user and add to the empty list array
    icase_current_users.append(cur_user.lower()) 
#print(icase_current_users)

for user in new_users:
    if user.lower() in icase_current_users:
        print(f"The {user} name is unavailable. Enter a new username.\n")
    else:
        print(f"The username {user} is available.\n")

print('# 5-11 Ordinal Numbers\n')
ord_nums = list(range(1, 10))
for num in ord_nums:
    if num == 1:
        print('1st')
    elif num == 2:
        print(str(num) + 'nd')
    elif num == 3:
        print('3rd')
    else:
        print(str(num) + 'th')
