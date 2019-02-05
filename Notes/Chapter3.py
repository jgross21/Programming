# Chapter 3 -- Quiz Games and If Statements

#Basic Comparison

a = 4
b = 5
c = 5
d = 6

if a < b:
    print("a < b")

if d > b:
    print('d > b')

if b >= c:
    print('b >=c')

if a == b:
    print('a equal to b.')

b = 5 # Assignment operator
b == 5 # Comparison operator

if a != b:
    print("a not equal to b.")

# Indentation
if a == 4:
    print('First')
# print('Second') Don't misalign the indent
    print('Third')

# Compound Statement
a = 4
b = 5
c = 5
d = 6

# And Statement
# Both have to be true

if a < b and b <= c:
    print('Both are true')
if a < b <= c: # You can only do this in Python
    print('Both are true')

# OR STATEMENT
# Either or both are true
if d < a or c > a:
    print('One or both are true.')

# Compound if/and
if (d < a or c > a) and b <= c:
    print('All this is true')

# Boolean Variables
# True of false
x = False # Boolean variables have to be capitalized
print(x)

y = 10 > 9
print(y)

# the number zero and False are the only two boolean Falses.
z = 0
if z:
    print('z is true')
z = 'A'
if z:
    print('A is true')

a = 5
b = 5
c = b == a
print(c)

# Else and Else If (elif)

temp = float(input('Whats the temperature in Farenheit? '))

if temp > 90:
    print('It is hot!')
elif temp < 30:
    print('It is cold outside!')
else:
    print('It is not hot outside')

grade = float(input('What is your grade?'))

if grade >= 90:
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 70:
    print('C')
elif grade >= 60:
    print('D')
else:
    print('F')

# Only one IF and one ELSE (else is optional)
# As many ELIF as you want (Order matters. Each has it's own condition)
# if non of the IF or ELIF are true, the Else will always trigger

# Text comparison

password = input('Enter the secret password')

if password == 'parker123':
    print('Correct')
else:
    print('Incorrect')

# Case insensitive text

school = input("Where do you go to school!")
print(school)

if school.upper() == 'PARKER' or school.upper() == 'FRANCIS PARKER'or school.upper() == "FRANCIS W. PARKER" or school.upper() == 'FWP':
    print('Nice! I go there too')
elif school.upper() == "FRANCIS WAYLAND PARKER":
    print('I\'Ve never heard of that place!')
elif school.lower() == "latin":
    print("Oops!")
else:
    print("I hear", school, "Is a fine institution")

# Make a multiple choice question
print('What is the capital of Illinois?\nA. Chicago\nB. Springfield\nC. Carbondale\nD. Evanston\n')

capital = input('Your Answer: ')
if capital.upper() == 'SPRINGIELD' or capital.upper() == 'B' or capital.upper() == 'B. SPRINGFIELD' or capital.upper() == 'B SPRINGFIELD':
    print('Yes. That\'s correct!')
else:
    print('No. The answer is B. Springfield')

# Math Problem

print('What is 17 squared?')

answer = float(input("Your answer: "))

if answer == 17 ** 2:
    print("You are a math genius!!")
else:
    print('Incorrect. The answer is', 17 ** 2)
