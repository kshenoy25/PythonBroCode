
#text = "Yooooo\nThis is some text looool"
text = "Have a nice day!"

with open('../PythonFiles/new.txt', 'a') as file:
    file.write(text)