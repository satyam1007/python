# Day09 - String Methods in Python

# Ek string banayi gayi hai jisme unnecessary exclamation marks hain
name = "!!! Harry !!!!!!!!"

print(name)  # !!! Harry !!!!!!!!  -> Puri string print karega
print(len(name))  # 18  -> String ka total length (characters ka count) batayega, including ! and spaces

print(name.upper())  # !!! HARRY !!!!!!!!  -> Saari alphabets ko CAPITAL me kar dega
print(name.lower())  # !!! harry !!!!!!!!  -> Saari alphabets ko lowercase me kar dega

# Sirf end ke '!' characters ko hata dega, beech wale nahi
print(name.rstrip("!"))  # !!! Harry  -> End ke exclamations hat gaye

# "Harry" ko "Honney" se replace kar dega
print(name.replace("Harry", "Honney"))  # !!! Honney !!!!!!!!  -> Sirf 'Harry' replace hua

# String ko space ke basis pe tod dega (list ban jayegi)
print(name.split(" "))  # ['!!!', 'Harry', '!!!!!!!!']  -> 3 parts me split hua

# Naya string: greetings
gritings = "welcome tO mY portfoliyo"

# Sirf first character capital hoga, baaki sab lowercase
print(gritings.capitalize())  # Welcome to my portfoliyo

# str1 me ek aur string assign ki gayi hai
str1 = "Welcome to the Console!!!"

# String ko center karega 50 character wide area me, left/right side me spaces daal ke
print(str1.center(50))  # '         Welcome to the Console!!!         '  -> 50 chars wide, center aligned

# str1 ka original length print karega
print(len(str1))  # 27  -> original string ka length

# Centered string ka length (jo 50 hoga kyunki center(50) use kiya hai)
print(len(str1.center(50)))  # 50  -> center karne ke baad total length

# String me 'e' character kitni baar aaya hai, count karega
print(str1.count("e"))  # 3  -> 'e' 3 times hai

# Kya string '!' pe end ho rahi hai? True/False return karega
print(str1.endswith("!"))  # True  -> kyunki '!!!' se end ho rahi hai

# Check karega ki position 4 se 10 ke beech me string 'to' end ho raha hai ya nahi
print(str1.endswith("to", 4, 10))  # True  -> "me to" substring me 'to' end ho raha hai

# Ek aur string assign hui
str1 = "He's name is Dan. He is an honest man."

# 'is' substring pehli baar kis position pe mila (index number dega)
print(str1.find("is"))  # 11  -> pehli baar 'is' position 11 pe mila

# Agar substring nahi mila to -1 return karega
print(str1.find("isss"))  # -1  -> 'isss' string me nahi hai

# Check karta hai string sirf letters aur numbers se bana hai ya nahi
str1 = "WelcomeToTheConsole"
print(str1.isalnum())  # True  -> sirf letters aur numbers hain

# Sirf alphabets hain ya nahi (space, number allowed nahi)
str1 = "Welcome"
print(str1.isalpha())  # True  -> sirf alphabets hain

# Kya poori string lowercase me hai?
str1 = "hello world"
print(str1.islower())  # True  -> saare characters lowercase hain

# Kya string printable characters se bani hai? (Jaise \n ho to False hoga)
str1 = "We wish you a Merry Christmas"
print(str1.isprintable())  # True  -> sab printable characters hain

# Spacebar se bani string hai, to check karega kya sirf whitespace hai?
str1 = "      "
print(str1.isspace())  # True  -> sirf space hi hai

# Wapas space hi hai, isliye ye bhi True hoga
str1 = "      "
print(str1.isspace())  # True

# Kya har word ka first letter capital hai?
str1 = "World Health Organization"
print(str1.istitle())  # True  -> har word ka pehla letter capital hai

str1 = "To kill a mockinf bird"
print(str1.istitle())  # False  -> 'kill', 'a', 'mockinf' lowercase hain

# Kya string 'Python' se start ho rahi hai?
str1 = "Python is a Interpreted Language"
print(str1.startswith("Python"))  # True  -> 'Python' se start ho rahi hai

# Jo lowercase me tha wo UPPER ho jayega aur vice versa
print(str1.swapcase())  # 'pYTHON IS A iNTERPRETED lANGUAGE'

# Har word ka first letter capital ho jayega (title case)
str1 = "His name is Dan. He is an honest man."
print(str1.title())  # 'His Name Is Dan. He Is An Honest Man.'
