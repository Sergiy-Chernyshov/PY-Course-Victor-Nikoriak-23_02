# task1

class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(f"Hello, my name is {self.firstname} {self.lastname} and I’m {self.age} years old")

person1 = Person("Carl", "Johnson", 26)
person1.talk()

person2 = Person("Alice", "Smith", 30)
person2.talk()

print ("\n")

#Task2
class Dog:
    age_factor = 7

    def __init__(self, age):
        self.age = age

    def human_age(self):
        return self.age * Dog.age_factor


dog1 = Dog(3)
print(dog1.human_age())

dog2 = Dog(5)
print(dog2.human_age())

print ("\n")

#Task3

CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.current_index = 0

    def first_channel(self):
        self.current_index = 0
        return self.channels[self.current_index]

    def last_channel(self):
        self.current_index = len(self.channels) - 1
        return self.channels[self.current_index]

    def turn_channel(self, N):
        if 1 <= N <= len(self.channels):
            self.current_index = N - 1
            return self.channels[self.current_index]
        return "No such channel"

    def next_channel(self):
        self.current_index = (self.current_index + 1) % len(self.channels)
        return self.channels[self.current_index]

    def previous_channel(self):
        self.current_index = (self.current_index - 1) % len(self.channels)
        return self.channels[self.current_index]

    def current_channel(self):
        return self.channels[self.current_index]

    def exists(self, arg):
        if isinstance(arg, int):
            return "Yes" if 1 <= arg <= len(self.channels) else "No"
        elif isinstance(arg, str):
            return "Yes" if arg in self.channels else "No"
        else:
            return "No"

controller = TVController(CHANNELS)

print(controller.first_channel())
print(controller.last_channel())
print(controller.turn_channel(1))
print(controller.next_channel())
print(controller.previous_channel())
print(controller.current_channel())
print(controller.exists(4))
print(controller.exists("BBC"))