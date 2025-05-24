#day17 - Function Arguments in Python

# 🧠 Types of Arguments:

# 1. Positional Arguments

# 2. Keyword Arguments

# 3. Default Arguments

# 4. Variable Length Arguments

# 1. ✅ Positional Arguments
# Yeh sabse basic hote hain. Order matter karta hai.
def student(name, age):
  print(name, "is", age, "years old")

student("Ravi", 20)

# 2. ✅ Keyword Arguments
# Yahaan hum key=value format mein dete hain, order important nahi hota.
student(age=21, name="Sita")

# 3. ✅ Default Arguments
# Agar koi argument naa diya jaye, toh default value use hoti hai.
def greet(name="Guest"):
  print("Hello", name)

greet()
greet("Shiv")

# 4. ✅ Variable Length Arguments
# Kabhi kabhi hume pata nahi hota kitne arguments milenge. Tab ye kaam aata hai.
# 🔸 *args (Tuple banata hai sab arguments ka)
def total(*numbers):
  print(type(numbers))
  sum = 0
  for n in numbers:
    sum += n
    # print("Total is ",sum)
  print("Total is ",sum)

total(10, 20, 30)

# 🔸 **kwargs (Keyword arguments ko dictionary banata hai)
def user_info(**details):
  print(type(details))
  for key, value in details.items():
    print(key, ':', value) # or ==> print(f"{key} : {value}")

user_info(name="Krish", age=20, city="Mumbai")
