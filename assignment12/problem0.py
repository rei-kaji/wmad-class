# Define a class and a static method that receives a string (word) and reverses it and returns it

class returnString:
    @staticmethod
    def reString(word):
        return word[::-1]


print(returnString.reString(input()))
