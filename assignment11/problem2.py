# problem 2
# Create a Student class and initialize it with coursesGrades, name and id number. Make methods to :
# Display - It should display name and id number of the student.
# AddCourseGrade – It adds the grades of the courses to the list of courses.
# getAverage – it calculates the average (GPA) of the student based on the grades of the student.
# No need to write test class or main function for this.

class Student:
    def __init__(self, name, courseGrade, id):
        self.name = name
        self.courseGrade = courseGrade
        self.id = id

    def display(self):
        print("Student name is %s" % self.name)
        print("Student id is %d" % self.id)

    def addCourseGrade(self, newGrade):
        self.courseGrade.append(newGrade)

    def getAverage(self):
        print("Average for %s is: %.2f" %
              (self.name, sum(self.courseGrade)/len(self.courseGrade)))


rei = Student("Rei", [20, 20, 15, 20], 11111)
rei.display()
rei.getAverage()
