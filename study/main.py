class Parrot:

    name = ""
    age = 0


parrot1 = Parrot()
parrot1.name = "Blue"
parrot1.age = 10


parrot2 = Parrot()
parrot2.name = "segun"
parrot2.age = 12


print(f"{parrot1.name} is {parrot1.age} years old")
print(f"{parrot2.name} is {parrot2.age} years old")


# Inheritance

class Animal:

    def eat(self):
        print("I can eat!")

    def sleep(self):
        print("I can sleep!")


class Dog(Animal):

    def bark(self):
        print("I can bark! Woof Woof!!")


dog1 = Dog()


dog1.eat()
dog1.sleep()
dog1.bark()

# Encapsulation


class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print(f"Selling Price: {self.__maxprice}")

    def setMaxPrice(self, price):
        self.__maxprice = price


c = Computer()

c.sell()

c.__maxprice = 1000
c.sell()

c.setMaxPrice(1000)
c.sell()


# PolyMorphism

class Polygon:
    def render(self):
        print("Rendenring Polygon...")


class Square(Polygon):
    def render(self):
        print("Rendering Square...")


class Circle(Polygon):
    def render(self):
        print("Rendering Circle...")


s1 = Square()
s1.render()

s2 = Circle()
s2.render()
