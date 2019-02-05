

'''
CALCULATOR LAB (20pts)

######################
##### BACKGROUND #####
######################

In this lab we'll create three custom calculator programs. To help create these labs check the code in Chapter 1 of the website. 
In particular, the example program at the end of that chapter provides a good template for the code needed in this lab.

Make sure you can write out simple programs like what is assigned in this lab; be able to do it from memory, and on paper. 
These programs follow a very common pattern in computing:

Take in data
Perform calculations
Output data

Programs take in data from sources like databases, 3D models, game controllers, keyboards, and the Internet. They perform calculations and output the result. Sometimes we even do this in a loop thousands of times a second.

It is a good idea to do the calculations separate from the output of the data. While it is possible to do the calculation inside the print statement, it is better to do the calculation, store it in a variable, and then output it later. This way calculations and output aren't mixed together.

When writing programs it is a good idea to use blank lines to separate logical groupings of code. For example, place a blank line between the input statements, the calculation, and the output statement. Also, add comments to your program labeling these sections.

########################
##### INSTRUCTIONS #####
########################

For this lab you will create three short programs. 



1.1 Part A (5pts)
Create a program that asks the user for a temperature in Fahrenheit, and then prints the temperature in Celsius. Search the Internet for the correct calculation. Look at Chapter 1 for the miles-per-gallon example to get an idea of what should be done.

Sample run:

Enter temperature in Fahrenheit: 32
The temperature in Celsius: 0.0
Sample run:

Enter temperature in Fahrenheit: 72
The temperature in Celsius: 22.2222222222

The numbers from this program won't be formatted nicely. That is ok. But if it bothers you, look to Chapter 20 and see how to make your output look great!

Make sure to spell "Celsius" and "Fahrenheit" correctly. When printing an input prompt, use proper grammar and capitalization. 
Don't lose points for being careless.



1.2 Part B (5pts)
Create a new program that will ask the user for the information needed to find the area of a trapezoid, and then print the area:

Sample run:

Area of a trapezoid
Enter the height of the trapezoid: 5
Enter the length of the bottom base: 10
Enter the length of the top base: 7
The area is: 42.5





1.3 Part C (5pts)
Create your own original problem and have the user plug in the variables. If you are not in the mood for anything original, choose an equation from this list:

Area of an ellipse	
Area of an equilateral triangle	
Volume of a cone	
Volume of a sphere	
Area of an arbitrary triangle

When done, check to make certain your variable names begin with a lower case letter, and that you are using blank lines between logical groupings of the code. (Between input, calculations, and output in this case.)  Check your spelling.  Check to make sure your outputs look just like the sample runs shown. (5pts)


# WHEN YOU COMPLETE THIS LAB, DO NOT FORGET TO COMMIT AND PUSH
# YOUR FILE BACK TO THE REPOSITORY.
'''

# Part A (place code here)
f = input("What is your temperature in Fahrenheit?")
f = float(f)

c = 5 / 9 * (f - 32)
c = float(c)
print("That is", c, "degrees celsius")

# PART B
height = input("What is the height of your trapezoid?")
bottom_length = input('What is the bottom base length of your trapezoid?')
top_length = input('What is the top base length of your trapezoid?')

top_length = float(top_length)
bottom_length = float(bottom_length)
height = float(height)

area = 1 / 2 * (top_length + bottom_length) * height
area = float(area)
print('The area of your trapezoid is', area)

# PART C Speed of light comparison calculator
print('You think you are the fastest person on the planet. You think that you might be faster than the speed of light!')
speed = input('Type in your speed in Miles Per Hour to see how you compare to the speed of light! (Just type a number.)')
speed = float(speed)

comparison = (6.706 * (10 ** 8)) - speed
percentage = speed / (6.706 * (10 ** 6))
comparison = float(comparison)
percentage = float(percentage)

print("You are", comparison, "MPH (", percentage, "%) slower than the speed of light")