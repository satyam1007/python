#day30 - For Loop With Else in Python

# for i in range(1, 10):
#   print(i)

# else:
#   print("Sorry")

# for i in []:
#   print(i)

# else:
#   print("Sorry")

# for i in range(1, 10):
#   print(i)
#   if i == 8:
#     break

# else:
#   print("Sorry")

i = 0
while i<10:
  print(i)
  i = i + 1
  if i == 8:
    break

else:
  print("Oops")

for x in range(5):
  print("iteration no {} in for loop".format(x+1))
else:
  print("Hello Jii")
print("Out of the loop")