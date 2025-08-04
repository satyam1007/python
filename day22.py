#day22 - KBC Project

'''
📝 Short Note: How correct_options[i] Works in Quiz Code

    questions list har question ko index (0, 1, 2...) ke through store karti hai.

    options list bhi same index par har question ke options store karti hai.

    correct_options list har question ke sahi option ka letter ('A', 'B', etc.) ko same index par store karti hai.



questions[0] = "Question 1..."
options[0] = ["A) ...", "B) ...", "C) ...", "D) ..."]
correct_options[0] = "B"  # Means question 1 ka sahi answer B hai

Jab loop chalta hai (for i in range(len(questions))), tab:

    questions[i] print hota hai

    options[i] print hote hain

    User se answer liya jaata hai → user_input

    Us input ko compare kiya jaata hai correct_options[i] se

'''

# Questions list
questions = [
    "Question 1: What is the output of print(2 + 3 * 4) in Python?", 
    "Question 2: Which of these is used to get input from the user in Python?",
    "Question 3: What is the correct file extension for Python files?",
    "Question 4: Which keyword is used to define a function in Python?",
    "Question 5: What will be the output of: print(len('Hello'))?"
]

# Har question ke liye options
options = [
    ["A) 20", "B) 14", "C) 12", "D) 10"], 
    ["A) scanf()", "B) cin", "C) input()", "D) gets()"],
    ["A) .pt", "B) .pyt", "C) .py", "D) .python"],
    ["A) func", "B) define", "C) function", "D) def"],
    ["A) 4", "B) 5", "C) 6", "D) 0"]
]

# Correct answers ke option letters
correct_options = ['B', 'C', 'C', 'D', 'B']

# Game start prompt
ready = input("Are You Ready To Play The Game ? Please Select (Yes/No): ")

if ready.lower() == "yes":
  while True:
        score = 0  # Har baar score reset karo
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

        # Quiz complete hone ke baad score dikhao
        print(f"\n🎉 Game Over! Your total score is: {score}/{len(questions)}")

        # Puchho: dubara khelna chahenge?
        retry = input("Kya aap dobara try karna chahte hain? (Yes/No): ")
        if retry.lower() != "yes":
            print("👋 Dhanyawaad! Fir milenge.")
            break  # Exit loop

else:
    print("No worries! Come back when you're ready 😊")
