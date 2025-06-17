#day18 - Introduction to Lists in Python

fruits = ["apple", "banana", "mango"]
print(fruits[0])  # Output: apple
print(fruits[-1])  # Output: mango (last item)
fruits.append("orange")  # last me add hoga
fruits.insert(1, "grapes")  # index 1 pe add karega
fruits[0] = "kiwi"  # apple ki jagah kiwi
fruits.remove("banana")  # banana ko hata dega
fruits.pop()  # last item delete hoga

for fruit in fruits:
    print(fruit)

if "apple" in fruits:
    print("Apple is there bro")
else:
   print("Sorry")

print(fruits)
print(len(fruits))  # Kitne items hain
print(fruits[1:3])  # Index 1 se 2 tak ke items

numbers = [4, 2, 9, 1]
print(min(numbers))  # 1
print(max(numbers))  # 9
print(sum(numbers))  # 16

cart = ["laptop", "mouse", "keyboard"]
cart.append("headphone")
print(cart)

# [expression for item in iterable]

lst = [i for i in range(5)]
print(lst)

lst = [i*i for i in range(5)]
print(lst)

lst = [i*i for i in range(10) if i%2==0]
print(lst)

# 📌 Explanation:

#     range(10) → 0 to 9

#     if i%2==0 → sirf even numbers lo

#     unka square list me daalo

# [0, 4, 16, 36, 64]

# ➡️ Because:

#     Even numbers: 0, 2, 4, 6, 8

#     Squares: 0²=0, 2²=4, 4²=16, 6²=36, 8²=64

names = ["Dhruv", "Kishan", "Ravi", "Aayush"]
uper_name = [name.upper() for name in names]
print(uper_name)