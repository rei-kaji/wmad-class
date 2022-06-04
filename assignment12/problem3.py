# - Look around your classroom or your bedroom and come up with 3 classes that you see
# there.
# - For each class define 3 instance Variables
# - For each class define 1 static variable
# - For each class define an accessor and a mutator for each instance variable
# - For each class define 2 instance methods in addition to the accessors and the mutators.
# - For each class define a constructor which initializes all its instance variables.

class Class1:
    def __init__(self, one, two, three):
        self.__one = one
        self.__two = two
        self.__three = three

    @staticmethod
    def staticMtd_class1(one, second):
        one = one

    def setclass1_mutators(self, one, two, three):
        self.__one = one
        self.__two = two
        self.__three = three

    def getclass1_accessors(self):
        return (self.__one, self.__two, self.__three)

    def main():
        exampleClass = Class1(1, 2, 3)

        exampleClass.staticMtd_class1(exampleClass.__one)

        exampleClass.setclass1_mutators(
            exampleClass.__one, exampleClass.__two, exampleClass.__three)

        exampleClass.getclass1_accessors(exampleClass)


class Class2:
    def __init__(self, four, five, six):
        self.__Ffour = four
        self.__five = five
        self.__six = six

    @staticmethod
    def staticMtd_class2():
        return 0

    def setclass2_mutators(self, four, five, six):
        self.__four = four
        self.__five = five
        self.__six = six

    def getclass2_accessors(self):
        return (self.__four, self.__five, self.__six)

    def main():
        exampleClass = Class2(1, 2, 3)

        exampleClass.staticMtd_class1(exampleClass.__one)

        exampleClass.setclass1_mutators(
            exampleClass.__one, exampleClass.__two, exampleClass.__three)

        exampleClass.getclass1_accessors(exampleClass)


class Class3:
    def __init__(self, seven, eight, nine):
        self.__seven = seven
        self.__eight = eight
        self.__nine = nine

    @staticmethod
    def staticMtd_class3():
        return 0

    def setclass3_mutators(self, seven, eight, nine):
        self.__seven = seven
        self.__eight = eight
        self.__nine = nine

    def getclass3_accessors(self):
        return (self.__seven, self.__eight, self.__nine)

    def main():
        exampleClass = Class3(1, 2, 3)

        exampleClass.staticMtd_class1(exampleClass.__one)

        exampleClass.setclass1_mutators(
            exampleClass.__one, exampleClass.__two, exampleClass.__three)

        exampleClass.getclass1_accessors(exampleClass)
