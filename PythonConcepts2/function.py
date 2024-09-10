# function = a block of code which is executed only when it is called (invoking a function )

def hello(first_name, last_name, age):
    print("Hello " + first_name + " " + last_name )
    print("You are " + str(age) + " years old")
    print("Have a nice day!")

hello("Kunal", "Shenoy", 26)

def funca (name, age = 22):
    print(name,age)
funca("Jack", 23)


def funcb (input):
    print(input + " programming language")
funcb("python")

def fun(a1 = 1, a2 = 9):
    print(f"The numbers lies between {a1} to {a2}")
fun(10,19)

def funcx (b1, b2):
    b1 = 2
    b2 = 3
    print(b1," " ,b2)
funcx()


def fun1(val):
    return val + 34
x = fun1(-34)
print(x)
#my_name = "Haley"

#hello("Kunal")
#hello("Dude")


