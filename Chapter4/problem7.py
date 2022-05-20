##Problem 7
print('Problem 7-------------------------------------------')

name = str(input("your name?: "))

while name.isdigit() == False:
  print(name.upper())
  name = str(input("your name?: "))
  
print("Finish!!")



##Problem 7
print('Problem 7-------------------------------------------')

name = str(input("your name?: "))

while any(chr.isdigit() for chr in name) == False:
  print(name.upper())
  name = str(input("your name?: "))
  
print("Finish!!")