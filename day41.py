#day41 - Local vs Global Variables in Python

x = 4 # Global Variable
print(x)

def my_func():
  global x
  x = 5 # This will change the value of global variable
  print(x)
  y = 10

my_func()
print(x)
# print(y) # This will cause an error because y is a local variable and is not accessible outside of the function
