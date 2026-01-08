# day47 - 'is' vs '==' in Python

# 'is' vs '==' in Python

# ---------------- '==' OPERATOR ----------------
# '==' value compare karta hai
# Matlab: dono variables ke andar SAME DATA hai ya nahi

a = 10
b = 10

print(a == b)   # True
# Kyunki a aur b dono ki value same hai (10)


# ---------------- 'is' OPERATOR ----------------
# 'is' memory location (identity) compare karta hai
# Matlab: kya dono variables SAME OBJECT ko point kar rahe hain

print(a is b)   # True (small integers cache hote hain Python mein)


# ---------------- LIST EXAMPLE ----------------
# Lists mutable hoti hain, isliye yahan difference clear dikhta hai

x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)   # True
# Kyunki dono lists ke elements same hain

print(x is y)   # False
# Kyunki dono alag-alag memory location mein stored hain


# ---------------- SAME OBJECT ASSIGNMENT ----------------
# yahan y ko x ke equal assign kiya gaya hai

x = [4, 5, 6]
y = x

print(x == y)   # True
# Value same hai

print(x is y)   # True
# Kyunki dono SAME object ko point kar rahe hain


# ---------------- STRING EXAMPLE ----------------
# Strings immutable hoti hain, kabhi-kabhi Python same memory use karta hai

s1 = "hello"
s2 = "hello"

print(s1 == s2)  # True
# Value same hai

print(s1 is s2)  # True (zyada cases mein same memory hoti hai)

