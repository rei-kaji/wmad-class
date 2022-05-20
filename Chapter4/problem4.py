print('Problem4-------------------------------------------')

num = int(input('number:'))
sum = 0
count = 0

while(num != 0):
  sum += num
  num = int(input('number:'))
  count += 1
    
print(sum)
print(sum/count)