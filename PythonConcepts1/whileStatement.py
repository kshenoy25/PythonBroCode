# while statement = a statement that will execute its block of code,
#                   as long as the condition is true


name = ""
#while len(name) == 0:
while not name:
    name = input("Enter your name: ")

print ("Hello " + name)
