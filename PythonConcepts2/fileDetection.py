import os

pathway = "/Users/k-shenoy/Documents/Folder"
if os.path.exists(pathway):
    print("That location exists")
    if os.path.isfile(pathway):
        print("That is a file")
    elif os.path.isdir(pathway):
        print("That is a directory")
else:
    print("That location does not exist")