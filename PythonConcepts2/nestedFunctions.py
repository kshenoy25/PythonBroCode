# nested function calls = function calls inside other function calls
#                         innermost function calls are resolved first
#                         returned value is used as argument for the next outer function

#num = int(input("Enter a positve number: "))
#um = float(num)
#num = abs(num)
#num = round(num)
#print(num)


print(round(abs(float(input("Enter a positive number: "))))) # extreme example of nested function calls