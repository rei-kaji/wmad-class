# -	Design and implement a function which takes 2 operands (numbers) and one operator (plus, minus, multiplication and division) and applies the operator on the operands and returns and prints the result. 
# Note: If operand1 is a non-zero number and the operand2 is zero, then the program should not perform the division operand and should print the operation is not possible because one number is zero (this is only for division operator) and return -1. 

n = int(input("Please input number1: "))
n2 = int(input("Please input number2: "))
operator = input("Please input operator: ")

if(n <= 0 or n2 <= 0):
  print("not possible because one number is zero. -1")
else:
  if(operator == "*"):
    result = n * n2
    print(result)
  elif(operator == "+"):
    result = n + n2
    print(result)
  elif(operator == "-"):
    result = n - n2
    print(result)
  elif(operator == "/"):
    result = n / n2
    print(result)
  elif(operator == "%"):
    result = n % n2
    print(result)
  

