# Day10 - If Else Conditional Statements in Python

drivingLicense = int(input("Hi, your age is: "))  # User se age input lega
age = 18

# Kuch comparison examples (commented out)
# print(age<18)  # False
# print(age<=18)  # True
# print(age>18)  # False
# print(age>=18)  # True
# print(age!=18)  # False
# print(age==18)  # True

print("Your age is", drivingLicense)  # Jo bhi input diya gaya wo print hoga

if(drivingLicense >= age):
    print("Wow, Now you are ready to drive because your age is above", age)
    # Agar age > 18 hai to driving allowed
else:
    print("Oops, Sorry you are not ready to drive because your age is below", age)
    # Agar age <= 18 hai to driving allowed nahi hai

# Apple aur budget ka example
applePrice = 100
budget = 200

if (budget - applePrice > 50):
    print("Alexa, add 1 kg Apples to the cart.")  # 200 - 100 = 100 > 50 → Apple add hoga
else:
    print("Alexa, do not add Apples to the cart.")

# Ek number input karaya ja raha hai
num = int(input("Enter a number: "))

if(num > 0):
    print("The value of num is", num, "and this positive")  # Agar number > 0 hai
elif(num < 0):
    print("The value of num is", num, "and this negative")  # Agar number < 0 hai
elif(num == 0):
    print("The value of num is", num, "and this a neither positive nor negative means neutral")  # Agar number 0 hai
else:
    print("Number is positive")  # Ye else kabhi nahi chalega actually (safety ke liye hai)
print("I am happy now")  # Ye hamesha chalega

# Nested if-else ka example
num = 8

if(num < 0):
    print("Number is negative")  # Agar num < 0 hota to
elif(num > 0):
    if(num < 10):
        print("Number is between 1-10")  # num > 0 and < 10
    elif(num > 10 and num < 20):
        print("Number is between 10 - 20")  # ✅ Output: Ye chalega kyunki 18 > 10 and < 20
    else:
        print("Number is", num)  # Ye num ki actual value show karega
else:
    print("Number is zero")  # Agar num == 0 hota to
