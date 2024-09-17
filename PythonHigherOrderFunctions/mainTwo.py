# higher order functions = a function that either:
#                          1) accepts a function as an arguments or
#                          2) returns a function (in python, functions are also treated as objects)



def divisor(x):
    def dividend(y):
        return y/x

    return dividend

# q = quotient | easier for code readability
q = divisor(2)
print(q(10))