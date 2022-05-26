# Problem 1
# Write a function which take a list of number as an input parameter 
# and find the second maximum of the list. The second maximum is a number 
# which is bigger than or equal to all numbers but smaller than the maximum of the list.

list = []

numbersInput = int(input("Digit how many numbers: "))

def checkBigger(list):
  newList = sorted(list)
  print("Second bigger:")
  print(newList[-2])
  
def listInput(num):
  i = 0
  while i != num:
    i = i + 1
    number = int(input("Number: "))
    list.append(number)
  checkBigger(list)

listInput(numbersInput)
