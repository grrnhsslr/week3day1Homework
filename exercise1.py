# Exercise 1 - Write a Python class for an Animal that has a name and energy attributes.
# The animal class should also have methods for eat, sleep, and play that will take in an integer
# and increase/decrease the energy of the animal with a formatted print statement
# # Example 1
# # buddy = Animal('Buddy', 10)
# # buddy.play(5) -> "Buddy is playing for 5 minutes. His energy is now 5"
# # buddy.sleep(10) -> "Buddy is sleeping for 10 minutes. His energy is now 15"

class Animal:
    def __init__(self, hunger, sleep, energy):
        self.hunger = hunger
        self.sleep = sleep
        self.energy = energy

    def eat(self, hunger):
        increase = hunger * 5
        self.hunger += increase
        print(f'your animal has eaten, their hunger is: {self.hunger}')
        if increase <= 0:
            print(f"Sorry, your animal starved, their hunger level was {self.hunger}")

    def rest(self, sleep):
        decrease = sleep * 5
        self.sleep += decrease
        print(f'your animal has slept, their energy level is {self.sleep}')
        if decrease <= 0:
            print(f"Sorry, your animal needs to rest, their energy level was {self.sleep}")

    def play(self, energy):
        decrease1 = energy // 10
        self.energy -= decrease1
        print(f'your animal has played, their energy level is {self.energy}')
        if decrease1 <= 0:
            print(f"Sorry, your animal needs to be resting their energy is {self.energy}")


animal1 = Animal(10, 10, 10)
animal2 = Animal(10, 10, 10)

animal1.play(10)
animal1.rest(10)
animal1.eat(10)
animal2.play(10)
animal2.rest(10)
animal2.eat(10)
