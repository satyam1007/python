#day20 - Tuples in Python

tup = (1, 2, 3, 4, "Hello", True)
print(tup[0])
print(tup[-1])
print(type(tup), tup)

if 3 in tup:
  print("yes, 3 is present in tup")
else:
  print("no, 3 is not present in tup")

print(tup[1:4])

# tup_2 = (1)
# print(type(tup_2))

tup_2 = (1,)
print(type(tup_2))
