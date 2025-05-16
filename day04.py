# Day04 - Calculator Project

# Variables define kar rahe hain: n ko 15 aur num ko 6 value de rahe hain
n = 15
num = 6

# Addition ka operation
# Yahaan pe hum n aur num ko add kar rahe hain aur result print kar rahe hain
print("Addition of", n, "+", num, "is", (n + num))

# Subtraction ka operation
# Yahaan pe hum n se num ko subtract kar rahe hain aur result print kar rahe hain
print("Subtraction of", n, "-", num, "is", (n - num))

# Multiplication ka operation
# Yahaan pe hum n aur num ko multiply kar rahe hain aur result print kar rahe hain
print("Multiplication of", n, "*", num, "is", (n * num))

# Division ka operation
# Yahaan pe hum n ko num se divide kar rahe hain aur result print kar rahe hain
print("Division of", n, "/", num, "is", (n / num))

# Floor division ka operation
# Yahaan pe floor division kar rahe hain, jo decimal part ko ignore karta hai
# Result ko integer form mein print kar rahe hain
print("Floor division number of", n, "//", num, "is", (n // num))

# Exponential ka operation
# Yahaan pe hum n ko num ki power raise kar rahe hain aur result print kar rahe hain
print("Exponential of", n, "**", num, "is", (n ** num))

# Modulus ka operation
# Yahaan pe hum modulus nikaal rahe hain, jo remainder dega jab n ko num se divide kiya jaye
print("Modulus number of", n, "%", num, "is", (n % num))

# For Better Practice

num_1 = float(input("Enter a number: "))
operator = input("What is your operator: ")
num_2 = float(input("Enter another number: "))

if operator in ["/", "//"] and num_2 == 0:
  print("Error: Division by zero is not allowed.")
elif(operator == "+"):
  print("The Addition of ", num_1, "and", num_2, "is", num_1+num_2)
elif(operator == "-"):
  print("The Substraction of ", num_1, "and", num_2, "is", num_1-num_2)
elif(operator == "*"):
  print("The Multiplication of ", num_1, "and", num_2, "is", num_1*num_2)
elif(operator == "/"):
  print("The Division of ", num_1, "and", num_2, "is", num_1/num_2)
elif(operator == "//"):
  print("The Floor division of ", num_1, "and", num_2, "is", num_1//num_2)
elif(operator == "**"):
  print("The Exponentiation of ", num_1, "and", num_2, "is", num_1**num_2)
elif(operator == "%"):
  print("The Modulus of ", num_1, "and", num_2, "is", num_1%num_2)
else:
  print("Oops something went wrong!!")

