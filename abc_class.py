from abc import ABC, abstractmethod

class Pets(ABC):

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def seeMouse(self):
        pass


class Dog(Pets):

    @abstractmethod
    def eat(self):
        return "Dog Food"

    @abstractmethod
    def seeMouse(self):
        return "Bark at it"


class Cat(Pets):

    @abstractmethod
    def eat(self):
        return "Cat Food"

    @abstractmethod
    def seeMouse(self):
        return "Eat it"