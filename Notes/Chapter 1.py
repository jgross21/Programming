# Chapter 1 Notes

#Single line comment -- not part of code

print("hello World") #Print a string, strings have quotes
print(3 + 4) #Can print numbers or do arithmatic
print('Francis', 'Parker') #separated by space with a Return after
print('High Score:', 1000+200)

#Escape Codes (Backslash)
print("I want to print a quote\", but it doesn't work")
# Backslash means that the next character is not code

#tab and new line (\t and \n)
print("Jonah\tLiam\tGross")
print("First\nSecond\nThird")
print("First\n\tSecond\n\t\tThird")

#Assignment Operators (=) only way to change a variable
x = 10 #the variable x is assigned a value of 10
y = 5 #variable name on left, value on right
print(x)
print(x, y)
print(x+y)

z = x + y
print(z)
print('z = x + y')

#Increment

z = z + 1 #You can't do this in math, but you can in programming
print(z)

#shorthand increment
z += 2
print(z)

#Variables
X = 1
x = 2
print(X)
print(x)    #python is case specific

# variable naming rules
# - Should be all lower case
# - Should use snake_case  (use underscore instead of space)
# - cannot use special characters (underscore is okay)
# - Cannot start with a number (can still use them later on)
# - cannot use spaces

eight_ball = 8 #Works
#8ball = 8 doesn't work

tax_percent = 0.09
#tax% = 0.09

#Constants are in ALL CAPS
PI = 3.141592638
RED = (255, 0, 0) # We'll learn this later

# Math Operators (+, -, /, *, //, **, %)
x = 5
# y = 5x # This is illegal
y = 5 * x
# y = 5(3 + x) # Also illegal
y = 5 * (3 + x)
z = 3 + 4 - 2 * 8 / 2 # PEMDAS rules apply

# Floor division (//)
# divides two numbers and chops off the remainder.
a = 14 // 4
print(a)

# Exponent (**)
b = 3 **2 # Square
print(b)
c = 5 ** .5 # square root
print(c)

# Modulus (%)
# Returns the remainder from division
d = 7 % 3
print(d)
e = 13 % 7
print(e)
f = 8 % 2
print(f)

# Spacing
x = 5 + 2 * (4 / 3) ** 2
x = 5+2*(4/3)**2
# Means the same thing but single spaces are easier to read

# Math Library
import math #import statement pulls in a library from the external libraries
print(math.pi)
print(math.cos(math.pi))

# Make a calculator
r = 5
area = math.pi * r ** 2
print(area)

# User Input
input("Press Return to Quit") # Input funtion, takes in one parameter

# We can also grab the value of the input
name = input("What is your name? ")
print("Hello", name, ", my name is Python.")

x = input("Enter a number: ")
x = float(x) # Float is a decimal
print(x ** 2)

# Improve area of circle
r = input("Enter the radius of the circle: ")
area = math.pi * float(r) ** 2
print("The area of the circle is:", area)