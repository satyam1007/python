#day08 - Strings Slicing and Operations on Strings in Python 
fruit  = "mango"
mangoLen = len(fruit)

print(mangoLen)

print(fruit[0:4]) # ==> 0 starting point hai aur 4 stopping point hai. 0 include hota hai lekin 4 include nahi hota.
print(fruit[1:4])

print(fruit[:5])

print(fruit[0:-3])

print(fruit[:len(fruit)-3])

print(fruit[-1:len(fruit)-3]) # ===> start = -1 ('o'), stop = -3 ('n'), left to right But -1 > -3 so Python won't extract anything in default (forward) slicing.

# start = -1 → this is character 'o'
# stop = -4 → this is character 'a' (but not included in the result)
# step = -1 → so we are moving backwards
print(fruit[-1:-4:-1])

print(fruit[-3:-1])
# fruit[-3:-1] ka matlab:
# Start at -3 → 'n'
# Stop before -1 → 'o' se pehle → 'g' tak