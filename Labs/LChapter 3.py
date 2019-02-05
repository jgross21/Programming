'''
CREATE A QUIZ LAB (25pts)

######################
##### BACKGROUND #####
######################

Now is your chance to write your own quiz. Use these quizzes to filter job applicants, test their knowledge, or just plain have a chance to sit on the other side of the desk and make, rather than take, the quiz.

This lab applies the material used in Chapter 3 on using if statements. It also requires a bit of Chapter 1 because the program must calculate a percentage.


########################
##### INSTRUCTIONS #####
########################

This is the list of features your quiz needs to have:

Create your own quiz with five or more questions.

You can ask questions that require:
    a number as an answer (e.g., What is 1+1?)
    text (e.g. What is Harry Potter's last name?)
    a selection (Which of these choices are correct? A, B, or C? True or False?

Your quiz will use at least two DIFFERENT question types from above.

If you have the user enter non-numeric answers, think and cover the different ways a user could enter a correct answer. For example, if the answer is “a”, would “A” also be acceptable? See Section 3.6 for a reminder on how to do this.

Let the user know if he or she gets the question correct. Print a message depending on the user's answer.

You need to keep track of how many questions they get correct.
At the end of the program print the percentage of questions the user gets right (not just 4/5, but 80%)



Keep the following in mind when creating the program:

Variable names should start with a lower case letter. Upper case letters work, but it is not considered proper.

To create a running total of the number correct, create a variable to store this score. Set it to zero. With an if statement, add one to the variable each time the user gets a correct answer. (How do you know if they got it correct? Remember that if you are printing out “correct” then you have already done that part. Just add a line there to add one to the number correct.) If you don't remember how to add one to a variable, go back and review Section 1.5.

Treat true/false questions like multiple choice questions, just compare to “True” or “False.” Don't try to do if a: we'll implement if statements like that later on in the class, but this isn't the place.

Calculate the percentage by using a formula at the end of the game. Don't just add 20% for each question the user gets correct. If you add 20% each time, then you have to change the program 5 places if you add a 6th question. With a formula, you only need 1 change.

To print a blank line so that all the questions don't run into each other, use the following code: print()

Remember the program can print multiple items on one line. This can be useful when printing the user's score at the end.  print("The value of x is", x)

Separate out your code by using blank lines to group sections together. For example, put a blank line between the code for each question.

Sometimes it makes sense to re-use variables. Rather than having a different variable to hold the user's answer for each question, you could reuse the same one.

Use descriptive variable names. x is a terrible variable name. Instead use something like number_correct.

Don't make super-long lines. Chances are you don't need to use \n at all. Just use multiple print statements.

Your final quiz should look similar to the example run below.  It does not have to be exactly like this, but please notice the consistent spacing, style, and feedback provided.


#######################
##### EXAMPLE RUN #####
#######################

Here's an example from my program. Please create your own original questions. I like to be entertained while I check these programs.

Quiz time!

How many books are there in the Harry Potter series? 7
Correct!

What is 3*(2-1)? 3
Correct!

What is 3*2-1? 5
Correct!

Who sings Black Horse and the Cherry Tree?
1. Kelly Clarkson
2. K.T. Tunstall
3. Hillary Duff
4. Bon Jovi
? 2
Correct!

Who is on the front of a one dollar bill
1. George Washington
2. Abraham Lincoln
3. John Adams
4. Thomas Jefferson
? 2
No.

Congratulations, you got 4 answers right.
That is a score of 80.0 percent.
'''

#####################################
# COMPLETE YOUR LAB BELOW THIS LINE #
#            Have Fun!              #
#####################################

print('Time to Test your sports knowledge!')
score = 0


print('\nA. Miami Dolphins')
print('B. Green Bay Packers')
print('C. Los Angeles Rams')
print('D. Kansas City Cheifs')
q1_answer = input('As of the end of week 3 of the 2018 NFL season, which of these teams isn\'t 3-0? ' )
if q1_answer.upper() == 'B' or q1_answer.upper() == 'B. GREEN BAY PACKERS' or q1_answer.upper() == 'GREEN BAY' or q1_answer.upper() == 'PACKERS':
    print('Correct! You\'ve obviously been paying attention this season.')
    score += 1
