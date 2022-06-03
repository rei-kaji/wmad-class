# problem 3
# Define a class with a static method that receives a list of numbers and calculate the average of the numbers.
# Add another static method the above class that receives a string and returns the reverse of it.

class Average:
    @staticmethod
    def getAverage(list):
        return sum(list)/len(list)

    @staticmethod
    def reverse(value):
        return value[::-1]


print(Average.getAverage([1, 2, 3, 4]))
print(Average.reverse("ReiKajiwara"))
