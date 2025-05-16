# Day03 - Variables and Data Types

# Here we are defining variables of different data types:

int = 1                # This is an integer data type (whole number).
float = 2.5            # This is a floating point number (decimal number).
boolean = False        # This is a boolean value, which can either be True or False.
string = "Hello"       # This is a string (sequence of characters).
noneType = None        # This is the 'None' type, used for 'null' values.
comp = complex(8,2)    # This creates a complex number with real part 8 and imaginary part 2.

# Now we print the values of the variables:

print(int)             # Prints the integer value 1
print(boolean)         # Prints the boolean value False
print(string)          # Prints the string "Hello"
print(noneType)        # Prints the None value, which represents 'null'
print(comp)            # Prints the complex number (8+2j)


# Checking and printing the type of each variable:

print("The type of int is", type(int))           # Output: <class 'int'>
print("The type of float is", type(float))       # Output: <class 'float'>
print("The type of boolean is", type(boolean))   # Output: <class 'bool'>
print("The type of string is", type(string))     # Output: <class 'str'>
print("The type of noneType is", type(noneType)) # Output: <class 'NoneType'>
print("The type of comp is", type(comp))         # Output: <class 'complex'>


# Creating a list (ordered collection of items) that can store different data types:

list1 = [1, 1.2, [-1, 2], ["Hello", "world"], ["Hello"], ["World"]]  # List containing an integer, float, another list, and another list with strings.
print(list1)                                  # Prints the whole list: [1, 1.2, [-1, 2], ['Hello', 'world']]
print(list1[2][0])                            # Prints the first element of the nested list: -1
# list1[4] → ["Hello"]
# list1[5] → ["World"]
# dono lists hain, unka addition concatenate karega
# ["Hello"] + ["World"] → ["Hello", "World"]
print(list1[4] + list1[5])  # Output: ['Hello', 'World']

# list1[4][0] → "Hello" (index 0 of list at index 4)
# list1[5][0] → "World" (index 0 of list at index 5)
# dono strings hain, + se concatenate hoga → "HelloWorld"
print(list1[4][0] + list1[5][0])  # Output: HelloWorld

# Same as above, lekin beech me ek space diya gaya hai
# "Hello" + " " + "World" → "Hello World"
print(list1[4][0] + " " + list1[5][0])  # Output: Hello World


# A tuple is like a list, but it is immutable (we cannot change the elements once created):

tuple1 = [("Apple", "Mango"), ("Banana", "Papaya")]
print(tuple1)   # Prints the tuple: [('Apple', 'Mango'), ('Banana', 'Papaya')]


# Creating a dictionary, which is a collection of key-value pairs:

dict1 = {"Name": "Aksh", "Gender": "Male", "Age": 15, "canVote": False}
print(dict1)  # Prints the dictionary: {'Name': 'Aksh', 'Gender': 'Male', 'Age': 15, 'canVote': False}
print(dict1["Name"]) # Output: Aksh
