##Problem 8
print('Problem 8-------------------------------------------')

name = str(input("number: "))
numberList = []
numberList.append(name)
while any(chr.isalpha() for chr in name) == False:
  if any(chr.isalpha() for chr in name) == False or name != "":
    numberList.append(name)
  name = str(input("number: "))

maxNumber = int(max(numberList))
minNumber = int(min(numberList))
print("Max: %f, Min: %f, Abusolute distance: %d" %(maxNumber, minNumber, maxNumber-minNumber))