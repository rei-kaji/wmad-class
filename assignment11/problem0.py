# problem 0
# Create a Cricle class and initialize it with radius.
# Make two instance methods getArea and getCircumference inside this class.
# Implement the methods.
# No need to write test class or main function for this.
from math import pi


class Circle:

    def __init__(self, radius):
        self._radius = radius

    def getArea(self):
        return pi * self._radius * self._radius

    def getCircumference(self):
        return 2*pi*self._radius


def main():
    area = Circle(5)
    print(area.getArea())
    print(area.getCircumference())


main()
