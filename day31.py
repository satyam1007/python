#day31 - Exception Handling in Python

'''
==> Exceptions are runtime errors that disrupt normal program flow. Python uses try-except blocks to handle them gracefully.
'''

'''
==> Syntax
try:
    Code that might raise an error
except ErrorType:
    What to do if the error occurs
'''

try:
    print(10 / 0)  # Division by zero → ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero!")

ente = input("Enter a number: ")  # User se number input le rahe hain
try:
  for table in range(1, 11):      # 1 se 10 tak table print karne ka loop
    print(f"Multiplication of {int(ente)} x {table} is {int(ente)*table}")
except Exception as e:            # Agar koi bhi error aaye to uska error message print hoga
  print(e)

ente = input("Enter a number: ")  # User se input le rahe hain
try:
  for table in range(1, 11):      # 1 se 10 tak loop
    print(f"Multiplication of {int(ente)} x {table} is {int(ente)*table}")
except:                           # Agar koi bhi error aaye (jaise wrong input), to generic message dega
  print("Invalid Input!")

try:
  value = int(input("Enter an number: "))  # User input ko int me convert kar rahe hain
  inde = [1, 2]                            # ek choti si list banayi gayi hai
  print(inde[value])                      # list ke us index ka value print ho raha hai
except ValueError:                        # Agar input integer nahi hai
  print("Number entered is not an integer.")
except IndexError:                        # Agar input index list me exist nahi karta
  print("Index Error")