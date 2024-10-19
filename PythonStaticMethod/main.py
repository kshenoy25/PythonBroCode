# static methods = a method that belong to a class rather than any object from the class (instance)
#                  usually used for general utility functions.

# instance methods = best for operations on instances of the class (objects)
# static methods = best for utility functions that do not need access to class data

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name}, {self.position}"

    # decorator
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["General Manager", "Cashier", "Beer Manager", "Liquor Manager"]

        return position in valid_positions

employee1 = Employee("Chris", "General Manager")
employee2 = Employee("Mary", "Cashier")
employee3 = Employee("Jack", "Beer Manager")
employee4 = Employee("Mike", "liquor Manager")

print(Employee.is_valid_position("THC Manager"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
print(employee4.get_info())


