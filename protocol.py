from typing import Protocol

class Pets(Protocol):

    def eat(self):
        pass

    def seeMouse(self):
        pass


class Dog:

    def eat(self):
        return "Dog Food"

    def seeMouse(self):
        return "Bark at it"


class Cat:

    def eat(self):
        return "Cat Food"

    def seeMouse(self):
        return "Eat it"