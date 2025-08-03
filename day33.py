#day33 - Raising custom errors in Python

'''
You can forcefully raise exceptions using raise to handle invalid scenarios.
'''

'''
==> Syntax
if condition:
    raise ErrorType("Custom message")
'''

'''
==> Raising Custom Errors In Python
'''

digit = int(input("Enter a digit value b/w 5 and 9: "))

if(digit<5 or digit>9):
  raise ValueError("Value should be b/w 5 and 9")

'''
==> Custom Exception Class:
'''

class NegativeAgeError(Exception):  
    pass  # Yahan kuch nahi likhna, bas error ka naam define karna hai

'''
Kyu?
  Python ko force karna hota hai ki class ka body empty nahi ho sakta.
  pass daalne se syntax error nahi aata.
'''

age = -5
if age < 0:
    raise NegativeAgeError("Age is negative!")