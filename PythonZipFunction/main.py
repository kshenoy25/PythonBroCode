# zip(*iterables) = aggregate elements from two or more iterables (list, tuples, set, etc.)
#                   creates a zip object with paired elements stored in tuples for each element

username = ["Dude", "Bro", "Mister"]
passwords = ["PASSWORD", "<sbc123", "guest"]
login_date = ["1/1/2024", "1/2/2024", "1/3/2024"]

users = zip(username, passwords, login_date)
for i in users:
    print(i)

#users = dict(zip(username, passwords))
#print(type(users))

#for key,value in users.items():
#   #print(i)
#    print(key+" : "+value)