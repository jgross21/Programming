'''
Chapter 3 Problem Set (16pts)

Instructions:  For each of the following, enter your answer below the numbered problem.

For questions asking you to fix code, just change the code to make it work as intended.

Make sure your file executes before you submit it!

If a single problem is not working properly, please comment it out of your code. If a question is commented out, it will receive partial credit.
Non working or broken code will not receive any credit for that problem.

'''

#################################
#  Problem 1 (1pt)
#  Fix the following code. Look closely, it is a common syntax error.

temperature = float(input("Temperature: "))
if temperature > 90:
     print("It is hot outside.")

#################################
#  Problem 2 (3pts)
#  Write code that will take in a number from the user and print to tell the user if their number is positive, negative, or zero.  Your output should print exactly like the example runs below.

'''
Example runs:
Enter a number: 5.3
Your number is positive

Enter a number: 0
Your number is zero
'''
number = float(input('Enter a number: '))
if number < 0:
    print('Your number is negative')
elif number == 0:
    print('Your number is zero')
else:
    print('Your number is positive')


#################################
#  Problem 3 (3pts)
#  Write a python program which takes a number from the user, and prints \"Success\" if it is both greater than -10 AND less than or equal to 10.  If the number is outside this range, print Failure.")

'''
Example Run:
 -5.2
Success
'''
number = float(input('Enter a number greater than -10 and less than or equal to 10:'))
if number > -10 and number <= 10:
    print('Success')
else:
    print('Failure')

##################################
#  Problem 4 (2pts)
#  Fix the following code.  There are three things wrong.

x = float(input("Enter a number:"))
if x == 3:
     print("You entered 3")

###################################
#  Problem 5 (2pts)
#  There are several things wrong with this code. Fix it.

answer = input("What is the Name of Cardi B\'s 2018 album? ")
if answer.upper() == "INVASION OF PRIVACY":
     print("Correct!")
else:
      print("Incorrect! It is titled \"Invasion of Privacy\"")

#####################################
#  Problem 6 (2pts)
#Look at the code below.  Before running the code, make a prediction of what each line will print. Put your prediction in a comment to the right of the print statement.  I am not grading you for your prediction, I simply want you to think about the code. Next, run the code and see if you are correct. One of the lines creates an error.  Fix it. Make sure you understand the reason for any incorrect guesses.  One produces an error.  Comment that one out.

print("3" == "3") #put guesses here # True
print(" 3" == "3") # and here # False
print(3 < 3) # etc # False
print(3 < 4) # True
print(3 < 10) # True
print("3" < "4") # False
print("3" < "10") # False
print((2 == 2) == "True") # False
print((2 == 2) == True ) # True


#####################################
#  Problem 7 (3pt)
#  Fix the following code which has multiple errors.

print("Welcome to Oregon Trail!")
print("A. Banker\nB. Carpenter\nC. Farmer")
ip = input("What is your occupation")
money = 100

if ip.upper() == "A":
     occupation = "Banker"
     money += 100
elif ip.upper() == "B":
     occupation = "Carpenter"
     money += 50
else:
     occupation = "Farmer"

print("You are a", occupation, "with", money, "dollars")
