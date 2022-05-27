# Write a python function which receives 2 mathematical equations and adds these two equations and prints and retunes the result. The mathematical equations that are inputs of this function have the following format / specifications:
# o   The maximum degree of the equation is 10.
# o   The equation can have only 2 variables: X and Y.
# o   The syntax of the equation is like: Example: X^4+ 5X^2 + Y^3+Y^2+1
# o   Only use lists to solve this problem



def common_elements():
  i = 0
  function = str(input("Function"))
  value = 0
  if(len(function) > 10):
    print("Cant have more than 10 digits")
  else:
    for i in range(0, len(function)):
      if(function[i] == "*"):
        value += int(function[i-1]) * int(function[i+1])
      elif(function[i] == "^"):
        value += int(function[i-1]) ** int(function[i+1])
      elif(function[i] == "-"):
        value += int(function[i-1]) - int(function[i+1])
      elif(function[i] == "+"):
        value += int(function[i-1]) + int(function[i+1])
      elif(function[i] == "/"):
        value += int(function[i-1]) / int(function[i+1])

  return value

print(common_elements())
