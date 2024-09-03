# tuple = collection which is ordered and uncahngeable used to group together related data

student = ("Kunal", 26, "male")
print(student.count("Kunal"))
print(student.index("male"))

for x in student:
    print(x)
if "Kunal" in student:
    print("Kunal is present!")