import random
print('Welcome to Outlaw!')
print('You have stolen a horse and are trying to make your way across the plains to your hideout.')
print('The sheriff and his posse are chasing you down!')
print('Survive your desert trek and out run the sheriff.')

done = False
miles_traveled = 0
thirst = 0
horse_tiredness = 0
miles_sheriff_traveled = -20
canteen_drinks = 5

while done == False:
    print('\nChoose Carefully!')
    print('A. Drink from your canteen.')
    print('B. Ahead moderate speed for an hour.')
    print('C. Ahead full speed for an hour.')
    print('D. Take a 4 hour nap.')
    print('E. Status check.')
    print('Q. Quit.')
    choice = input('Make your choice... ')
    if choice.upper() == 'Q':
        done = True
    elif choice.upper() == 'E':
        print('\n\nMiles traveled:', miles_traveled)
        print('Drinks in canteen:', canteen_drinks)
        print('The sheriff is', miles_traveled - miles_sheriff_traveled, 'miles behind you.')
    elif choice.upper() == 'D':
        horse_tiredness = 0
        print('\n\nThe horse is happy.')
        miles_sheriff_traveled += random.randrange(3, 11)
    elif choice.upper() == 'C':
        recent_miles_traveled = random.randrange(3, 7)
        miles_traveled += recent_miles_traveled
        print('\n\nYou traveled', recent_miles_traveled, 'miles.')
        thirst += random.randrange(1, 3)
        horse_tiredness += random.randrange(1, 4)
        miles_sheriff_traveled += random.randrange(2, 5)
    elif choice.upper() == 'B':
        recent_miles_traveled = random.randrange(1, 5)
        miles_traveled += recent_miles_traveled
        print('\n\nYou traveled', recent_miles_traveled, 'miles.')
        thirst += random.randrange(0, 2)
        horse_tiredness += random.randrange(1, 3)
        miles_sheriff_traveled += random.randrange(2, 5)
    elif choice.upper() == 'A':
        if canteen_drinks < 0:
            print('\n\nYou are out of drinks.')
        else:
            canteen_drinks -= 1
            miles_sheriff_traveled += random.randrange(1, 3)
            thirst = 0
            print('\n\nYour thirst is quenched')
    if thirst > 5:
        print('\n\nYou are thirsty.')
    if thirst > 7:
        print('\n\nYou died of thirst.')
        done = True
    if horse_tiredness > 6:
        print('\n\nYour horse is getting tired.')
    if horse_tiredness > 9:
        print('\n\nYour horse is dead.')
        done = True
    if miles_sheriff_traveled >= miles_traveled:
        print('\n\nThe sherrif has caught up.')
        done = True
    elif miles_sheriff_traveled >= miles_traveled - 10:
        print('\n\nThe police are close!')
    if miles_traveled >= 100:
        print('\n\nYou have reached your hideout and evaded the cops!')
        done = True
    oasis_odds = random.randrange(1, 26)
    if oasis_odds == 1:
        print('\n\nYou found an oasis!')

        print('\n\nA. Stay at the oasis.')
        print('B. Leave the oasis.')
        oasis_choice = input('Your choice... ')
        if oasis_choice.upper() == 'A':
            canteen_drinks = 5
            thirst = 0
            horse_tiredness = 0
            miles_sheriff_traveled += random.randrange(2, 6)
    heart_failure_odds = random.randrange(1, 101)
    if heart_failure_odds == 1:
        print('\n\nYou had heart failure and suddenly passed away.')
        done = True
if done == True:
    print('\n\nGame over')









