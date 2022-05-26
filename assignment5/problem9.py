##Problem 9
print('Problem 9-------------------------------------------')

##f1 = 2**x
##f2 = x**5

num = 3

#f1 = 2 ** num
#f2 = num ** 2


if num > 2:
    f1 = pow(2, num)
    f2 = pow(num, 5)
    while num <= 100 and f1 < f2: 
      if f2 < f1:
        print(num)
        num += 1
      else:
        num += 1
      f1 = pow(2, num)
      f2 = pow(num, 5)
      #print("num%d" %(num))
      #print("%f" %f1)
      #print("%f" %f2)
print("num%d" %(num))