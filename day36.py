#day36 - Enumerate Function in Python 

list1 = ["A", "B", "C", "D", "E", "F", "G"]

# index = 0
# for lst in list1:
#   print(lst)
#   if(index == 6):
#     print("Wow!")
#   index += 1


for index, lst in enumerate(list1, start=3): # 📝 Matlab: start=3 hone ka matlab pehla element "A" ka index 3 ban gaya. Jab 4th element "D" pe aaye to index 6 hua → "Wow!" print ho gaya.
  print(lst)
  if(index == 6):
    print("Wow!")
