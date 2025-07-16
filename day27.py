#day27 - Sets Method in Python

# Ek set banaya jisme kuch cities hain
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
print(cities)

# Dusra set banaya jisme kuch aur cities hain
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities2)

# union(): Dono sets ko mila kar ek naya set banata hai (duplicates hata deta hai)
cities3 = cities.union(cities2)
print(cities3)

# update(): cities me cities2 ke elements add kar deta hai
cities.update(cities2)
print(cities)

# intersection(): Dono sets ke common elements batata hai
cities4 = cities.intersection(cities2)
print(cities4)

# intersection_update(): Sirf common elements ko hi cities me rakhta hai
cities.intersection_update(cities2)
print(cities)

# symmetric_difference(): Dono sets ke unique elements ko return karta hai (jo common nahi hain)
cities5 = cities.symmetric_difference(cities2)
print(cities5)

# symmetric_difference_update(): cities me sirf un elements ko rakhta hai jo dono me common nahi hain
cities.symmetric_difference_update(cities2)
print(cities)

# difference(): Jo elements cities me hain lekin cities2 me nahi, unko return karta hai
cities6 = cities.difference(cities2)
print(cities6)

# isdisjoint(): True return karega agar dono sets me koi bhi common element nahi hoga
print(cities.isdisjoint(cities2))

# issuperset(): True agar cities me cities2 ke saare elements ho
print(cities.issuperset(cities2))

# issubset(): True agar cities2 ke saare elements cities me ho
print(cities2.issubset(cities))

# add(): Set me ek naya element add karta hai
cities.add("Hello")
print(cities)

# update(): Ek saath multiple elements add karta hai (yahaan cities2 ke saare)
cities.update(cities2)
print(cities)

# remove(): Specific element ko remove karta hai (agar element nahi mila to error dega)
cities.remove("Hello")
print(cities)

# discard(): remove ki tarah hi hai lekin agar element na ho to error nahi deta
cities.discard("Hello")
print(cities)

# pop(): Random element ko remove karta hai aur usse return bhi karta hai
item = cities.pop()
print(cities)
print(item)

# del cities => Ye poora set hi delete kar dega
# print(cities) => Error aayega kyunki ab ye set exist nahi karega

# clear(): Set ke saare elements ko hata deta hai
cities.clear()
print(cities)

# Ek aur set jisme alag-alag type ke values hain
info = {"Carla", 19, False, 5.9}

# in operator se check kar rahe hain ki "Carla" set me hai ya nahi
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")
