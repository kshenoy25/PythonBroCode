class Car:

    # declared outside of the constructor at the class level

    wheels = 4 # class variable

    # creating object of car
    def __init__(self, make, model, year, color):

        # instance variable is declared inside the constructor

        self.make = make # instance variables
        self.model = model  # instance variables
        self.year = year  # instance variables
        self.color = color  # instance variables


    def drive(self):
        print("This " + self.model + "is driving")
    def stop(self):
        print("This " + self.model + "has stopped")