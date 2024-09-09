# exception = events detected during execution that interrupt the flow of a program
# for code maintainability and readability handling specific exceptions when they occur is more ideal

try:
    numerator = int(input("Enter a number to divide: "))

    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator

    #print(result)
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero")
except ValueError as e:
    print(e)
    print("Please enter a number")
except Exception as e:
    print(e)
    print("Oops! Something went wrong.")

else:
    print(result)

finally:
    print("This will always execute")
