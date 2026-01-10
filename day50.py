# day50 - Constructors in Python

# ---------------- CLASS DEFINITION ----------------
# Person ek class hai (blueprint)

class Person():
    
    # ---------------- CONSTRUCTOR ----------------
    # __init__() ek special method hota hai
    # object banate hi automatically call ho jata hai
    def __init__(self, n, o):
        # self current object ko refer karta hai
        # n aur o se values lekar object ke variables set kar rahe hain
        self.name = n
        self.occ = o

    # ---------------- METHOD ----------------
    # info() object ki details print karega
    def info(self):
        print(f"{self.name} is {self.occ}")


# ---------------- OBJECT CREATION ----------------
# object banate time constructor ko values pass karni padti hain

b = Person("Satish", "Software Engineer")
# yahan __init__ automatically call hua
# self.name = "Satish"
# self.occ = "Software Engineer"
b.info()
# Output: Satish is Software Engineer


c = Person("Sam", "Software Developer")
# yahan __init__ dobara call hua
c.info()
# Output: Sam is Software Developer


# ---------------- ERROR EXAMPLE ----------------
# Agar constructor mein 2 parameters hain
# aur hum zyada ya kam values denge to error aayega

# d = Person(1, 2, 3)   ❌ TypeError
# Kyunki constructor sirf 2 arguments expect karta hai
