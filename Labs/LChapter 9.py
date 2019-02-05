# 1
def min3(a, b, c):
    minim = 0
    if a <= b and a <= c:
        minim = a
    if b <= a and b <= c:
        minim = b
    if c <= a and c <= b:
        minim = c
    return minim


print(min3(4, 7, 5))
print(min3(4, 5, 5))
print(min3(4, 4, 4))
print(min3(-2, -6, -100))
print(min3("Z", "B", "A"))

# 2
def box(h, w):
    for i in range (h):
        for f in range (w):
            print('*', end='')
        print()


box(7,5)  # Print a box 7 high, 5 across
print()   # Blank line
box(3,2)  # Print a box 3 high, 2 across
print()   # Blank line
box(3,10) # Print a box 3 high, 10 across

# 3
def find(my_list, key):
    for i in range (len(my_list)):
        if my_list[i] == key:
            print('Found', key, 'at position', i)


my_list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]

find(my_list, 12)
find(my_list, 91)
find(my_list, 80)


# 4.1
import random
def create_list(size):
    new_list = []
    for i in range(size):
        new = random.randrange(1, 7)
        new_list.append(new)
    return new_list

my_list = create_list(5)
print(my_list)

# 4.2
def count_list(list, number):
    amount = 0
    for i in range(len(list)):
        if list[i] == number:
            amount += 1
    return amount

count = count_list([1,2,3,3,3,4,2,1],3)
print(count)

# 4.3
def average_list(list):
    total = 0
    for number in list:
        total += number
    return (total / len(list))

avg = average_list([1,2,3])
print(avg)

# 4.4
l4 = create_list(10000)
print(count_list(l4, 1))
print(count_list(l4, 2))
print(count_list(l4, 3))
print(count_list(l4, 4))
print(count_list(l4, 5))
print(count_list(l4, 6))

av = average_list(l4)
print(av)