import os
f = open("file1.txt", "x")
path = os.path.abspath("file.txt")
print(path) #prints the full path of the file created above
