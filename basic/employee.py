class Employee:
    def __init__(self, ID=None, salary=0, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department

    # defining the properties and assigning them None
    ID = None
    salary = None
    department = None


# cerating an object of the Employee class
Steve = Employee(3789,2500,"Human Resources")
Mark = Employee()

# assigning values to properties of Steve - an object of the Employee class
Steve.ID = 3789
Steve.salary = 2500
Steve.department = "Human Resources"
# creating a new attribute for Steve
Steve.title = "Manager"

# Printing properties of Steve
print("ID =", Steve.ID)
print("Salary", Steve.salary)
print("Department:", Steve.department)
print("Title:", Steve.title)
print("Mark")
print("ID =", Mark.ID)
print("Salary", Mark.salary)
print("Department:", Mark.department)