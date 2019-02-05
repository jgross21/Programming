# Chapter 09 Problem Set - FUNCTIONS are FUN! (18pts)
'''
Section 1 of 3...
For the code below, GIVE A PREDICTION for what it will output. Then run
the code and state if your prediction was accurate or not. If your prediction
is incorrect, make a quick note of the difference.  More importantly, make sure you understand how and why it differed.

If you don't know why the code runs the way it does, watch the video at the
end of the chapter assignment (on the website) for an explanation. NOTE: The problems contained on this worksheet are numbered differently than the video.
'''
# This section is worth 3 points.

print("Problem # 1")
'''
I think this will print...
3

It actually printed...
3
'''


def f1(x):
    print(x)


y = 3
f1(y)

print("Problem # 2")
'''
I think this will print...
4

It actually printed...
4
3
'''


def f2(x):
    x = x + 1
    print(x)


y = 3
f2(y)
print(y)

print("Problem # 3")
'''
I think this will print...
4
3
It actually printed...
4
3
'''


def f3(x):
    x = x + 1
    print(x)


x = 3
f3(x)
print(x)

print("Problem # 4")
'''
I think this will print...
4
Error
It actually printed...
4
Error
'''


def f4(x):
    z = x + 1
    print(z)


x = 3
f4(x)
print(z)

print("Problem # 5")
'''
I think this will print...
x = 10
x = 11
x = 10

It actually printed...
x= 10
x= 11
x= 10

'''


def foo(x):
    x = x + 1
    print("x=", x)


x = 10
print("x=", x)
foo(x)
print("x=", x)

print("Problem # 6")
'''
I think this will print...
f start
g start
h
g end
h
f end

It actually printed...
f start
g start
h
g end
h
f end
'''


def f():
    print("f start")
    g()
    h()
    print("f end")


def g():
    print("g start")
    h()
    print("g end")


def h():
    print("h")


f()

print("Problem # 7")
'''
I think this will print...
x= 10
spam has been called
x= 10
It actually printed...
x= 10
spam has been called
x= 10
'''


def spam():
    x = 3
    print("spam has been called")


x = 10
print("x=", x)
spam()
print("x=", x)

'''
Section 2 of 3
This next section involves finding the mistakes in the code. If you can't
find the mistake, check out the video on the website for the answer and 
explanation of the mistakes.  Again, our problems will not match exactly the ones from the video.

This section is worth 7 points.
'''
print("Problem # 8")


# Correct the following code: (Don't let it print out the word ``None'')
# Only change the function.  Do not change the call to the function.

def find_sum(a, b, c):
    sum = a + b + c
    return sum


print(find_sum(10, 11, 12))

print("Problem # 9")


# Correct the following code: (x should increase by one, but it doesn't.)
# The correct solution involves capturing and use the returned value from the function.

def increase(x):
    return x + 1


x = 10
print("x is", x, " I will now increase x.")
print("x is now", increase(x))

print("Problem # 10")


# Correct the following code:

def print_hello():
    print("Hello")


print_hello()

print("Problem #11")


# Correct the following code:

def count_to_ten():
    for i in range(1, 11):
        print(i)


count_to_ten()

print("Problem #12")


# Correct the following code:

def sum_list(list):
    sum = 0
    for i in list:
        sum += i
    return sum

list = [45, 2, 10, -5, 100]
print(sum_list(list))

print("Problem #13 (2pts)")


# Correct the following code: (This almost reverses the string. What is wrong?)

def reverse(text):
    result = ""
    text_length = len(text)
    for i in range(1, text_length + 1):
        result = result + text[i * -1]
    return result


text = "Programming is the coolest thing ever."
print(reverse(text))

'''
Section 3 of 3...
(8 pts) For this section, write code that satisfies the following:
'''

print("Problem # 14 (2pts)")
# Write AND call a function that will take two numbers as parameters (not as an input from the user)
# and print their product (multiply them).


def multiplier (a, b):
    product = a*b
    return product


print(multiplier(5, 6))

print("Problem # 15 (2pts)")
# Write AND call a function that takes in two parameters.
# The first parameter will be a string named phrase.
# The second parameter will be a number named count.
# Print phrase to the screen count times.

# (e.g., the function takes in "Hello" and 5, then prints "Hello" five times.)


def f15 (phrase, count):
    for i in range (count):
        print(phrase)
    return ''


print(f15('Jonah Liam', 5))

print("Problem # 16 (2pts)")
# Write AND call a function that takes in a number, and returns the square of that number.
# Note, this function should RETURN the answer, not print it out.
def sqrt (n):
    root = n ** .5
    return root


print(sqrt(5))

print("Problem # 17 (2pts)")
# Write AND call  a function that takes three numbers as parameters,
# and returns the centrifugal force.
# The formula for centrifugal force is: F=mrv^2
# (F is centrifugal force, m is mass, r is radius, and v is angular velocity.)
def f17 (m, r, v):
    f = m * r * (v ** 2)
    return f


print(f17(2, 2, 2))