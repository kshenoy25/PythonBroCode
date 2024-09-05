# keyword arguments = arguments preceded by an identifier when we pass them to a function
#                     the order of the arguments does not matter, unlike positional arguments
#                     Python knows the names of the arguments that our function receives

def hello(first, middle, last):
    print("Hello " + first + " " + middle + " " + last)

hello(first="Kunal", middle="Big Head", last="Shenoy")
##print(hello("John", "Doe", "Smith"))
