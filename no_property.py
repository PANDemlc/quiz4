class Rental:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    def get_price(self):
        return self._price
    
    def set_price(self, value):
        if value < 0:
            raise ValueError("Can't be negative")
        self._price = value

    def printValue(self):
        return f"Property: {self.name} is worth ${self._price}"
    
house1 = Rental("Mansion", 14000000)
print(house1.printValue())

house1._price = 1
print(house1.printValue())