# nested class = a class defined within another class
#                   class outer:
#                       class Inner:

# benefits : allows you to logically group classes that are closely related and encapsulates private details that aren't
#            relevant outside the outer class
#            keeps the namespace clean; reduces the possibility of naming conflicts

class Company:
    class Employee:
        pass

    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, name, position):
        pass

    def lsit