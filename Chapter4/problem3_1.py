print('Problem3-1-------------------------------------------')
i = 1
num = int(input('number:'))
if num <= 30:
  print("You have to input over 30")
  num = int(input('number:'))
else:
  while i <= num:
    i += 1
    if i % 3 == 0 and i % 2 == 0:
      print("divisible by 2 and 3:")
      print(i) 
