# nested loop = the "inner loop" will finish all of its iterations before
#               finishing one iteration of the "outer loop"

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
symbol = input("Enter symbol: ")

for i in range(rows):
    for j in range(cols):
        # after using print statement "end" will prevent cursor from moving down to the next line
        print(symbol, end="")
    print()
