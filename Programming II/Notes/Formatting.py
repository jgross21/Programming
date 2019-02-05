# Formatting
import math
import random

# area of circle calculator

radius = 5
area = math.pi * radius ** 2
print(area)

# round function
print(round(area, 2)) # Round(number, precision)

for i in range(20):
    print(round(random.random(), 2))

# format method is more useful

# index: spaceholder + justification + sign + width + commas + precision + datatype + notation

print('my formatted number is {:.2f}'.format(3.14159)) # Formats for rounding precision
print('my formatted number is {:10}'.format(3.14159)) # Formats for justification (number of spaces) to the right
print('my formatted number is {:10.3f}'.format(3.14159)) # Formats for justification and precision
print('my formatted number is {:<10}.'.format(3.14159)) # Formats for justification to the left
print('my formatted number is {:^10}.'.format(3.14159)) # Formats for center alingment

for i in range(20):
    print('${:<5.2f}'.format(random.random()))

for i in range(20):
    print('{:.2e}'.format(random.random())) # Scientific notation

for i in range(20):
    print('${:8,}'.format(random.randrange(1000000)))