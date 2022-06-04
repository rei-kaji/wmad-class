# - Write a main function and inside the function write a test scenario for each of the above
# classes. Your test scenario should include creating one or two instances of each class, call
# some of its accessors and mutators and its instance variables

class Student:
    _studentIDCounter = 1000

    def __init__(self, firstName, lastName, address, age):
        self._listOfCourse = []
        self._firstName = firstName
        self._lastName = lastName
        self._address = address
        self._age = age
        Student._studentIDCounter = Student._studentIDCounter + 1
        self._studentID = Student._studentIDCounter

    def _getFirstName(self):
        return self._firstName

    def _getLastName(self):
        return self._lastName

    def _getAddress(self):
        return self._address

    def _getAge(self):
        return self._age

    def addCourseGrades(self, grade):
        self._listOfCourse.append(grade)

    def calculateAverage(self):
        if len(self._listOfCourse) > 0:
            sum = 0
            for item in self._listOfCourse:
                sum = sum + item
                average = sum / len(self._listOfCourse)
                return average
            else:
                return

    def getStudentID(self):
        return self._studentID

    def printStudentProfile(self):
        print("============================")
        print(self._firstName)
        print(self._lastName)
        print(self._age)
        print(self._address)
        print(self.getStudentID())
        print(self.calculateAverage())


class TestStudent:
    def test(self):
        student1 = Student("Peter", "Mak", "Vancouver", "29")
        student2 = Student("David", "Cameron", "Burnaby", "30")
        student1.printStudentProfile()
        student2.printStudentProfile()
        student1.addCourseGrades(80)
        student1.addCourseGrades(73)
        student1.addCourseGrades(85)
        student2.addCourseGrades(48)
        student2.addCourseGrades(90)
        student1.printStudentProfile()
        student2.printStudentProfile()


def main():
    testStudent = TestStudent()
    testStudent.test()


main()
