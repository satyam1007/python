# Day11 - Good Morning Sir

# User se input le rahe hain (time in hours, 24-hour format me)
time = int(input("What's the time? "))

# Valid time check
if time < 0 or time > 23:
    print("Invalid time! Please enter time between 0 and 23.")
# Agar time 0 se 12 ke beech hai (subah), toh Good Morning
elif 0 <= time <= 12:
    print("Good Morning Sir!!")
# Agar time 12 se bada aur 15 se chhota ya barabar hai (dopahar), toh Good Afternoon
elif 12 < time <= 15:
    print("Good Afternoon Sir!!")
# Agar time 15 se bada aur 18 se chhota ya barabar hai (shaam), toh Good Evening
elif 15 < time <= 18:
    print("Good Evening Sir!!")
# Agar time 18 se bada ya barabar hai (raat), toh Good Night
elif 18 <= time <= 23:
    print("Good Night Sir!!")
