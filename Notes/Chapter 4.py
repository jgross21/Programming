# Chapter 4 - Loops and Random Numbers

# FOR loop
# Useful for repeating code a specific number of times

for i in range(10):
    print('Hello')
    print('Goodbye')
print('This will print once')

#We can use the index in the loop

for i in range(10):
    print(i)

# We can even adjust the range
for j in range(1, 11):
    print(j)

# We can do steps
for k in range(5, 50, 5):
    print(k)

# We can go backwards and negative
for i in range(5, -5, -3):
    print(i)

# Nested loops

for i in range(10):
    print('i')
    for j in range(10):
        print('j')

# Import time
for h in range(24):
    for m in range(60):
        for s in range(60):
            print(h, m, s)
            # time.sleep(1)

# Running Totals

# add all the numbers up from 1 to 100
total = 0

for i in range(101):
    total +=i
print(total)

# add user input numbers together
total = 0

for i in range(3):
    my_number = int(input('Number: '))
    total += my_number

print (total)

# Random Number

import random
my_number = random.randrange(10)
print(my_number)
# randrage follows same format as range() in a FOR loop

print(random.randrange(10, 21)) # int from 10 to 20

print(random.randrange(0, 51, 5)) # random multiple of 5 from 0 to 50

# Sometimes you need a float
print(random.random()) # random float from 0 approaching 1.000000

print(random.random() * 10) # Random float from 0 to 10.0000

print(random.random() * 5 + 5) # Random float from 5 to 10.000

print(random.random() * 10 - 5) # random float from -5 to 5

# WHILE loop
# Has more flexibility than for loop
# WHILE loop continues until a condition is satisfied
# Looks similar to IF condition

# for loop
for i in range(10):
    print(i)

# While loop
i = 0 # Establish a condition you can check
while i <10:
    print(i) # The location of a print or code is important
    i+=1

for i in range(5, 15):
    print(i)

i = 5
while i < 15:
    print(i)
    i +=1

for i in range (5, -10, -2):
    print(i)

while i > -10:
    print(i)
    i-=2

#The game loop

done = False
while not done:
    answer = input('Do you want to quit?')
    if answer.upper() == 'YES' or answer.upper() == 'Y':
        done = True
    else: print('I hope you are endoying the game.')

print('Game Over')

# The problem with while loops
x = 5
while x > 0:
    print('Hi')

x = 10
while x > 0:
    x += 1

# Roll a die
import random

sixes = 0

for i in range(1000):
    die = random.randrange(1,7)
    print(die)
    if die == 6:
        sixes += 1

print('You rolled', sixes, 'sixes.')

# Roll 2 die added together 100000 times
#Find \# of sixes

import random
sixes = 0
rolls = 100000

for i in range(rolls):
    die1 = random.randrange(1,7)
    die2 = random.randrange(1,7)

    if die1 + die2 == 6:
        sixes += 1

print(round(sixes / rolls * 100, 3), end = '%')

# For problem set

import random
flip = random.randrange(2)

if flip == 1:
    pass
    # do something
else:
    pass
    # do something else