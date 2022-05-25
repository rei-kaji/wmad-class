##Problem 9
print('Problem 9-------------------------------------------')

##f1 = 2**x
##f2 = x**5

num1 = 3

f1 = 2 ** num1
f2 = num1 ** 2
print("f1:%f" %f1)
print("f2:%f" %f2)

T = 13

if num1 > 2:
  while num1 < T:
    if f1 < f2:
       print("num1: %f"%num1)
    num1 = num1 + 1
  num1 = 3
  while num1 < 100:
    if num1 >= T:
      if f1 > f2:
        print(num1)
    num1 = num1 + 1