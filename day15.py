#day15 - break and continue in Python

# for i in range(12):
#   if(i == 10):
#     print("Skip the iteration")
#     break
#   print("5 x", i, "=", 5 * i)

# for i in range(12):
#   if(i == 10):
#     print("Skip the iteration")
#     continue
#   print("5 x", i, "=", 5 * i)

i = 0
while True:
  print(i)
  i = i + 1
  if(i % 100 == 0):
    break