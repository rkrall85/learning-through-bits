import math


#exercise 1 -
#Create a Sphere class that accepts a radius upon instantiation
#and has a volume and surface area method.

class Sphere():

    pi = math.pi #import pi from math library
    def __init__(self, radius=1):
        self.radius = radius

    def surface_area(self):
        return round((4*Sphere.pi *self.radius**2),4)

    def volume(self):
        return round(((4/3)* Sphere.pi * (self.radius**3)),4)


s = Sphere()
print(s.surface_area())
print(s.volume())


#exercise 2
'''
For this exercise we will have several steps.

1. Create a class called GuessingGame.
2. The class doesn't need any user provided arguments for instantiation.
3. In the init method have the class set a self.rand_choice attribute to a random integer between 0-10 (use import random)
4. Now create a method in the class called reset_random that will reset this self.rand_choice attribute
5. Now create a method called guess that uses the input() function to accept a user guess for the random number.
    This method should print out a statement indicating whether or not the user guess was correct.
    Bonus: Add logic that will report back to the user to guess higher or lower next time they call the guess() method.
'''

import random

class GuessingGame():
    def __init__(self):
        self.rand_choice = random.randint(0,10)

    def reset_random(self):
        print("restting the random choice")
        self.rand_choice = random.randint(0,10)

    def guess(self):
        user_guess = int(input("Please guess a number betweon 0 and 10:"))
        if user_guess == self.rand_choice:
            print("You got it")
        else:
            print("keep guessing")
            if user_guess > self.rand_choice:
                print("You are too high")
            else:
                print("You are too low")
            self.guess()



g = GuessingGame()
print(g.rand_choice)
g.reset_random()
g.guess()
