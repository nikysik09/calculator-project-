def add(a, b):
 return a + b
def subtract(a, b):
 return a - b
def multiply(a, b):
 return a * b
def divide(a, b):
 if b != 0:
  return a / b
 else:
  return "pomulka!"
def power(a, b):
 return a ** b
print("=== just kalkulator ===")
print("u can: +, -, *, /, **")
print("for exit type 'exit'")
while True:
 operation = input("\nVedit operciu (+, -, *, /, **) or 'exit': ")

 if operation.lower() == 'exit':
  print("goodbay!")
  break

 if operation not in ['+', '-', '*', '/', '**']:
  print("False!")
  continue

 try:
  num1 = float(input("Your first number: "))
  num2 = float(input("Your second number: "))

  if operation == '+':
   result = add(num1, num2)
  elif operation == '-':
   result = subtract(num1, num2)
  elif operation == '*':
   result = multiply(num1, num2)
  elif operation == '/':
   result = divide(num1, num2)
  elif operation == '**':
   result = power(num1, num2)

  print(f"Result: {result}")

 except ValueError:
  print("False: write true numbers!")