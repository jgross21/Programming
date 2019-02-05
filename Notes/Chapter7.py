# Chapter 7 - Lists

my_list = [10, 20, 30]  # this list stores 3 integers
print(my_list)

# We can also address individual elements of a list
print(my_list[0])  # Like all things programing, we count from 0
print(my_list[2])  # the 2 here is the "index" of the list.
# print(my_list[3])  # You've gone beyond the capabilities of the end of the list

# You can use the index to change your list
my_list[0] = 15
print(my_list)

grocery_list = ['milk', 'eggs', 'cereal', 'spam', 2]  # Python allows mixing variable types
# You can read through a list with a for loop

for item in grocery_list:
    print(item)

# lists can even contain other lists
my_list2 = [[100, 200], [300, 400], [500, 600, 700]]
# use multiple indices to address individual elements of the list/array
print(my_list2[0][1])  # Prints the second item from the first list
print(my_list2[2][2])  # Print 700

my_list3 = [11, 21, 31, 41, 51]
# There is a second way to iterate through a list. (index variable loop)

# len function returns the length of the list
print(len(my_list3))

for i in range(len(my_list3)):
    print(my_list3[i])

# This method is more complex but more capable

# When we iterate the first way, we are working with a copy
for number in my_list3:
    number += 1
    print(number)

print(my_list3)  # the list didn't change

# When we index the variable, we are working directly with the list
for i in range(len(my_list3)):
    my_list3[i] += 1
    print(my_list3[i])

print(my_list3)

# Tuples
# tuple is a less capable cousin to the list
my_tuple = (255, 255, 0)
print(my_tuple[0])  # You can index tuples the same as a list

# You can iterate, same as a list
for n in my_tuple:
    print(n)

# only difference is that a tuple is immutable (unchanging)
# my_tuple[0] = 0 # This is illegal (TypeError)

# Adding to a list
grocery_list = []

# Append to the list
grocery_list.append('spam')
grocery_list.append('eggs')
print(grocery_list)

# add items in a loop
for i in range (3):
    #  item = input('Enter an item')
    item = 'Spam'
    grocery_list.append(item)
print(grocery_list)

# roll a die 100 times and store it in a list
import random
my_rolls = []

for roll in range(100):
    my_rolls.append(random.randrange(1, 7))
print(my_rolls)
sixes = 0
for roll in my_rolls:
    if roll == 6:
        sixes += 1
print(sixes, 'Sixes')
print(1/6)

# Totaling numbers in a list
my_list = [19, 25, 24, 30, 42]

# Method one - better for this task
total = 0
for number in my_list:
    total += number
print(total)

# Method 2 - Can also be used
total = 0
for i in range (len(my_list)):
    total += my_list[i]

print(total)

# Find the average
print(total / len(my_list))

# Square all of the numbers in the list
for i in range (len(my_list)):
    my_list[i] = my_list[i] ** 2
print(my_list)

# YAHTZEE!
done = False
count = 0
while not done:
    roll_list = []
    count += 1
    for i in range (5):
        roll = random.randrange(1,7)
        roll_list.append(roll)
    if roll_list[0] == roll_list[1] and roll_list[0] == roll_list[2] and roll_list[0] == roll_list[3] and roll_list[0] == roll_list[4]:
        print('YHATZEE! in', count, 'rolls')
        done = True
print(roll_list)

# String Slicing
my_text = 'Francis W. Parker'

# Use the index to adress cahracter
print(my_text[0]) # Prints the "F"
print(my_text[6])  # Prints the "s"

# Accesing characters from the right
print(my_text[-1])  # prints the "r"
print(my_text[-6])  # Prints the "P"

# Access multiple characters
print(my_text[4:7])  # cis
print(my_text[-5:-2])  # ark
print(my_text[:7]) # Francis
print(my_text[-6:]) # Parker

for char in my_text:
    print(char)
