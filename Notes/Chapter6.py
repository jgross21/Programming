# Chapter 6 notes, More Loops
# Learn to master the FOR loop.

# more printing
print('Francis', 'Parker') # Python automatically puts a space in between
print('Francis' + 'Parker') # Smushes them together
print('Python' * 10) # Printing miltiple times
# Python automatically adds '\n' to the end of every print()
print()
print('First', end=' ')
print('Second', end='whatever')
print('Third', end='.')

#1.)
'''
* * * * * * * * * *
'''
# Have this code print using a for loop, and print each
# asterisk individually, rather than just printing ten asterisks with one print statement.
# This can be done in two lines of code, a for loop and a print statement.
for i in range(10):
    print('*', end=' ')
print()

#2.)Write code that will print the following:
'''
* * * * * * * * * *
* * * * *
* * * * * * * * * * * * * * * * * * * *
'''
# This is just like the prior problem, but also printing five and twenty stars.
# Copy and paste from the prior problem, adjusting the for loop as needed.
for i in range(10):
    print('*', end=' ')
print()
for i in range(5):
    print('*', end=' ')
print()
for i in range(20):
    print('*', end=' ')
print()

#3.) Use two for loops, one of them nested inside the other, to print the following 10x10 rectangle:
'''
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
'''
# To start, take a look at Problem 1. The code in Problem 1 generates one line of asterisks.
# It needs to be repeated ten times. Work on this problem for at
# least ten minutes before looking at the answer.
for i in range(10):
    for j in range(10):
        print('*', end='')
    print()


#4.) Use two for loops, one of them nested, to print the following 5x10 rectangle:
'''
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''
# is is a lot like the prior problem.
# Experiment with the ranges on the loops to find exactly what the numbers passed
# to the range function control.
print('4.')
for i in range(10):
    for j in range(5):
        print('*', end=' ')
    print()

# 5.) Use two for loops, one of them nested, to print the following 20x5 rectangle:

# * * * * * * * * * * * * * * * * * * * *
# * * * * * * * * * * * * * * * * * * * *
# * * * * * * * * * * * * * * * * * * * *
# * * * * * * * * * * * * * * * * * * * *
# * * * * * * * * * * * * * * * * * * * *
# Again, like Problem 3 and Problem 4, but with different range values.
print('5.')
for i in range(5):
    for j in range(20):
        print('*', end=' ')
    print()

#6.) Write code that will print the following:
'''
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
'''
#Use two nested loops. Print the first line with a loop, and not with:

# print("0 1 2 3 4 5 6 7 8 9")
#Tip: First, create a loop that prints the first line.
# Then enclose it in another loop that repeats the line 10 times.
# Use either i or j variables for what the program prints.
# This example and the next one helps reinforce what those index variables are doing.

#Work on this problem for at least ten minutes before looking at the answer.
# The process of spending ten minutes working on the answer is far more important than the answer itself.
print('6.')
for i in range(10):
    for j in range(10):
        print(i, end=' ')
    print()

# 7.) Adjust the prior program to print:
# 0 0 0 0 0 0 0 0 0 0
# 1 1 1 1 1 1 1 1 1 1
# 2 2 2 2 2 2 2 2 2 2
# 3 3 3 3 3 3 3 3 3 3
# 4 4 4 4 4 4 4 4 4 4
# 5 5 5 5 5 5 5 5 5 5
# 6 6 6 6 6 6 6 6 6 6
# 7 7 7 7 7 7 7 7 7 7
# 8 8 8 8 8 8 8 8 8 8
# 9 9 9 9 9 9 9 9 9 9
print('7.')
for i in range(10):
    for j in range(10):
        print(j, end=' ')
    print()

# 8.) Write code that will print the following:
# 0
# 0 1
# 0 1 2
# 0 1 2 3
# 0 1 2 3 4
# 0 1 2 3 4 5
# 0 1 2 3 4 5 6
# 0 1 2 3 4 5 6 7
# 0 1 2 3 4 5 6 7 8
# 0 1 2 3 4 5 6 7 8 9
# Tip: This is just problem 6, but the inside loop no longer loops a fixed number of times.
# Don't use range(10), but adjust that range amount.
# After working at least ten minutes on the problem.
print('8.')
for i in range(10):
    for j in range(i+1):
        print(j, end=' ')
    print()

# 9.)Write code that will print the following:
# 0 1 2 3 4 5 6 7 8 9
#   0 1 2 3 4 5 6 7 8
#     0 1 2 3 4 5 6 7
#       0 1 2 3 4 5 6
#         0 1 2 3 4 5
#           0 1 2 3 4
#             0 1 2 3
#               0 1 2
#                 0 1
#                   0
# This one is difficult. Tip: Two loops are needed inside the outer loop that controls each row.
# First, a loop prints spaces, then a loop prints the numbers. Loop both these for each row.
# To start with, try writing just one inside loop that prints:
#
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8
# 0 1 2 3 4 5 6 7
# 0 1 2 3 4 5 6
# 0 1 2 3 4 5
# 0 1 2 3 4
# 0 1 2 3
# 0 1 2
# 0 1
# 0
# Then once that is working, add a loop after the outside loop starts and before the already
# existing inside loop. Use this new loop to print enough spaces to right justify the other loops.

print('9.')
for i in range(10):
    for j in range(i):
        print(' ', end=' ')
    for j in range(10-i):
        print(j, end=' ')
    print()

# Print a multiplication table
print('10.')
for i in range(1, 10):
    for j in range(1, 10):
        if i * j >= 10:
            print(i*j, end=' ')
        if i * j < 10:
            print(i*j, end='  ')
    print()
# 11.)Write code that will print the following:
#                   1
#                 1 2 1
#               1 2 3 2 1
#             1 2 3 4 3 2 1
#           1 2 3 4 5 4 3 2 1
#         1 2 3 4 5 6 5 4 3 2 1
#       1 2 3 4 5 6 7 6 5 4 3 2 1
#     1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
#   1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1
# Tip: first write code to print:
#
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7 8 9
# Then write code to print:
#
# 1
# 1 2 1
# 1 2 3 2 1
# 1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1
# 1 2 3 4 5 6 5 4 3 2 1
# 1 2 3 4 5 6 7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1
#
# Then finish by adding spaces to print the final answer.
print('11.')
for i in range (9):
    for j in range(9-i):
        print(' ', end=' ')
 # Left Half (count up)
    for j in range(1, i+2):
            print(j, end=' ')
# Right Half (count down)
    for j in range (i, 0, -1):
        print(j, end=' ')
    print()
