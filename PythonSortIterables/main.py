# sort() method = used with lists
# sort() function = used with iterables
# tuples () will not work as they are immutable

#students = ["Haley", "Kunal","Parker", "Abby", "Lexi", "Julia"]
students = ("Haley", "Kunal","Parker", "Abby", "Lexi", "Julia")
#students.sort()
#students.sort(reverse=True)

# using sorted in this way can basically let you override the tuples rules of immutability
sorted_students = sorted(students, reverse=True)
for i in sorted_students:
    print(i)