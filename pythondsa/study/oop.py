class Group:
    age = 26
    s_name = "Paul"


Paul = Group()

Paul.s_name
Paul.age


class Employee:
    employee_id = 0


employee1 = Employee()
employee2 = Employee()

employee1.id = 1000
employee2.id = 1001


class Room:
    length = 0.0
    breadth = 0.0

    def calculate_area(self):
        print("Area of Room = ", self.length * self.breadth)


study_room = Room()


study_room.length = 42.5
study_room.breadth = 30.8


study_room.calculate_area()


# Here the class Name is ROOM, the
# The Attributes are length and breadth
# The Methods is calculated_area()


class Circle:
    pi = 22/7

    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        print("The perimeter of the circle is: ", self.pi * self.radius*2)

    def area(self):
        return ("The area of the circle is: " + str(self.pi * self.radius ** 2))


one = Circle(7)

one.area()
one.perimeter()


# Inheritance

# The newly created class is known as a subclass.
# The existing class from which the child class inherits from is known as a superclass

# We use inheritance when there is an "is a" relationship between the superclass and the subclass


class Animal:

    # name = ""
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("I can eat")


class Dog(Animal):

    def display(self):
        print("My name is ", self.name)


labrador = Dog()

labrador.name = "Jojo"

labrador.eat()

labrador.name
labrador.display()


# super() overrides the superclass's Method
class Animal:

    name = ""

    def eat(self):
        print("I can eat")


class Dog(Animal):
    def eat(self):

        super().eat()

        print("I like to eat bones")


labrador = Dog()

labrador.eat()

# Python Multiple Inheritance


class Mammal:
    def mammal_info(self):
        print("Mammals give direct birth")


class WingedAnimal:
    def winged_animal_info(self):
        print("Winged Animals flap")


class Bat(Mammal, WingedAnimal):
    pass


b = Bat()
b.mammal_info()
b.winged_animal_info()


# Operator Overloading

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)


p1 = Point(1, 2)
p2 = Point(1, 3)

print(p1 + p2)

# ITERATORS

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

lt = iter(l)

n = next(lt)
print(n)
print(n)
print(n)


# EXAMPLE

class PT:

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


numbers = PT(4)


i = iter(numbers)
print(next(i))
print(next(i))
print(next(i))
print(next(i))


# GENERATOR
