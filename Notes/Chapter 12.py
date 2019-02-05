# Chapter 12 - Classes

import random
# Class is a classification of an object

# vocab
# Method - a function that belongs to a class.
# Constructor method - __init__(self), runs when object is created.
# Attributes - variables that belong to a class.
# Object/instance- an example of a class object.
# Self - reference to the object in question. Used inside the class.

class Player():
    def __init__(self):
        self.money = 1500
        self.token = 'no token'
        self.space = 0
        print('A new player has been added to the game.')
    def print_money(self):
        print(self.token, 'has', '$' + str(self.money))
    def roll_dice(self):
        self.die1 = random.randrange(1, 7)
        self.die2 = random.randrange(1, 7)
        self.my_roll = self.die1 + self.die2
        print(self.token, 'rolled a', self.die1, 'and', self.die2, '=', self.my_roll)
    def move(self, number):
        self.space += number
        print(self.token, 'moved', number, 'spaces to space', self.space)
    def pay_rent(self, amount, other):
        self.money -= amount
        other.money += amount
        print(self.token, 'paid', other.token, '$' + str(amount))

player1 = Player() # object called player1. Instance of player class.
print(player1) # Object exists in local memory
print(player1.money)  # Access using dot notation
player1.money += 200
print('player 1 now has','$' + str(player1.money))
player1.token = 'Moneybag'
# print(player1.token, 'has', '$' + str(player1.money))
player1.print_money()
player1.roll_dice()
player1.move(player1.my_roll)
print()

player2 = Player()
player2.token = 'Racecar'
# print(player2.token, 'has', '$' + str(player2.money))
player2.print_money()
player2.roll_dice()
player2.move(player2.my_roll)
player2.pay_rent(103, player1)
player2.print_money()
player1.print_money()

'''
player3 = player2 # This is wrong. Use player3 = Player()
player3.token = 'Dog'
print(player2.token)
print(player2, player3)
'''
# Vocab
# Parent - General example of the class, more broad.
# Child - More specific example of the parent. Parent plus extra stuff
# Inheritance - the child class has all attributes/ methods of a parent plus more/

class Character():
    def __init__(self, name):
        print(name, 'is born' )
        self.health = 100
        self.strength = 10
        self.gold = 50
        self.name = name
    def attack(self, damage, other):
        other.health -= damage
        print(self.name, 'attacked', other.name, 'for', damage, 'health points.')
    def print_health(self):
        print(self.name, 'has', self.health, 'health points remaining.')

class Vampire(Character):
    def __init__(self, name):
        super().__init__(name)
        print('A vampire named', name, 'is born.')
        self.form = 'Human'
    def change_form(self):
        if self.form == 'human':
            self.form = 'bat'
        else:
            self.form = 'human'
        print(self.name, 'changed into a', self.form)


hero = Character('Hero')

enemy = Character('Lane')
# enemy.name = 'Lane'

hero.attack(10, enemy)

vampire1 = Vampire('Bob')
vampire1.print_health()
vampire1.change_form()
vampire1.change_form()

