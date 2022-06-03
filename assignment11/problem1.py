# problem 1
# Create a Temprature class. Make two class/static methods :
# convertFahrenheit - It will take Celsius and will convert and print it into Fahrenheit.
# convertCelsius - It will take Fahrenheit and will convert it into Celsius.
# Write a test class for this one and test it (Look at problem 3 and 4 for example)

class Temprature:
    @staticmethod
    def convertFahrenheit(celsiusDegree):
        return (celsiusDegree*9/5)+32

    @staticmethod
    def convertCelsius(fahrenheitDegree):
        return ((fahrenheitDegree)-32)*5/9


print(Temprature.convertFahrenheit(5))
print(Temprature.convertCelsius(10))
