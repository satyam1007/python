#day40 - os Module in Python

import os
# os.mkdir("data")

# if (not os.path.exists("data")):
#   os.mkdir("data")

# for i in range(0, 100):
#   if i < 9:
#     with open(os.path.join(f"data", f"day0{i+1}.py"), 'w') as file:
#       pass
#   else:
#     with open(os.path.join(f"data", f"day{i+1}.py"), 'w') as file:
#       pass

# ==> A. Working with the File System
cwd = os.getcwd()
# Get current working directory
print(cwd)
# Change current directory ==> os.chdir("/path/to/folder")
# List files in a directory
files = os.listdir(".")  # "." means current folder
print(files)

# ==> B. Creating & Removing Folders
# Create a single folder
os.mkdir("new_directory")
# Create nested folders
os.makedirs("parent/child/grandchild")
# Remove empty folder
os.rmdir("new_folder")
# Remove nested folders
os.removedirs("parent/child/grandchild")

# ==> C. File and Path Operations
# Join paths safely (cross-platform)
path = os.path.join("folder", "file.txt")
# Check if a path exists
print(os.path.exists(path))
# Check if it’s a file or directory
print(os.path.isfile(path))
print(os.path.isdir(path))

# ==> D. Environment Variables
# Get value
user = os.environ.get("USER") # or "USERNAME" on Windows
print(user)

# Set value
os.environ["MY_VAR"] = "Hello"

# ==> E. Running System Commands
os.system("echo Hello from OS!") # Executes a shell command
# Use carefully — direct shell commands can be risky.

# ==> F. File Metadata
stats = os.stat("day40.py")
print(stats.st_size) # File size
print(stats.st_mtime) # Last modified time