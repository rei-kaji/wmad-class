# Problem3
# -	 Design and implement a function which receives a number as its input parameter and checks whether the number is a prime number or not. If it is a prime number the algorithm returns true and if not the algorithm will return false. 
# -	Prime number: https://simple.wikipedia.org/wiki/Prime_number

def prime_function(num):  
  response = False

  biggerNumber = num +1
  
  if biggerNumber > 1:
    while response != True:
      for i in range(2, biggerNumber):
          if (biggerNumber % i) == 0:
            response = True
            break
      biggerNumber = biggerNumber +1
          
  print(biggerNumber)

  
num = int(input("Number:"))
prime_function(num)