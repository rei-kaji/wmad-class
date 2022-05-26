print('Problem3-3-------------------------------------------')
i = 1
num = int(input('number:'))
if num <= 30:
  print("You have to input over 30")
  num = int(input('number:'))
else:
  while i <= num:
    i += 1
    if i % 5 != 0:
      print("not divisible by 5:")
      print(i)