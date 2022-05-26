print('Problem3-1-------------------------------------------')
i = 1
num = int(input('number:'))
if num <= 30:
  print("You have to input over 30")
  num = int(input('number:'))
else:
  while i <= num:
    i += 1
    if i % 6 == 0 and i % 7 == 0:
      print("divisible by 6 or 7:")
      print(i) 