class Employee:
    language = "Python"
    salary = 1000000
    def getInfo(self):
        print(f"language is {self.language}. The salary is {self.salary}.")
        
    @staticmethod
    def greet():
        print("Good Evening")

person1 = Employee()
person1.getInfo() # or Employee.getInfo(person1)

person1.greet()