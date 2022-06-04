# Problem1
# Design a class that represents a histogram like the one in the image below.
# The X axis represents the days of the week and then the Y axis represents the sales.
# Add an instance method which receives a day and return the corresponding Y value.

class Histogram:
    def __init__(self, dayAndValue):
        self.dayAndValue = dayAndValue

    def returnYValue(self, day):
        return self.dayAndValue[day]


histogram = Histogram({"Monday": "51k", "Thuesday": "56k", "Wednesday": "56k",
                      "Thursday": "54k", "Friday": "53k", "Saturday": "41k", "Sunday": "37k"})

print(histogram.returnYValue("Monday"))
