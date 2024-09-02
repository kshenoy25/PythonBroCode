# if statement = a block of code that will execute if it's condition is true
# order of if statements are something that matter for optimal execution of logic

age = int(input("Enter your age: "))
if age == 100:
    print("You are old af.")
elif age >= 18:
    print("You are an adult.")
elif age < 0:
    print("You have not even been born yet bruh.")
else:
    print("You are a child")