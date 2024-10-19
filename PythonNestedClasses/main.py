# nested class = a class defined within another class
#                   class outer:
#                       class Inner:

# benefits : allows you to logically group classes that are closely related and encapsulates private details that aren't
#            relevant outside the outer class
#            keeps the namespace clean; reduces the possibility of naming conflicts

class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_details(self):
            return f"{self.name} {self.position}"

    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)

    def list_employees(self):
        return [employee.get_details() for employee in self.employees]


company1 = Company("John's Grocery")
company2 = Company("Facebook")

company1.add_employee("Chris", "Department Manager")
company1.add_employee("Javi", "THC Manager")
company1.add_employee("Kunal", "Tech Consultant")

company2.add_employee("Sarah", "Department Manager")
company2.add_employee("Mark","CEO")
company2.add_employee("Edwardo","CFO")
#print(company.list_employees())
print(company2.company_name)
for employee in company2.list_employees():
    print(employee)

print("*******************")

print(company1.company_name)
for employee in company1.list_employees():
    print(employee)