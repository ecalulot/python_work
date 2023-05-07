dinner_invite_list = ['abraham lincoln', 'alexander the great', 'Martin Luther King Jr']
print(f"\nHello {dinner_invite_list[0].title()}! I'd like to invite you to dinner.")
print(f"\nGood evening {dinner_invite_list[1].title()}! I want to invite you lunch.")
print(f"\nHello Sir! Mr. {dinner_invite_list[-1]}, may I buy you a coffee and interview you?")

#print(f"\nUnfortunately {dinner_invite_list[-2].title()} cannot make our lunch meeting.")
missed_attendance = dinner_invite_list.pop(-2)
#print(missed_attendance)
print(f"\nUnfortunately {missed_attendance.title()} cannot break away for lunch.")

dinner_invite_list.insert(1, 'elon musk')
print(f"\nThe new invite list is: {dinner_invite_list}. Welcome {dinner_invite_list[1].title()}!")

print(f"\nHey {dinner_invite_list[1].title()}! Let me buy you lunch.")

#3-6. More Guests exercise
print("Hey folks! Looks like I was able to get a larger table. Let's do a breakfast brunch!")

dinner_invite_list.insert(0, 'henry ford')
dinner_invite_list.insert(1, 'Aristotle')
dinner_invite_list.append('marcus aurelius')
print(f"\nThe new dinner list is: {dinner_invite_list}.")
print("The new number of dinner guests are:", len(dinner_invite_list))

print(f"\nHello! I want to formally invite you all to brunch. {dinner_invite_list[0].title()}, {dinner_invite_list[1].title()}, and {dinner_invite_list[2].title()} please welcome the new folks. May I introduce you to {dinner_invite_list[3].title()}, {dinner_invite_list[4].title()}, and {dinner_invite_list[-1].title()}.")

#3-7. Shrinking Guest List exercise
print("\nUnfortunately we were late with the reservations and I can only invite two of you. Which two shall it be?")
print(dinner_invite_list)

uninvite_list = dinner_invite_list.pop(0)
print(f"\nI'm sorry {uninvite_list.title()}. Your invite has been rescinded.")

#print(f"\nThe uninvited list is {uninvite_list.title()}.")
uninvite_list = dinner_invite_list.pop(1)
print(f"\nI'm sorry {uninvite_list.title()}, you too have been uninvited.") 

uninvite_list = dinner_invite_list.pop(-2)
print(f"\nI'm sorry {uninvite_list.title()}, you too have been uninvited.")

uninvite_list = dinner_invite_list.pop(0)
print(f"\nI'm sorry {uninvite_list.title()}, you too have been uninvited.")

#print(f"\nThe uninvited list is {uninvite_list.title()}.")
print(f"\nThe remaining diners are: {dinner_invite_list}.")
print("The remaining number of guests are: " + str(len(dinner_invite_list)))
print(f"\nCongratulations {dinner_invite_list[0].title()}. We're having dinner.")
print(f"\nHope you like lamb {dinner_invite_list[1].title()}. That's what we're having for dinner.")

del dinner_invite_list[0]
print(f"\nThe remaining diners are: {dinner_invite_list}.")
del dinner_invite_list[0]
print(f"\nThe list should now be empty. Just to verify: {dinner_invite_list}")