"""
Explanation :
When we define the methods, area and perimeter, in the child class Square, an object of Shape cannot be instantiated, but an object of Square can be.
We allow the user to have a free hand over the definition of the methods while also making sure that the methods are defined.
Note: Methods with @abstractmethod decorators must be defined in the child class.

By using abstract base classes, we can control classes whose objects can or cannot be created.

Abstract methods must be defined in child classes for proper implementation of inheritance.
"""
from abc import ABC, abstractmethod


class Shape(ABC):  # Shape is a child class of ABC
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return (self.length * self.length)

    def perimeter(self):
        return (4 * self.length)


square = Square(4)