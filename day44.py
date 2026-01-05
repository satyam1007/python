with open("file.txt", "r") as f:
  print(type(f))      # Yeh batayega ki 'f' kis tarah ka object hai (TextIOWrapper).
  f.seek(10)          # Cursor ko jump kara kar sidha 10th character (index) par le jayega.
  print(f.tell())     # Yeh check karega ki cursor abhi kaunsi position par hai (Output: 10).
  data = f.read(5)    # 10th position se agle 5 characters read karega.
  print(data)         # Unn 5 characters ko print kar dega.

with open("sample.txt", "w") as f:
  f.write("Hello World") # File mein "Hello World" likh diya (11 characters).
  f.truncate(5)          # File ko sirf 5 bytes/characters tak limit kar diya.

with open("sample.txt", "r") as f:
  print(f.read()) # Output aayega: "Hello"
