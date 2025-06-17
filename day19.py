#day19 - List Methods in Python

fruits = ["apple", "banana"]
fruits.append("mango")
print(fruits)  # ['apple', 'banana', 'mango']
fruits.insert(1, "grapes")
print(fruits)  # ['apple', 'grapes', 'banana', 'mango']
fruits.pop()
print(fruits)  # Last item hat gaya
fruits.clear()
print(fruits)  # []

a = [1, 2]
b = [3, 4]
a.extend(b)
print(a)  # [1, 2, 3, 4]

nums = [1, 2, 3, 2]
nums.remove(2)
print(nums)  # [1, 3, 2]

nums = [5, 10, 15]
print(nums.index(10))  # 1

nums = [1, 2, 2, 3, 2]
print(nums.count(2))  # 3

marks = [90, 70, 50]
marks.sort()
print(marks)  # [50, 70, 90]
marks.sort(reverse=True)
print(marks)  # [90, 70, 50]

nums = [1, 2, 3]
nums.reverse()
print(nums)  # [3, 2, 1]

original = [1, 2, 3]
new = original.copy()
print(new)  # [1, 2, 3]
