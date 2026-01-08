#day45 -  Lambda functions in Python

# 1. Normal Tareeka: 'def' keyword se function banana
def double(x):
    return x*2

# --- HIGHER ORDER FUNCTIONS IN PYTHON ---

# 1. Pehle ek simple function banate hain jo cube nikalta hai
def cube(x):
    return x * x * x  # Yeh number ko 3 baar multiply karega (x^3)

# 2. Ab 'appl' function define karte hain
# 'fx' yahan ek "function" hai jo hum pass karenge
def appl(fx, value):
    # fx(value) ka matlab hai: jo function pass kiya usse value ke saath run karo
    # Phir jo result aaye usmein 6 add kar do
    return 6 + fx(value)

# 3. Execution: 'cube' function ko 'appl' ke andar pass kiya
print(appl(cube, 2))

# --- STEP-BY-STEP LOGIC ---
# Step 1: appl(cube, 2) call hua -> fx ban gaya 'cube' aur value ban gayi '2'
# Step 2: fx(value) execute hua -> yani cube(2) calculate hua -> Result aaya 8
# Step 3: return 6 + 8 execute hua -> Result aaya 14
# Step 4: Final Output screen par 14 print ho gaya

# 2. Lambda Tareeka: Bina naam ka chhota function (Anonymous Function)
# double = lambda input: expression
double = lambda x: x*2       # Yeh 'x' lega aur 'x*2' return karega
cube = lambda x: x*x*x       # Yeh 'x' lega aur uska cube return karega
avg = lambda x, y: (x+y)/2   # Lambda mein multiple arguments (x, y) bhi de sakte hain

# 3. Basic Calls:
print(double(2))  # Output: 4 (2*2)
print(cube(3))    # Output: 27 (3*3*3)
print(avg(3, 5))  # Output: 4.0 ((3+5)/2)

# Yahan humne koi purana function nahi bheja,
# balki on-the-spot ek naya lambda function bana kar bhej diya!
print(appl(lambda x: x*x, 2)) 

# --- Is Last Line Ka Logic ---
# 1. 'appl' function call hua: fx = (lambda x: x*x) aur value = 2
# 2. fx(value) run hua -> (lambda 2: 2*2) -> Answer aaya 4
# 3. appl ne return kiya: 6 + 4 = 10
# Final Output: 10
