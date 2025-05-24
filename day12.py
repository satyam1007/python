#day12 - Match Case Statements in Python 

# User se ek input le rahe hain, aur usse int (integer) mein convert kar rahe hain
x = int(input("Enter your first digit number: "))

# Yahan se match-case block start ho raha hai (Python 3.10+ ka feature hai)
match x:
  
  # Agar x ki value 0 hai, to yeh block chalega
  case 0:
    print("The value of x is ", x)

  # Agar x ki value 4 hai, to yeh block chalega
  case 4:
    print("The value of x is ", x)

  # Agar x ki value 90 **nahi** hai (x ≠ 90), to yeh block chalega
  # Dhyan rahe: yeh condition mostly TRUE hoti hai, sirf jab x == 90 ho tabhi skip hoti hai
  case _ if x != 90:
    print(x, "is not 90")

  # Agar x ki value 80 **nahi** hai (x ≠ 80), to yeh chalega
  # Lekin upar wali condition (x ≠ 90) agar TRUE ho gayi to yeh block tak kabhi pahunchega hi nahi
  case _ if x != 80:
    print(x, "is not 80")

  # Agar upar ke sabhi cases match nahi karte, tab yeh default block chalega
  # Yeh tab chalega jab x == 90 AND x == 80 ho (matlab x = 80 hoga to hi yeh chalega)
  case _:
    print(x)
