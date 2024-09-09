import os
import shutil

#os.remove('test2.txt')
#path = "test2.txt"
#path = "file.txt"
path = "newFolder"

try:
    #os.remove(path)
    #os.rmdir(path)
    # be careful when running this due to deletion of small to large files
    shutil.rmtree(path)

#except FileNotFoundError:
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("You do not have permission to delete file")
except OSError:
    print("You cannot do that")
else:
    print(path + " was deleted")
finally:
    print("Cleaning up")