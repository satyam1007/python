# Day07 - Strings in Python

# Define a string variable 'name' with value "Harry"
name = "Harry"

# Define a multi-line string variable 'apple'
apple = '''He said,
Hi Harry
hey I am a good boy/girl
"I want to wat an apple"
'''

# Print a greeting message followed by the value of the 'name' variable
print("Hello, ", name)

# Print the multi-line string 'apple'
print(apple)

# Print each character of the 'name' string one by one using indexing
print(name[0])  # Prints the first character 'H'
print(name[1])  # Prints the second character 'a'
print(name[2])  # Prints the third character 'r'
print(name[3])  # Prints the fourth character 'r'
print(name[4])  # Prints the fifth character 'y'

# The line below would throw an error because there is no character at index 5
# print(name[5])  # Throws an error (IndexError)

# Print a message indicating that we're going to use a for loop to print characters
print("Let's use a for loop\n")

# Loop through each character in the 'name' string and print them one by one
for character in name:
  print(character)  # Prints each character in the string 'name' on a new line
