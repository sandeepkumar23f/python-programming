class Employee:
    company="ITC"
    def show(self):
        print(f"the name of the employee is {self.name} and salary is {self.salary}")

class Programmer(Employee):
    company = "ITC infotech"
    def showLanguage(self):
        print(f"name is {self.name} and he is good with {self.language} language")

a = Employee()
b = Programmer()

print(a.company, b.company)