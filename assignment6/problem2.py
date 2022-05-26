#Problem2
# -	 Design and implement a function which receives a number as its input parameter and checks whether the number is a prime number or not. If it is a prime number the algorithm returns true and if not the algorithm will return false. 
# -	Prime number: https://simple.wikipedia.org/wiki/Prime_number

response = False

num = int(input("Number:"))

if num > 1:
  for i in range(2, num):
    if(num % i) == 0:
      response = True
      break

if response:
  print(num, "isn't prime")
else:
  print(num, "is prime")
