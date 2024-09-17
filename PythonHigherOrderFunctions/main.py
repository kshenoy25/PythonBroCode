# higher order functions = a function that either:
#                          1) accepts a function as an arguments or
#                          2) returns a function (in python, functions are also treated as objects)

def loud(text):
    return text.upper()
def quiet(text):
    return text.lower()

# the higher order function
def hello(func):
    text = func("bombaclat")
    print(text)

hello(loud)
hello(quiet)
