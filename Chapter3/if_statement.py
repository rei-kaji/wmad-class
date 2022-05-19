##Problem 1
hisAge = int(input("How old are you?: "))
if hisAge > 18:
print("You can drive a car!!")
else:
print("You can't drive a car...")


##Problem 2

num = int(input("input numbers\n"))

if num < 10 and num > 0:
  print("Hello " * num)
else:
  print("You put numbers grater than 0 and less than 10!")

##Problem 3

number1 = int(input("Please input number1: "))
number2 = int(input("Please input number2: "))

if number1 > number2:
  print("number1 is the biggest.")
elif number1 == number2:
  print("number1 and number2 is same value.")
else:
  print("number2 is the biggest.")


##Problem 4

num = int(input("input a number\n"))
if num % 6 == 0 and num % 7 == 0:
  print("The number X is divisible by 6 and 7")
else:
  print("The number X is not divisible by 6 and 7")


##Problem 5

num = int(input("input a number\n"))
if num % 6 == 0 or num % 7 == 0:
  print("The number X is divisible by 6 or 7")
else:
  print("The number X is not divisible by 6 and 7")


##Problem 6

a = int(input("input a number A\n"))
b = int(input("input a number B\n"))
x = int(input("input a number X\n"))

if a > b and a < x:
  print(pow(a, x) + pow(x, b))
else:
  print(0)


##Problem 7

gradeNumber = int(input("input your grade: "))

if gradeNumber >= 86 and gradeNumber <= 100:
  print("Your are GREAT (A)")
elif gradeNumber >= 73 and gradeNumber <= 85:
  print("Your are GOOD (B)")
elif gradeNumber >= 67 and gradeNumber <= 72:
  print("Your are AVERAGE (C+)")
elif gradeNumber >= 60 and gradeNumber <= 66:
  print("You need to practice more (C)")
elif gradeNumber >= 50 and gradeNumber <= 59:
  print("You need to try harder (C-)")
elif gradeNumber >= 0 and gradeNumber <= 49:
  print("Unfortunately you failed (F)")
else:
  print("Please write down between 0 to 100.")
