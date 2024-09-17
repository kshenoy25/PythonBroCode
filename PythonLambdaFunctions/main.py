# lambda functions = function written in 1 line using lambda keyword
#                    accepts any number of arguments, but only one has expression
#                    (like a shortcut) and useful if needed for a short period of time - throw away


#def double(x):
#    return x * 2

#print(double(5))

double = lambda x:x * 2
multiply = lambda x,y:x * y
add = lambda x,y,z: x + y + z

full_name = lambda first_name, last_name: first_name + " " + last_name
age_check = lambda age:True if age >= 18 else False

print(double(5))
print(multiply(5,1))
print(add(34,12,23))

print(full_name("Kunal", "Shenoy"))
print(age_check(26))
