#Problem2
#Define and implement a function which does linear search. This function receives two input parameters, one is a list of integers and the other one is a number to search for. The function returns -1 if the number (the second parameter of the function) does not exist in the list or return the index of the number if the number exists in the list.
#If there are more than one occurrence of the number, the function will return the index of the first occurrence


list = []

numbersInput = int(input("Digit how many numbers: "))

def search(list, num):
  i = 0
  count = 0
  size = len(list)
  while i <= size:
    i = i + 1
    count = count + 1
    if num in list:
      print("FOUND")
      print("INDEX: ", count)
      break
    else:
      print("NOT FOUND")
      return -1
  
def listInput(num):
  i = 0
  while i != num:
    i = i + 1
    number = int(input("Number: "))
    list.append(number)
  
  number2 = int(input("Number to search: "))
  search(list, number2)

listInput(numbersInput)