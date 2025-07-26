#day06 - Taking Input from User

# input() function ka use karke user se naam pucha ja raha hai
# Yeh jo input doge, wo hamesha string (text) ke form mein aata hai
nameInput = input("Enter your name:")  
print("Your name is", nameInput)  # Jo naam user ne diya usse print kar rahe hain

# Ab 2 numbers user se input le rahe hain
numInput1 = input("Enter your first number:")  # Yeh bhi string hi hoga
numInput2 = input("Enter your second number:")

# Yahaan dono inputs ko add kar rahe hain bina convert kiye
# Dono values string hain, toh yeh string concatenation karega
# Example: agar user 2 aur 3 input karta hai toh output hoga "23"
print(numInput1 + numInput2)

# Ab dono inputs ko int() function se integer mein convert kar ke add kar rahe hain
# Example: 2 + 3 = 5
print(int(numInput1) + int(numInput2))
