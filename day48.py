# day48 - Exercise 5 - Snake Water Gun  Also we will learn "random" in python

# random module import kar rahe hain
# random module random values generate karne ke kaam aata hai
import random


# ---------------- random.random() ----------------
# 0.0 se 1.0 ke beech random float number generate karta hai
# 1.0 include nahi hota
print(random.random())


# ---------------- random.randint(a, b) ----------------
# a se b ke beech random integer generate karta hai
# a aur b dono include hote hain
print(random.randint(1, 10))


# ---------------- random.randrange(start, stop) ----------------
# start include hota hai
# stop include nahi hota
# bilkul range() jaisa kaam karta hai
print(random.randrange(1, 10))


# ---------------- random.choice() ----------------
# list ke andar se random ek element choose karta hai
lst = ["apple", "banana", "mango", "orange"]
print(random.choice(lst))


# ---------------- random.shuffle() ----------------
# list ke elements ko randomly shuffle kar deta hai
# original list change ho jaati hai
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)


# ---------------- random.sample() ----------------
# list se random unique elements return karta hai
# original list change nahi hoti
nums = [1, 2, 3, 4, 5, 6]
print(random.sample(nums, 3))


# ---------------- Dice Example ----------------
# 1 se 6 ke beech random number generate karta hai (dice roll)
dice = random.randint(1, 6)
print("Dice number is:", dice)

# ---------------- Let's Make a Game ----------------

game = ["Snake", "Water", "Gun"]
compu_choice = random.choice(game)
compu_input = f"Hey there my choice will be: {compu_choice}"
print(compu_input)

user_input = input("Enter your choice: ")

if user_input.lower() == "snake" and compu_choice == "Water":
  print("Winner is User")
elif user_input.lower() == "water" and compu_choice == "Snake":
  print("Winner is Computer")
elif user_input.lower() == "water" and compu_choice == "Gun":
  print("Winner is User")
elif user_input.lower() == "gun" and compu_choice == "Water":
  print("Winner is Computer")
elif user_input.lower() == "gun" and compu_choice == "Snake":
  print("Winner is User")
elif user_input.lower() == "snake" and compu_choice == "Gun":
  print("Winner is Computer")
elif user_input.lower() == "snake" and compu_choice == "Snake":
  print("Match Draw")
elif user_input.lower() == "water" and compu_choice == "Water":
  print("Match Draw")
elif user_input.lower() == "gun" and compu_choice == "Gun":
  print("Match Draw")
else:
  print("Invalid Input")
