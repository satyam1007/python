#day22 - KBC Project

# Questions list
questions = [
  "Question 1: What is the output of print(2 + 3 * 4) in Python?", 
  "Question 2: Which of these is used to get input from the user in Python?",
]

# Har question ke liye options
options = [
  ["A) 20", "B) 14", "C) 12", "D) 10"], 
  ["A) scanf()", "B) cin", "C) input()", "D) gets()"]
]

# Correct answers ke option letters
correct_options = ['B', 'C']  # First question ka answer: B, second ka: C

# Score variable to track user score
score = 0

# Game start prompt
ready = input("Are You Ready To Play The Game ? Please Select (Yes/No): ")

# Agar user "yes" likhta hai
if ready.lower() == "yes":
  # Har question ke liye loop
  for i in range(len(questions)):
    print(f'\n{questions[i]}')  # Question print karo
    for opt in options[i]:      # Uske options print karo
      print(opt)

    # User se answer lo aur uppercase mein convert karo
    user_input = input("Submit your answer [A/B/C/D]: ").upper()
    
    # Answer check karo
    if user_input == correct_options[i]:
      print("✅ Correct Answer!")
      score += 1  # Score badhao
    else:
      print("❌ Wrong Answer.")
    
    # Agar ye last question nahi hai, toh poochho continue karna hai ya nahi
    if i != len(questions) - 1:
      cont = input("Do you want to continue? (Yes/No): ")
      if cont.lower() != "yes":
        break  # Loop se bahar aa jao agar user "no" bole

  # Game over, final score print karo
  print(f"\n🎉 Game Over! Your total score is: {score}/{len(questions)}")

# Agar user ready nahi hai
else:
  print("No worries! Come back when you're ready 😊")
