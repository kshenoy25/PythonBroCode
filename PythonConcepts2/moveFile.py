import os
# you can accomplish moving directories as well
# source = "folder"
source = "test.txt"
destination = "/Users/k-shenoy/Desktop/test.txt"
#destination = "/Users/k-shenoy/Desktop/folder"
try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source + " was moved successfully")
except FileNotFoundError:
    print(source + " was not found")