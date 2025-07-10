#day23 - f-strings in Python

# Old way (commented out):
# letter = "Hey my name is {} and I'm from {}"
# country = "India"
# name = "Don"
# print(letter.format(country, name))  # Output will be: Hey my name is India and I'm from Don

# Correct order using index:
# letter = "Hey my name is {1} and I'm from {0}"
# print(letter.format(country, name))  # Output: Hey my name is Don and I'm from India

# f-string method (recommended, cleaner and readable)
country = "India"
name = "Don"

# Variables directly curly braces mein likh ke use kiya
print(f'Hey my name is {name} and I from {country}')  # Output: Hey my name is Don and I from India

# Agar hume braces print karne hain (as text), toh double curly braces ka use karte hain
print(f'Hey my name is {{name}} and I from {{country}}')  # Output: Hey my name is {name} and I from {country}

# Float formatting example: only 2 decimal places show karo
price = 51.024032
txt = f"For only {price:.2f}"  # .2f ka matlab: 2 decimal tak round karna
print(txt)  # Output: For only 51.02

# f-string mein expression bhi likh sakte hain
print(f'{2*30}')  # Output: 60

# f-string expression ka type bhi string hi hota hai
print(type(f'{2*30}'))  # Output: <class 'str'>
