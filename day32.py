#day32 - Finally keyword in Python

'''
The finally block always executes, whether an exception occurs or not. It’s used for cleanup (e.g., closing files).
'''

'''
==> Syntax
try:
    # Risky code
except:
    # Handle error
finally:
    # Always runs (even if error occurs)
'''

def func1():
  try:
    l = [1,2,3,4]  # Ek list banayi jisme 4 elements hain: index 0 to 3
    i = int(input("Enter the index: "))  # User se index input liya (string ko int mein convert kiya)
    print(l[i])  # List ke i-th index ka element print kiya
    return 1     # Agar sab kuch sahi raha to 1 return kiya
  except:
    print("Some Error occurred")  # Agar try block mein koi error aaya (e.g. galat index ya non-integer input)
    return 0     # To 0 return kiya
  finally:
    print("I am always executed")  # Yeh line har haal mein chalegi — error aaye ya na aaye, return ho ya na ho
    # print("I am always executed")  # (Extra comment ki line — ignore kar sakte ho)

# func1() function ko call kiya aur uska return value x mein store kiya
x = func1()

# x ko print kiya — ya to 1 ya 0 hoga, depend karta hai upar kya hua
print(x)
