# Write a python program with the following description:
# Define a class called MyCustomList.
# The class has an instance variable called myList which is a list of integers.
# Define the following instance methods for the class:
# addItem: It has an input of type int and it add the number to the list if this number already does not exist in the list. If it exits it will ignore it.
# calculateSum: It has no input and will return the sum of all numbers in the list.
# calculateMax: it has no input and will return the maximum number of the list.
# printList: It has no input but print the current content of the list to the out.
# Remember to define a constructor for this class.
# Define another class called Test MyCustomList. This class has a static method called testMyCustomList. This method is used to contain a test scenario for the MyCustomeList.
# In another python file, define a main function and use the TestClass to test the MyCustomeList class.

class MyCustomList:

    def __init__(self, items):

        self.myList = items

    def addItem(self, item):

        if item not in self.myList:

            self.myList.append(item)

    def calculateSum(self):

        return sum(self.myList)

    def calculateMax(self):

        return max(self.myList)

    def printList(self):

        print(self.myList)


class TestMyCustomList:

    @staticmethod
    def testMyCustomList():

        customList = MyCustomList([5, 22, 45])

        print("Initial List is :")

        customList.printList()

        print("Trying to add already exist item as 22")

        customList.addItem(22)

        print("List after trying to add 22")


test = TestMyCustomList()
print(test.testMyCustomList())
