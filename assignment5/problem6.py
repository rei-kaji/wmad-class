##Problem 6
print('Problem 6-------------------------------------------')
reversed = 0
num = int(input("number:"))

while num % 10 == 0:
  print("CANT BE DIVISIBLE OF 10!")
  num = int(input("number:"))

while num != 0:
  digit = num % 10
  reversed = reversed * 10 + digit
  num //= 10

print("Reversed = %d" %reversed)