# problem 4
# Define and design a class that represents the time. (hours and minutes, AM and PM).
# Also add an instance method called addMinutes, that receives a number which represent a number (that represents a minute)
# and adds the time to current time the instance is showing. For instance if the object represent 3:31 pm then you call addMinutes(30)
# then the new time is going to be 3:31 + 30 (minute) = 4:01 PM.


class Time:
    def __init__(self, hour, minute, AMorPM):
        self.hour = hour
        self.minute = minute
        self.AMorPM = AMorPM

    def addMinutes(self, minutes):
        if minutes >= 60:
            print("Minutes should be less than 60")
            return
        elif self.minute + minutes >= 60:
            self.minute = (self.minute + minutes) % 60

            if self.hour == 11:
                self.hour = 0
                if self.AMorPM == "AM":
                    self.AMorPM = "PM"
                else:
                    self.AMorPM = "AM"
            else:
                self.hour = self.hour + 1
        else:
            self.minute = self.minute + minutes

    def displayTime(self):
        print("Time is %2.d:%2.d %s" % (self.hour, self.minute, self.AMorPM))


time = Time(11, 40, "PM")
time.displayTime()
time.addMinutes(50)
time.displayTime()
