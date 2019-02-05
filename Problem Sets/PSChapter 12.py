# Chapter 12 Problem Set (21pts)

# 1 Write code to create an INSTANCE of the class below.
#  Use DOT NOTATION to change its three attributes to those of your own pet or one you know and love: (2pts)

class Dog():
    def __init__(self):
        self.age = 0
        self.name = ""
        self.weight = 0


dog = Dog()
dog.name = 'Winnie'
dog.age = 1.5
dog.weight = 45



# 2 Write code to create an INSTANCE of this class
#  Set the name and email attribute by passing the values to the constructor method
#  (that means adding additional parameters to the init method): (2pts)

class Person():
    def __init__(self, name, email):
        self.name = name
        self.email = email
        print(name, email)


Person('Jonah', 'Jgross@fwparker.org')


# 3 For the code below, create a CLASS with attributes for color, name, and breed.
#  The instance code below will use that class to create a green parrot named Sunny. (2pts)

class Bird():
    def __init__(self, color, name, animal):
        self.color = color
        self.name = name
        self.animal = animal
        print('I am', str(name) + ',', 'a', color, str(animal) + '.')


myBird = Bird("green", "Sunny", "Parrot")


# 4 The following code has three errors.  Fix the code. (3pts)

class Person():
    def __init__(self, name):
        self.name = name
        self.money = 0


nancy = Person("Nancy")
nancy.money = 100  # set nancy's money to 100 dollars

# 6 With the following items, identify two unique "has-a" relationships, and two unique"is-a" relationships from any item pairs.  (2pts)
#  Ask if you don't understand this problem.  It requires no code.
'''
     * Checking account
     * Person
     * Customer
     * Withdraw
     * Bank Account
     * SSN
     * Transaction
     * Address
     * Deposit
     * Balance
'''
# Person has a checking account
# Person has an adress.
# Customer is a person
# Checking account is a bank account.

# 7. This problem has several parts that are all contained in a single program. Make sure that the program satisfies the requirements for each part.

# part A. Write code that defines a class named Animal: (3pts)
class Animal():
    def __init__(self, name):
        self.name = name
        print('An animal has been born.')
    def eat(self):
        print('Munch Munch.')
    def makeNoise(self):
        print('Grr says', str(self.name) + '.')

'''
* Add an attribute for the animal name.
* Add a constructor for the Animal class that prints ''An animal has been born.''
* Add an eat() method for Animal that prints ''Munch munch.''
* Add a makeNoise() method for Animal that prints ''Grrr says [animal name].''
'''

# part B. Create a class named Cat: (3pts)
class Cat(Animal):
    def __init__(self):
        print('A cat has been born.')
    def makeNoise(self):
        print('Meow says', str(self.name) + '.')

'''
* Make Animal the parent.
* A makeNoise() method for Cat that prints ``Meow says [animal name].''
* A constructor for Cat that prints ``A cat has been born.'' and it calls the parent constructor.
'''

# part C.  Create a class named Dog: (3pts)
class Dog(Animal):
    def __init__(self):
        print('A dog has been born.')
    def makeNoise(self):
        print('Bark says', str(self.name) + '.')

'''
* Make Animal the parent.
* A makeNoise() method for Dog that prints ``Bark says [animal name].''
* A constructor for Dog that prints ``A dog has been born.'' and it calls the parent constructor.
'''

# part D.  Make a single program with the following: (3pts)
class Animal():
    def __init__(self):
        self.name = ''
        print('An animal has been born.')
    def eat(self):
        print('Munch Munch.')
    def makeNoise(self):
        print('Grr says', str(self.name) + '.')


class Cat(Animal):
    def __init__(self):
        print('A cat has been born.')
    def makeNoise(self):
        print('Meow says', str(self.name) + '.')

class Dog(Animal):
    def __init__(self):
        print('A dog has been born.')
    def makeNoise(self):
        print('Bark says', str(self.name) + '.')

''' 
* Code that creates a cat, two dogs, and an animal.
* Set the name for each animal.
* Code that calls eat() and makeNoise() for each animal. (Don't forget this part.)
'''

print()
tom = Cat()
tom.name = 'Tom'
tom.makeNoise()
tom.eat()
print()

winnie = Dog()
winnie.name = 'Winnie'
winnie.makeNoise()
winnie.eat()
print()

ivy = Dog()
ivy.name = 'Ivy'
ivy.makeNoise()
ivy.eat()
print()

pumpkin = Animal()
pumpkin.name = 'Pumpkin'
pumpkin.makeNoise()
pumpkin.eat()