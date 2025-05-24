#day13 - For Loops in Python

name = "Abhishek"
for i in name:
  print(i, end=", ")
  if(i == "b"):
    print("Hello b is printed")

list_1 = ["Red", "Blue", "Yellow", "Purple", "Dark", "White"]
for color in list_1:
  print(color)
  for i in color:
    print(i)

for k in range(5):
  print(k)
  # print(k + 1)

for k in range(1, 9):
  print(k)

# range(1, 12, 2) ka matlab:

# range(start, stop, step)

#     start = 1 → counting 1 se shuru hogi

#     stop = 12 → lekin 12 se pehle tak chalega (12 include nahi hota)

#     step = 2 → har step me 2 number ka gap hoga (odd numbers generate honge)
for k in range(1, 12, 3):
  print(k)