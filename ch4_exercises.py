# 4-3 Counting to Twenty
#simple_numbers = list(range(1, 21))
#print(simple_numbers)
#for numbers in range(1, 21):
#    print(numbers)

# 4-4 One Million
#un_mil = list(range(1, 10 ** 6)) 
#print(un_mil)
# Q: can it do the 10 ** 6 as the stop value?
# A: yes, it can peform the calculation and returned 999999 as the final value - correct

#another_mil = list(range(10 ** 6)) 
# Q: can it do this? 
# A: yes, it performed the same, except it started at 0
# print(another_mil)

# how do we determine which is less computationally intensive? going for efficiency. 

# 4-5 Summing a Million
#one_mil = list(range(1, ((10 ** 6)+1)))
#print(one_mil)
#print("\nThe lowest number in the list is:", min(one_mil))
#print("\nThe max number on the list is:", max(one_mil))
#print("\nThe sum from one to one million is:", sum(one_mil))

# 4-5 Try another way
#one_million = list(range(1, 1000001))
#uno_mil = range(1, 1000001)
#print(min(uno_mil))
#print(max(uno_mil))
#print(sum(uno_mil))


# All my previous calculations are correct. The mathematical formula for this:
# N * (N + 1)/2 
# where N = 10^6

# 4-6 Odd Numbers
for odds in range(1, 21, 2):
    print(odds)

# 4-7 Threes
threes_multiple = []
for threes in range(3, 31, 3):
    threes_multiple.append(threes)

print(threes_multiple)

# 4-8 Cubes - actually did 4-8 in a list comprehension version, which is 4-9
cubes = [num ** 3 for num in range(1,11)]
print(cubes)

# 4-9 Cubes - doing this the original method asked for in 4-8
for kube in range(1, 11):
    print(kube ** 3)

more_cubes = list(range(1, 11))
print(more_cubes)
for value in more_cubes:
    print(value ** 3)

