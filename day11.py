# Day11 - Good Morning Sir

# User se input le rahe hain (time in hours, 24-hour format me)
time = int(input("What's the time ?"))

# Agar time 00 se 12 ke beech hai (subah), toh Good Morning
if(time >= 00 and time <= 12):
    print("Good Morning Sir!!")

# Agar time 12 se bada aur 15 se chhota ya barabar hai (dopahar), toh Good Afternoon
elif(time > 12 and time <= 15):
    print("Good Afternoon Sir!!")

# Agar time 15 se bada aur 18 se chhota ya barabar hai (shaam), toh Good Evening
elif(time > 15 and time <= 18):
    print("Good Evening Sir!!")

# Agar time 18 se bada hai (raat), toh Good Night
elif(time > 18):
    print("Good Night Sir !!")

# Agar koi bhi condition match nahi hui (jaise galat input), toh error message
else:
    print("Oops something went wrong")
