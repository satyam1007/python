#day43 - read(), readlines() and other methods

f = open('myfile_3.txt', 'r') # 'myfile.txt' ko 'r' (read) mode mein open kiya.
i = 0 # Ek counter 'i' initialize kiya 0 se.
while True: # Ek infinite loop shuru kiya.
  i = i + 1 # Har iteration mein 'i' ko badhaya.
  line = f.readline() # File se ek line padhi.
  if not line: # Agar line empty hai (matlab file ka end aa gaya hai), toh loop tod do.
    break
  m1 = int(line.split(",")[0]) # Line ko commas (',') se split kiya aur pehle part ko integer mein convert karke 'm1' mein store kiya.
  m2 = int(line.split(",")[1]) # Dusre part ko integer mein convert karke 'm2' mein store kiya.
  m3 = int(line.split(",")[2]) # Teesre part ko integer mein convert karke 'm3' mein store kiya.
  print(f"Marks of student {i} in Maths is: {m1*2}") # Student ke Maths ke marks (m1*2) print kiye.
  print(f"Marks of student {i} in English is: {m2*2}") # Student ke English ke marks (m2*2) print kiye.
  print(f"Marks of student {i} in SST is: {m3*2}") # Student ke SST ke marks (m3*2) print kiye.

  print(line) # Original line ko bhi print kiya.
# Note: Is code mein f.close() missing hai, jo achhi practice nahi hai. Ideally, file ko loop ke baad close karna chahiye.
f.close()


f = open("myfile_4.txt", "w") # 'myfile_4.txt' ko write mode ('w') mein open kiya. Agar yeh file pehle se exist karti hai toh uska content delete ho jayega, aur agar nahi karti toh nayi file ban jayegi.
lines = ['line 1st\n', 'line 2nd\n', 'line 3rd\n'] # Ek list banayi hai jismein teen strings hain, har string ke end mein `\n` (newline character) hai taki har line alag-alag aaye.
f.writelines(lines) # `writelines()` method use karke list ki saari strings ko file mein likha gaya hai.
f.close() # File ko band kiya gaya hai.
