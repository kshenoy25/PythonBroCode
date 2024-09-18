# sort() method = used with lists
# sort() function = used with iterables

# list of tuples
#students = [
#   ("Haley", "F", 23, 26),
#       ("Kunal", "A", 90, 26),
#        ("Parker", "B", 86, 23),
#        ("Lexi", "D", 66, 22),
#        ("Abby", "C", 75, 26)]


new_students =(("Haley", "F", 23, 26),
            ("Kunal", "A", 90, 26),
            ("Parker", "B", 86, 23),
            ("Lexi", "D", 66, 22),
            ("Abby", "C", 75, 26))

# key word argument with sorting
#grade = lambda grades:grades[1]

age = lambda ages:ages[2]
#students.sort(key = age)  #reverse = True
# using tuples of tuples
student_sorted = sorted(new_students, key=age)

for j in student_sorted:
    print(j)