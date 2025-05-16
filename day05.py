# Day05 - Typecasting in Python

# num1 aur num2 ko humne string type mein define kiya hai
num1 = "1"
num2 = "2"

# Yahaan hum num1 aur num2 ko directly add kar rahe hain
# Lekin, dono variables string type hain, isliye unhe concatenate kiya jaa raha hai
# Output: "12" - dono strings ko jod diya gaya hai
print(num1 + num2)

# Explicit type conversion (data type ko explicitly convert karna)
# Yahaan hum num1 aur num2 ko strings se integers mein convert kar rahe hain
# Phir inhe add kar rahe hain
# Output: 3 - ab dono variables integers hain, toh addition hoga
print(int(num1) + int(num2))

# Implicit type conversion (Python apne aap data type ko convert karta hai)
# Yahaan hum num3 ko float type mein define karte hain aur num4 ko integer type mein
# Python automatically float ko integer ke saath add karne ke liye convert kar deta hai
# Output: 9.9 - num3 (float) aur num4 (int) ko add kiya gaya hai
num3 = 1.9
num4 = 8
print(num3 + num4)

# Strings ko concatenate karna
str1 = "Hello"
str2 = "world"

# Yahaan hum dono strings ko directly add kar rahe hain
# Output: "Helloworld" - strings ko concatenate kiya gaya hai
print(str1 + str2)

# Yahaan hum dono strings ko space ke saath add kar rahe hain
# Output: "Hello world" - dono strings ke beech mein space diya gaya hai
print(str1 + " " + str2)
