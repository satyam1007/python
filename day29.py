#day29 - Dictionary Methods in Python

# Dictionary banaya hai jisme kuch key-value pairs hain
info = {'name':'Karan', 'age':19, 'eligible':True, 12: 7}

# Ek aur dictionary banayi jisme extra info hai
infoExtra = {"surname": "Kumar"}

# update() method use karke infoExtra ko info ke andar merge kar diya\info.update(infoExtra)
# Ab info dictionary mein surname bhi add ho gaya hoga
print(info)

# clear() method dictionary ko completely khali kar deta hai
# info.clear()  # Isko comment kiya hai, warna puri dictionary delete ho jaati
# print(info)

# pop() method se specific key ("name") ko dictionary se hata diya\info.pop("name")
print(info)

# popitem() last inserted key-value pair ko remove karta hai\info.popitem()
print(info)

# del statement se pura dictionary ya specific item delete kar sakte hain
# del info  # Isse puri dictionary delete ho jaati
# print(info)

# yahan sirf "age" key ko delete kiya gaya hai
del info["age"]
print(info)
