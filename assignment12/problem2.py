# Problem2
# Define and design a class with a static method called convert,
# which receives a positive number and a base number and converts the number to the given base and returns it as a string.
# For instance: convert (9, 2) returns 1001

class returnConvert:
    @staticmethod
    def convert(positive, base):
        if base == 2:
            return bin(positive)
        elif base == 8:
            return oct(positive)
        elif base == 16:
            return hex(positive)


print(returnConvert.convert(11, 2))
print(returnConvert.convert(11, 8))
print(returnConvert.convert(11, 16))
