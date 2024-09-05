# scope = the region that a variable is recognized
#         a variable is only available from inside the region it is created
#         a global and locally scoped versions of a variable can be created
# L.E.G.B rule:
# local
# enclosing
# global
# built-in


# global variable (available inside & outside functions)
name = "Kunal"
def display_Name():
    # local variable (available only inside this function)
    name = "Shenoy"
    print(name)

display_Name()
print(name)