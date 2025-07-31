#day25 - Recursion in Python

# Factorial calculate karne ke liye recursive function
def factorial(n):
    # Base case: agar n 0 ya 1 ho, toh factorial 1 hota hai
    if(n == 0 or n == 1):
        return 1
    else:
        # Recursive case: n * factorial of (n - 1)
        return n * factorial(n - 1)

print(factorial(5))

# Function calls with different inputs
# print(factorial(0))  # Output: 1 (0! = 1)
# print(factorial(1))  # Output: 1 (1! = 1)
# print(factorial(3))  # Output: 6 (3! = 3*2*1)
# print(factorial(4))  # Output: 24 (4! = 4*3*2*1)
# print(factorial(5))  # Output: 120 (5! = 5*4*3*2*1)

# What is Fibonacci Sequence?
# Fibonacci sequence ek number series hoti hai jisme:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# Har number previous 2 numbers ka sum hota hai:

# F(0) = 0  
# F(1) = 1  
# F(n) = F(n-1) + F(n-2)   (for n >= 2)

# Fibonacci Using Loop (Iterative Method)
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b

fibonacci(10)
print('\n')

# Fibonacci Using Recursion
def fib(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return fib(n-1) + fib(n-2)

for i in range(6):
    print(fib(i), end=' ')

print('\n')

# Fibonacci With List (Storing Sequence)
def fibonacci_list(n):
    fib_siq = [0, 1]                # Fibonacci list start ho rahi 0, 1 se
    for i in range(2, n):           # Loop 2 se start ho raha hai yahaa per humne 2 esliye liyaa kyuki fib_siq = [0, 1] esme index ke hisab se 1 element he aur hum 2 se start karna chahte he esliye agar usme 2 elements hote to hum 3 se start karte
        fib_siq.append(fib_siq[-1] + fib_siq[-2])
        # fib_siq = [0, 1]
        # fib_siq[-1] = 1
        # fib_siq[-2] = 0
        # 1 + 0 = 1
        # fib_siq.append(1)
        print(fib_siq)


fibonacci_list(10)