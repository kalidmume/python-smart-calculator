#create function get_input_user
def get_user_input():
  valid_operators = {"+", "-", "*", "/", "%", "**", "//" }
  while True:
    try:
      #prompt the  user for the  first and second numbers
      num1 = float(input("Enter the number first: "))
      num2 = float(input("Enter the number second: ")) 
      #prompt the  user to choose an operator
      operate = input("Enter an operation ( +, -, *, /, %, **,// ): ")
      if operate not in valid_operators:
        continue
      return num1, num2, operate 
    
    except ValueError:
      print('Invalid input! please enter numeric values only.')

#perform basic arithmetic operations
def calculate(num1, num2, operator):
  #Addition
  if operator == "+":
    return f"{num1} + {num2} = {num1 + num2}"

  #Substraction
  elif operator == "-":
    return f"{num1} - {num2} = {num1 - num2}"
 
 #Multiplication
  elif operator == "*":
    return f" {num1} * {num2} = {num1 * num2}"
 
 #Division 
  elif operator == "/":
    try:
      return f"{num1} / {num2} = {num1 / num2}"
    except ZeroDivisionError:
      return "Error: Cannot divide by zero."
 
 #Modulus
  elif operator == "%":
    try:
      return f"{num1} % {num2} = {num1 % num2}  "
    except ZeroDivisionError:
      return "Error: Cannot divide by zero."
 
 
  #Exponentiation
  elif operator == "**":
   return f" {num1} ** {num2} = {num1 ** num2}"
   
   #Floor Division
  elif operator == "//":
    try:
      return f" {num1} // {num2} = {num1 // num2}"
    except ZeroDivisionError:
      return "can't divide by zero!"
 
 #Invalid operator
  else:
   return "Error: invalid operator."


#function to run the calculator
def run_calculator():
  print("Welcome to the smart calculations!")
  while True:
    user_choice = input("Would you like to calculate? (yes or no): "). lower()
   
    if user_choice == "yes":
      #Get user input
      num1, num2, operator = get_user_input()
      #perform calculation
      result = calculate(num1, num2, operator)
      print(f"Result:, {result}")
    
    elif user_choice == "no":
      print("Exiting calculator. Goodbye!")
      break
    
    else:
      print("invalid input. please enter 'yes or no' .")


run_calculator()
