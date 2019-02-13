import random

my_list = ['Abe', 'Bev', 'Cam', 'Dan', 'Eve', 'Flo', 'Gus']
my_numbers = [5, 9, 12, 6, 3, -3, 4]

print(my_list[1]) # Single index
print(my_list[-1]) # Negative index
print(my_list[:4]) # from the first to the fourth
print(my_list[-3:]) # last fourth

my_copy = my_list # NO!!
print(my_copy)
my_copy.append('Hal')
print(my_copy)
print(my_list)

my_copy = my_list[:] # NO!!
print(my_copy)
my_copy.append('Ike')
print(my_copy)
print(my_list)


# 2d list
my_2dlist = [['Abe', 8], ['Bev', 5], ['Cam', 11]]
print(my_2dlist[2][0]) # Cam

# if in
if 'Cam' in my_list:
    print('Cam is in there')

# list functions
print(len(my_list)) # Length of list(not incliding index
print(min(my_numbers)) # smallest number
print(min(my_list)) # smallest by alphabetical
print(max(my_numbers))
print(sum(my_numbers))

# list methods

# find the index of an item
print(my_list.index('Cam'))
my_list.append('Cam')
print(my_list.index('Cam')) # only finds the first one

my_list.count('Cam') # How many times does it appear
my_list.count('Abe')

my_list.append('Deb')
print(my_list)
my_list.sort() # orders/alphabetizes the list
print(my_list)
my_numbers.sort()
print(my_numbers)

my_list.reverse() # reverses the order
print(my_list)

# Important! pop method
my_list.pop() # Pops one off the end of a list
print(my_list)
customer = my_list.pop() # pops and then returns the item
print(customer)
print(my_list)
customer = my_list.pop(3) # pick which one you want to grab
print(customer)
print(my_list)

del my_list[3]
print(my_list)

# Concatenation
first = 'Francis'
last = 'Parker'
print(first + last)

print(my_list + my_numbers)

# Iterating through lists
# make a list of numbers 0-9
my_list = []
for i in range(10):
    my_list.append(i)
print(my_list)

# print every item in my_list
# index variable loop
for i in range (len(my_list)):
    my_list[i] += 1
    print(my_list[i])
print(my_list)

print()
# For each loop (uses a copy of the item)
for number in my_list:
    number += 1
    print(number)

# make a 2d list that is 10 x 10 [[0, 1], [0,2], [0, 3]... [9, 9]]
my_list = []
for i in range (10):
    for j in range (10):
        my_list.append([i, j])
print(my_list)

# print each pair
for pair in my_list:
    print(pair)

# print each x value
for pair in my_list:
    print(pair[0])

# LIST COMPREHENTIONS (show old way then new way)
# [returned_item for iterator list/range filter]
# Syntactic Sugar

# make a list from 0 to 100
my_list = []
for i in range (101):
    my_list.append(i)
print(my_list)

my_list = [x for x in range(101)]
print(my_list)

# make a list of 0 to 100 squared
my_list = []
for i in range(101):
    my_list.append(i ** 2)
print(my_list)

my_list = [x ** 2 for x in range(101)]
print(my_list)

# make a list of 0 to 100 squared but filter out the odd numbers
my_list = []
for i in range(101):
    if i % 2 == 0:
        my_list.append(i ** 2)
print(my_list)

my_list = [x ** 2 for x in range(101) if x ** 2 % 2 == 0]
print(my_list)

# roll a single die 100 times and add it to a list
my_list = []
for i in range(100):
    my_list.append(random.randrange(1, 7))
print(my_list)

my_list = [random.randrange(1, 7) for x in range(100)]
print(my_list)

# roll die two die 100 times and add it to a list
my_list = [[random.randrange(1, 7), random.randrange(1, 7)]for x in range(100)]
print(my_list)

# roll two die 100 times, only show the doubles

my_list = [x for x in my_list if x[0] == x[1]]
print(my_list)

# all at once
my_list = [x for x in [[random.randrange(1, 7), random.randrange(1, 7)]for x in range(100)] if x[0] == x[1]]
print(my_list)

# working with strings
first = 'Francis'
last = 'Parker'
print(first[0])
first = first.upper()
print(first)
print(first + last)
print(last[-2:])
if 'F' in first:
    print('Yeah')
for char in last:
    print(char)

