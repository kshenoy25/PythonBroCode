# slicing = create a substring by extracting elements from another string
#           indexing[] or slice[]
#           [start: stop: step]

name = "Haley Jo"

# substring 1
#first_name = name[0:5]
#first_name = name[:5]

#last_name = name[6:8]
#last_name = name[6:]

#funky_name = name[0:8:3]
#funky_name = name[::2]

#reversed_name = name[::-1]

#print(first_name)
#print(last_name)
#print(funky_name)
#print(reversed_name)

website1 = "hhtp://google.com"
website2 = "hhtp://wikipedia.com"
slice = slice(7,-4)

print(website1[slice])
print(website2[slice])
