import time

# day51 - Decorators in Python
'''
Think of a decorator as a piece of "gift wrap" for a function. It allows you to wrap another function to extend its behavior—without permanently modifying the code of the function you’re wrapping.

In Python, decorators are a powerful tool for keeping your code DRY (Don't Repeat Yourself). They are commonly used for logging, access control, or timing how long a function takes to run.

1. The Core Concept: Functions as Objects
To understand decorators, you first need to know that in Python, functions are objects. This means you can:

Assign a function to a variable.

Pass a function as an argument to another function.

Return a function from another function.

2. Anatomy of a Basic Decorator
A decorator is essentially a function that takes another function as an input, defines a "wrapper" inside it, and then returns that wrapper.
'''

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()  # This is where the original function runs
        print("Something is happening after the function is called.")
    return wrapper

def say_hello():
    print("Hello!")

# Manual way to decorate:
decorated_hello = my_decorator(say_hello)
decorated_hello()

'''
The "Sugar" Syntax: @
Instead of manually reassigning the function, Python provides a much cleaner way to apply decorators using the @ symbol.
'''

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

'''Now, every time you call say_hello(), it automatically runs through my_decorator.'''

'''
3. Handling Arguments (*args and **kwargs) 
The example above works for functions with no arguments. But what if your function needs to take inputs? To make a decorator universal, we use *args and **kwargs.
'''

'''
👉 Important point:
wrapper() must accept the same arguments as the original function (add).
'''

def logger(func):
  def wrapper(*args, **kwargs):
    print(f"Running '{func.__name__}' with arguments {args}")
    result = func(*args, **kwargs)
    print(f"Finished running '{func.__name__}'")
    return result
  return wrapper

@logger
def add(x, y):
  return x + y

print(add(1, 2))

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer
def heavy_computation():
    time.sleep(1.5) # Simulating a delay
    return "Done!"

heavy_computation()
