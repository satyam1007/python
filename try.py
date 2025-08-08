# print(4.00//(2.0+2.0))
# print(24//6%3)
# print(2**3**2)
# print(21//4+6/3)
# print(5 < 10 and 12 > 7 or not 7 > 4)

# s = "madam"  
# print(s == s[::-1])  # True  

# s = "helloworld"
# vowels = "aeiouAEIOU"
# count = 0
# for ch in s:
#   if ch in vowels:
#     count += 1
#     print("Vowels:", count)

# for i in range(100):
#   print(f"{i}. hello world")

# squareOfNum = [i*i for i in range(10) if i%2 == 0]
# print(squareOfNum)

# def intro(*args, **kwargs):
#     for item in args:
#         print(item)
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# intro("Aman", "Python", age=20, city="Delhi")


# def sum(n):
#   if n == 0:
#     return 0
#   else:
#     return n + sum(n-1)

# print(sum(7))
# print(7+6+5+4+3+2+1+0)
def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count

print(count_vowels("dfaeioutbmk"))  # Output: 5

if(0.1 + 0.2 == 0.3):
    print("True")
else:
    print("False")

# if (0.1 + 0.2 == 0.30000000000000004):
#     print("True")
# else:
#     print("False") #This would work