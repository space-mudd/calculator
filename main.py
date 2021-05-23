import math
first_number = float(input("type a number: "))
# operations: + - * /

symbol = input("choose an operation (* / - + or exp): ")
if not symbol in {"*","/","+","-", "exp"}:
  print("Don't type that")
  quit()

second_number = float(input("type a second number: "))

# addition +
if symbol == "+": 
  print(first_number + second_number)

# multiplication *  
if symbol == "*":
  print( first_number * second_number)

if symbol == "/":
  print(first_number / second_number)

# subtraction -
if symbol == "-":
  print( first_number - second_number)

if symbol == "exp":
  print( math.pow(first_number, second_number ) )