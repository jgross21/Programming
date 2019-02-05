# Chapter 9 - FUNctions

# Why use fxns:
# Make code repeatable
# Organize your code

def hi(name):
    print('Hello', name)

# def means define
# name of fxn is hi. Follows snake_case naming rules
# parentheses contain the parameters of the fxn

# this is the call to the fxn
hi('Mr. Lee')
hi('computer')

import math

def volume_cylinder(height, radius):
    """
    Calculate the volume of a cylinder
    :param height: float height of cylinder
    :param radius: float radius of cylinder
    :return:
    """
    volume = math.pi * radius ** 2 * height
    # print(volume)
    return volume

volume_cylinder(5, 3)

# returning values from the fxn
# use return statement to send values bacl to your program

print(volume_cylinder(5, 3))
vol = volume_cylinder(3, 8) # assign and capture the value
print(vol)

# Scope - the most misunderstood thing in programming

# scope is where a variable (or object) alive.
# (Where can it be used and where can it be seen

x = 5 # this is a global variable (all the way to the left)
# global variables can be seen everywhere.

def f1():
    x = 10 # I am a local variable. I exist only inside the fxn.

f1()
print(x)



y = 21

def f2():
    # y += 1
    print(y)

f2()

# if we want to change something with a function, we must return and capture
z = 10

def f3(z):
    z += 1
    return z

z = f3(z)
print(z)

# Fxns can call fxns
def f4():
    print('Hello')
    f5()

def f5():
    print('Goodbye')
    # f4() This would go infinitely


f4()

# Returning multiple items

def double_triple(n):
    double = n * 2
    triple = n * 3
    return double # You only get one return, then it exits the fxn
    return triple

print(double_triple(5))

def double_triple(n):
    double = n * 2
    triple = n * 3
    return double, triple # Returns a tuple

print(double_triple(5))

double, triple = double_triple(5) # Python specific "special power"
print(double)
print(triple)

def total_avg(my_list):
    total = 0
    for num in my_list:
        total += num
    average = total / len(my_list)
    return total, average

my_list = [4, 5, 6, 3, 5]
total, average = total_avg(my_list)
print(total)
print(average)