'''
Chapter 04 Problem Set (21pts)")

Instructions:  For each of the following, enter your answer below the numbered problem.
Ensure the code runs properly without errors. Make sure your file executes before you submit it!

If a single problem is not working properly, please comment it out of your code. If a question is commented out, it will receive partial credit.
Non working or broken code will not receive any credit for that problem.
'''

#################################
# Problem 1 (2pts)
#Write a Python program that will use a for loop to print your name 5 times on separate lines, and then the word \"Done\" on the last line.

'''
Sample Run:

Francis
Francis////////////////////////////////////
Francis
Francis
Francis
Done
'''
for i in range(5):
    print('Jonah')
print('Done')
#################################
#  Problem 2 (2pts)
#Write a Python program that will use a for loop to print your first name 3 times and then your last name 3 times.  Repeat this pattern (3 first followed by 3 lasts) 10 times.


'''
Sample Run

Francis
Francis 
Francis
Parker 
Parker
Parker
(Above is repeated 10 times)
'''
for i in range (10):
    for i in range(3):
        print("Jonah")
    for i in range(3):
        print('Gross')

#################################
#  Problem 3 (Multiples of seven - 2pts)
#  Write a Python program that will use a for loop to print multiples of seven from 21 to 70. (70 must be included)
for i in range(21, 71, 7):
    print(i)


#################################
#  Problem 4 (Countdown - 2pts)
#  Write a Python program that will use a while loop to count from 10 down to 1. Then print the words \"Blast off!\" Remember, this time we will use a WHILE loop, don't use a FOR loop.
i = 10
while 10 >= i >= 1:
    print(i)
    i -= 1
print('Blast off!')

#################################
#  Problem 5 (Random ints - 2pts)
#  Write a program that prints a random integer from 1 to 10. Put it in a loop so that it prints a different random integer 10 times


'''
Sample Run
4
2
5
9
10
1
8
4
3
3
'''
import random
for i in range(10):
    x = random.randrange(1, 10)
    print(x)


###########################
#  Problem 6 (Random floats - 2pts)
#  Write a program that prints a random floating point number somewhere between 1 and 10 (inclusive).
#  Do not make the mistake of generating a random number from 0 to 10 instead of 1 to 10.
#  Put it in a loop to print a different random float 10 times.

'''
Sample Run
2.987862719820445
6.870129734673759
4.434092587298322
9.929302003474453
6.0609415060503515
8.428599151662887
6.715550409049674
1.083673547723635
7.917120042736795
8.982349679748726
'''
import random
for i in range(10):
    print(random.random() * 9 + 1)

#################################
#  Problem 7 (Coin Flipper - 4pts)

'''  
Make a Coin flipper: 
    * Start by creating a program that will print a random 0 or 1.
    * Then, instead of 0 or 1, make it print heads or tails.
    * Add a loop so that the program does this 100 times.
    * Print the total number of heads flipped, and the number of tails.

If done properly, you will likely have around half heads and half tails.
'''
import random

heads = 0
tails = 0

for i in range(100):
    x = random.randrange(0,2)
    if x == 0:
        print('heads')
        heads += 1
    elif x == 1:
        print('tails')
        tails += 1

print('You had', heads, 'heads and', tails, 'tails.')


#################################
#  Problem 8 (Rock Paper Scissors - 5pts)
'''
Write a program that plays rock, paper, scissors:

    * Start by creating a program that randomly prints 0, 1, or 2.
    * Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list, as shown in the chapter.  This random selection will be the computer's choice.
    * Add to the program so it first asks the user their choice.(It might be easier if you have them enter a number instead of rock, paper, or scissors. See sample run)
    * Add conditional statement to figure out who wins and print back the result to the user.
'''

'''
Sample run:

Welcome to rock paper scissors:

Enter your choice (0 for rock, 1 for paper, or 2 for scissors): 1
Player chooses paper.
Computer chooses rock.

Congratulations, you win.
'''

import random

print('Welcome to rock paper scissors:')
user_choice = input('\n Enter your choice (0 for rock, 1 for paper, or 2 for scissors): ')

if user_choice == '0':
    print('Player chooses rock.')
elif user_choice == '1':
    print('Player chooses paper.')
elif user_choice == '2':
    print('Player chooses scissors.')
else:
    print('Invalid response.')

x = random.randrange(0, 3)
if x == 0:
    print('Computer chooses rock.')
elif x == 1:
    print('Computer chooses paper')
elif x == 2:
    print('Computer chooses scissors')

if user_choice == '0' and x == 0:
    print('\nOops! You tied.')
elif user_choice == '0' and x == 1:
    print('\nDarnit! You lose.')
elif user_choice == '0' and x == 2:
    print('\nCongradulations, you win!')
elif user_choice == '1' and x == 1:
    print('\nOops! You tied.')
elif user_choice == '2' and x == 2:
    print('\nOops! You tied.')
elif user_choice == '1'and x == 0:
    print('\nCongradulations, you win!')
elif user_choice == '2' and x == 1:
    print('\nCongradulations, you win!')
elif user_choice == '1' and x == 2:
    print('\nDarnit! You lose.')
elif user_choice == '2' and x == 0:
    print('\nDarnit! You lose.')