# day46 - Map, Filter aur Reduce in Python

# reduce function ko import kar rahe hain functools module se
from functools import reduce


# Ye list hai jisme 1 se 10 tak numbers hain
lst = [1,2,3,4,5,6,7,8,9,10]


# ---------------- MAP FUNCTION ----------------
# map() function har element par same function apply karta hai

# yahan lambda function use ho raha hai
# lambda x: x*x*x ka matlab hai number ka cube nikalna
# map har element ka cube banake new list return karega

new_lst = list(map(lambda x: x*x*x, lst))
print(new_lst)
# Output: [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]


# ---------------- FILTER FUNCTION ----------------
# filter() function condition ke base par elements ko filter karta hai

def num(n):
    # ye function True return karega agar n > 2 ho
    return n > 2

# sirf wahi values list mein aayengi jo condition satisfy karti hain
new_new_lst = list(filter(num, [2,3,4]))
print(new_new_lst)
# Output: [3, 4]


# ---------------- REDUCE FUNCTION ----------------
# reduce() function list ke saare elements ko combine karke ek single value banata hai

def sum(x, y):
    # do numbers ko add karta hai
    return x + y

# list ke saare numbers ko add karega
new_lst2 = reduce(sum, [1,2,3,4,5,6])
print(new_lst2)
# Output: 21


# reduce ko lambda ke saath bhi use kar sakte hain
new_lst2 = reduce(lambda x, y: x + y, [1,2,3,4,5,6,7])
print(new_lst2)
# Output: 28
