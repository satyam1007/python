#day21 - Operations on Tuples in Python

t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)   # Output: (1, 2, 3, 4)

t = (1, 2)
print(t * 3)     # Output: (1, 2, 1, 2, 1, 2)

t = (10, 20, 30)
print(20 in t)      # True
print(40 not in t)  # True

t = ('a', 'b', 'c')
for item in t:
    print(item)

# Packing
t = 1, 2, 3

# Unpacking
a, b, c = t
print(a)  # 1
print(b)  # 2
print(c)  # 3