#day35 - Short hand if else statements

# value_if_true if condition else value_if_false

age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)

num1 = 11
num2 = 21
print("Yes") if num1 > num2 else print("=") if num1 == num2 else print("Sorry")

num3 = 31 if num1 > num2 else 0
print(num3)