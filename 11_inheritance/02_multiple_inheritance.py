class Employee:
    company="ITC"
    name = "Default name"
    def show(self):
        print(f"the name of the employee is {self.name} and company is {self.company}")

class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"The language of all the employee is {self.language}")


class Programmer(Employee,Coder):
    company = "ITC infotech"
    def showLanguage(self):
        print(f"name is {self.company} and he is good with {self.language} language")

a = Employee()
b = Programmer()
b.show()
b.showLanguage()
b.printLanguage()