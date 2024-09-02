# logical operators (abd, or, not) = used to check if two or more conditional are true

temp = int(input("What is the temperature outside?: "))

if not(temp >= 0 and temp <= 30):
    print("The temperature is bad today!")
    print("Stay insside brrrrrr!")

    #print("The temperature is good today!")
    #rint("Go outside!")

elif not(temp < 0 or temp > 30):
    #print("The temperature is bad today!")
    #print("Stay insside brrrrrr!")

    print("The temperature is good today!")
    print("Go outside!")