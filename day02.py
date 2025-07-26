#day02 - Comments, Escape Sequences & Print Statement

# Ye line "Hey I am a' "good boy" and this viewer is also a good boy/girl" print karegi
# Yahaan escape sequences ka use ho raha hai:
# - \' : Single quote ko string mein include karne ke liye.
# - \" : Double quote ko string mein include karne ke liye.
# - \n : New line dene ke liye, jo text ke neeche new line pe move karega.
print("Hey I am a\' \"good boy\" \nand this viewer is also a good boy/girl")

# Ye line comment hai, matlab code me isse run nahi hoga jab tak hum usse comment se hata nahi dete.
# print("Hello World !!!") # Ye line comment ke roop mein hai, jo explanation ke liye hoti hai.

'''
Ye ek multi-line comment hai.
Python mein multiple lines ke comment ke liye hum 'single quot' ya "double quote" ka use karte hain.
Ye text jo likha gaya hai, wo Python ignore karega aur usse execute nahi karega.
'''

# Ye line print karegi "Hey 6~7", jisme '~' separator ke roop mein use ho raha hai.
# sep="~" ka matlab hai ki "6" aur "7" ke beech "~" ka symbol dikhayi dega.
# end="009\n" ka matlab hai ki print statement ke baad "009" dikhayi dega aur phir new line (enter) press hoga.
print("Hey", 6, 7, sep="~", end="009\n")

# Ye line simply "Hello world" print karegi.
print("Hello world")