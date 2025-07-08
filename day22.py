#day22 - KBC Project

questions = [
  "Question 1: What is the output of print(2 + 3 * 4) in Python?", 
  "Question 2: Which of these is used to get input from the user in Python?",
  ]

options = [
  ["A) 20", "B) 14", "C) 12", "D) 10"], 
  ["A) scanf()", "B) cin", "C) input()", "D) gets()"]
  ]

correct_options = ['B', 'C'] # Only correct options (just the letters)

score = 0 # Track user's score

ready = input("Are You Ready To Play The Game ? Please Select (Yes/No):")

if ready.lower() == "yes":
  # Question 1
  for i in range(len(questions)):
    print(f'\n{questions[i]}')
    for opt in options[i]:
      print(opt)
    user_input = input("Submit your answer [A/B/C/D]").upper()
      
    if user_input == correct_options[i]:
      print("✅ Correct Answer!")
      score += 1
    else:
      print("❌ Wrong Answer.")
    if i != len(questions) - 1:
      cont = input("Do you want to continue? (Yes/No): ")
      if cont.lower() != "yes":
        break
  print(f"\n🎉 Game Over! Your total score is: {score}/{len(questions)}")
else:
  print("No worries! Come back when you're ready 😊")