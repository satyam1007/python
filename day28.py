#day28 - Dictionaries in Python

# Ek simple dictionary banayi gayi hai jisme teen key-value pairs hain
info = {'name':'Karan', 'age':19, 'eligible':True}

# Yahan dictionary se 11 key ko access karne ki koshish ki gayi hai
# Lekin 11 key dictionary mein exist nahi karti, isliye yeh line error degi
# print(info[11])

# get() method use karte hain jo error nahi deta, agar key nahi mile to None return karta hai
print(info.get(112))

# keys() method se dictionary ke saare keys ka list milta hai
print(info.keys())

# values() method se dictionary ke saare values ka list milta hai
print(info.values())

# items() method se dictionary ke saare key-value pairs tuple ke form mein milte hain
print(info.items())

# is loop mein sirf keys ko access karke unki values print kar rahe hain
for key in info.keys():
  print(info[key])

# is loop mein key aur value dono ko ek saath access karke print kar rahe hain
for key, value in info.items():
  print(f"The value of corresponding to the key {key} id {value} ")