elif q1_answer.upper() == 'A' or q1_answer.upper() == 'A. MIAMI DOLPHINS' or q1_answer.upper() == 'MIAMI' or q1_answer.upper() == 'DOLPHINS':
    print('Nope. B. Green Bay Packers was the right answer.')
elif q1_answer.upper() == 'C' or q1_answer.upper() == 'C. LOS ANGELES RAMS' or q1_answer.upper() == 'RAMS' or q1_answer.upper() == 'LOS ANGELES':
    print('Nope. B. Green Bay Packers was the right answer.')
elif q1_answer.upper() == 'D' or q1_answer.upper() == 'D. KANSAS CITY CHEIFS' or q1_answer.upper() == 'KANSAS CITY' or q1_answer.upper() == 'CHEIFS':
    print('Nope. B. Green Bay Packers was the right answer.')
else:
    print('Invalid answer. No points for you! The answer is B. Green Bay Packers.')


q2_answer = input('\nHow many different teams have made it to the World Series in the past 10 years (it has to be in between 10 and 20?) ')
if  q2_answer == '14':
    print('Correct. You sure know your baseball!')
    score += 1
elif float(q2_answer) <= 20 and float(q2_answer) >=10:
    print('Nope. The answer is 14.')
else:
    print('Invalid answer. No points for you! The answer is 14.')


print('\nA. Charlotte Hornets')
print('B. Atlanta Hawks')
print('C. Washington Wizards')
print('D. Phoenix Suns')
q3_answer = input('Which of these teams has Dwight Howard not played for? ')
if q3_answer.upper() == 'D. PHOENIX SUNS' or q3_answer.upper() == 'D' or q3_answer.upper() == 'PHOENIX' or q3_answer.upper() == 'SUNS':
    print('Correct! Are you a stalker or something?')
    score += 1
elif q3_answer.upper() == 'A. CHARLOTTE HORNETS' or q3_answer.upper() == 'A' or q3_answer.upper() == 'CHARLOTTE' or q3_answer.upper() == 'HORNETS':
    print('Nope. The answer is D. Phoenix Suns.')
elif q3_answer.upper() == 'B. ATLANTA HAWKS' or q3_answer.upper() == 'B' or q3_answer.upper() == 'ATLANTA' or q3_answer.upper() == 'HAWKS':
    print('Nope. The answer is D. Phoenix Suns.')
elif q3_answer.upper() == 'C. WASHINGTON WIZARDS' or q3_answer.upper() == 'C' or q3_answer.upper() == 'WASHINGTON' or q3_answer.upper() == 'WIZARDS':
    print('Nope. The answer is D. Phoenix Suns.')
else:
    print('Invalid answer. No points for you! The answer is D. Phoenix Suns.')


q4_answer = input('\nWho won the Stanely Cup last year? ')
if q4_answer.upper() == 'THE WASHINGTON CAPITALS' or q4_answer.upper() == 'WASHINGTON CAPITALS' or q4_answer.upper() == 'WASHINGTON' or q4_answer.upper() == 'CAPITALS':
    print('Nice job! I didn\'t know people still watched hockey.')
    score += 1
else:
    print("Nope. The answer is the Washington Capitals.")


print('\nA. Boston')
print('B. Miami')
print('C. Pittsburgh')
print('D. Denver')
q5_answer = input('Which U. S. sports city with at least 3 major (NHL, NFL, MLB, NBA) teams has the same colors throughout all the teams? ')
if q5_answer.upper() == 'C' or q5_answer.upper() == 'C. PITTSBURGH' or q5_answer.upper() == 'PITTSBURGH':
    print('Correct! That was your last chance to rack up some points.')
    score += 1
elif q5_answer.upper() == 'A' or q5_answer.upper() == 'A. BOSTON' or q5_answer.upper() == 'BOSTON':
    print('Nope. The answer is C. Pittsburgh')
elif q5_answer.upper() == 'B' or q5_answer.upper() == 'B. MIAMI' or q5_answer.upper() == 'MIAMI':
    print('Nope. The answer is C. Pittsburgh')
elif q5_answer.upper() == 'D' or q5_answer.upper() == 'D. DENVER' or q5_answer.upper() == 'DENVER':
    print('Nope. The answer is C. Pittsburgh')
else:
    print('Invalid answer. No points for you! The answer is B. Pittsburgh.')

print('Nice job! You got', str(score / 5 * 100) + '%.')

