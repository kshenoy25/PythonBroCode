# index operator [] = gives access toa sequence's elements (str, list, tuples)

name = "bob smith"

first_name = name[0:3].upper()
last_name = name[4:].upper()
last_character = name[-2].upper()
last_character1 = name[-2].lower()

print(first_name, last_name)
print(last_character)
print(last_character1)
#print(first_name)
#print(last_name)
#if (name[0].isupper()):
#    name = name.lower()
#print(name)

#if (name[0].islower()):
#    name = name.capitalize()
#print(name)
