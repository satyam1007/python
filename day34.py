#day34 - Secret Code Language

# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

# 1. Mujhe ye karna hoga ki pehle ek list bana lo uske baad usme words daal do phir for loop se usey print karana he aur phir ye logic lagana he ki agar list ke ander ke words ka length 3 yaa 3 ke barabar he to yes print karo yaa phir no print karo

words = ["Eat", "Tea", "Sweet", "Treet", "Dog", "World", "Cat", "Hello", "Two"]

encoded_words = []

print("Encoded Words:")
for item in words:
    if len(item) <= 3:
        transformed = "cid" + item[1:] + item[0] + "dic"
        encoded_words.append(transformed)
    else:
        encoded_words.append(item[::-1])  # reverse
    print(encoded_words[-1])

print("Before Decoding The Elements\n")

print("After Decoding The Elements:")
decoded_words = []

for word in encoded_words:
    if word.startswith("cid") and word.endswith("dic"):
        middle = word[3:-3]  # remove 'cid' and 'dic'
        original = middle[-1] + middle[:-1] # middle[-1] = 'C' (last character)
                                            # middle[:-1] = 'at' (everything except the last)
        decoded_words.append(original)
    else:
        decoded_words.append(word[::-1])  # reverse again to restore
    print(decoded_words[-1])
