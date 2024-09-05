# *kwargs = parameter that will pack all arguments into a dictionary
#           useful so that a function can accept a varying amount of keyword arguments

#def hello(first, last):

# can have any naming convention but make sure that ** is assigned
def hello(**kwargs):
    #print("Hello " + kwargs['First'] + " " + kwargs['Last'])
    print("Hello", end =" ")
    for key, value in kwargs.items():
        print(value, end= " ")

hello(title= "Mr.", first= "Kunal", last= "Shenoy")