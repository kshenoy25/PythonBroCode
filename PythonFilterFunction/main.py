# filer() = creates a collection of elements from an iterable for which a function returns true

# filter(functino, iterable)

friends = [("Haley", 26),
            ("Kunal", 26),
            ("Parker",23),
            ("Lexi", 22),
            ("Abby", 26)]

age = lambda data:data[1] >= 18

drinking_buddies = list(filter(age,friends))

for i in drinking_buddies:
    print(i)