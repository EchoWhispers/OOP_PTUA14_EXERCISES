class Employee:

    def __init__(self, name, lname):
        self.name = name
        self.lname = lname

    def __str__(self):

        return (
            f"Your full name is : {self.name} {self.lname}\n"
            f"Your email address is : {self.name}.{self.lname}@company.com".lower())
name = input("Enter your first name: ")
lname = input("Enter your last name:")

a = Employee(name= name, lname= lname)
print(a)