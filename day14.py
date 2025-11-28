#day14 - While Loops in Python

i = 0
while i < 5:
  print(i)
  i += 1

i = 0
while i < 5:
  i += 1
  print(i)


If increment is after print → 0 se 4 tak
If increment is before print → 1 se 5 tak

i  = int(input("Enter a number: "))
while(i<20):
  i  = int(input("Enter a number: "))
  print(i)

print("Done with the loop")

count = 5
while(count > 0):
  print(count)
  count = count - 1
else:
  print("I'm inside")

# Example: do while ka alternative in Python

while True:
    user_input = input("Kya tu continue karna chahta hai? (yes/no): ")
    if user_input.lower() != 'yes':
        break

# while True:

#     Ye ek infinite loop hai — matlab hamesha chalta rahega jab tak hum break na kar dein.

#     Yani body pehle chalegi, condition baad me check hogi. Ye hi hota hai do while ka concept.

# 🔹 input("Kya tu continue karna chahta hai? (yes/no): ")

#     Ye user se input leta hai.

#     Jaise: agar tu type karega yes ya no, wo value user_input variable me store ho jaayegi.

# 🔹 if user_input.lower() != 'yes':

#     .lower() isliye kiya gaya taaki agar tu YES, Yes, yes kuch bhi likhe — sab same treat ho.

#     Agar user ne yes nahi likha, to:

# 🔹 break

#     Ye loop ko roka deta hai. Matlab ab repeat nahi karega, loop se bahar nikal jaayega.
