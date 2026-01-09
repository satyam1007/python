# day49 - Classes and Objects in Python

# ---------------- CLASS DEFINITION ----------------
# Person ek class hai (blueprint)
# Class ke andar properties (variables) aur methods (functions) hote hain

class Person():
    
    # Class variables (default values)
    name = "harry"
    age = 23
    occupation = "Software Engineer"

    # Method (function inside class)
    # self ka matlab hai current object
    def info(self):
        # object ki name aur occupation print karega
        print(f"{self.name} is a {self.occupation}")


# ---------------- OBJECT CREATION ----------------
# Person class ka object banaya gaya
person1 = Person()

# person1 object ka info method call kiya
person1.info()
# Output: harry is a Software Engineer


# ---------------- MULTIPLE OBJECTS ----------------
# same class se multiple objects ban sakte hain
a = Person()
b = Person()

# a object ke values change kar rahe hain
a.name = "Rahul"
a.occupation = "HR"

# a ka info print hoga
a.info()
# Output: Rahul is a HR


# b object ke values change kar rahe hain
b.name = "Rohit"
b.occupation = "Senior Software Developer"

# b ka info print hoga
b.info()
# Output: Rohit is a Senior Software Developer


# ---------------- ACCESSING OBJECT DATA ----------------
# person1 ke attributes print kar rahe hain
print(person1.name)        # harry
print(person1.age)         # 23
print(person1.occupation) # Software Engineer


# ---------------- MODIFY OBJECT DATA ----------------
# person1 ka name change kar rahe hain
person1.name = "prince"

# updated name print hoga
print(person1.name)        # prince
