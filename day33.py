#day33 - Raising custom errors in Python

# digit = int(input("Enter a digit value b/w 5 and 9: "))

# if(digit<5 or digit>9):
#   raise ValueError("Value should be b/w 5 and 9")


# class MyCustomError(Exception):
#     """Custom exception for specific application errors."""
#     pass



class ValidationError(Exception):
    def __init__(self, message, code=None):
        super().__init__(message)
        self.code = code

def check_age(age):
    if age < 18:
        raise ValidationError("User must be at least 18 years old", code=1001)

try:
    check_age(15)
except ValidationError as e:
    print(f"Validation failed: {e} (code: {e.code})")