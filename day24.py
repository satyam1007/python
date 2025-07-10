#day24 - Docstrings in Python

# Function define kar rahe hain jo kisi number ka square print karega
def square(n):
    '''Takes in a number n, and return the square of n'''  # Yeh hai docstring — function ka explanation
    print(n**2)  # Yeh line n ka square print karti hai

# Function call kar rahe hain with input 5
square(5)  # Output: 25

# Function ki docstring print kar rahe hain
print(square.__doc__)  # Output: Takes in a number n, and return the square of n
