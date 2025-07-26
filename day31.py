#day31 - Exception Handling in Python

# ente = input("Enter a number: ")
# for table in range(1, 11):
#   print(f"Multiplication of {int(ente)} x {table} is {int(ente)*table}")

# ente = input("Enter a number: ")
# try:
#   for table in range(1, 11):
#     print(f"Multiplication of {int(ente)} x {table} is {int(ente)*table}")
# except Exception as e:
#   print(e)

# ente = input("Enter a number: ")
# try:
#   for table in range(1, 11):
#     print(f"Multiplication of {int(ente)} x {table} is {int(ente)*table}")
# except:
#   print("Invalid Input!")

try:
  value = int(input("Enter an number: "))
  inde = [1,2]
  print(inde[value])
except ValueError:
  print("Number entered is not an integer.")
except IndexError:
  print("Index Error")