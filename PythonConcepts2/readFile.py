
try:
    with open('test.txt') as file:
        print(file.read())
except FileNotFoundError:
    print('File not found')
#print(file.closed)