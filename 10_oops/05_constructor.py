class Employee:
    language = "Python"
    salary = 1000000
    def __init__(self,name,age,salary):  # dunder method which is automatically called
        self.name = name
        self.age = age
        self.salary = salary
        print("I am creating an obj")
    def getInfo(self):
        print(f"language is {self.language}. The salary is {self.salary}.")

    @staticmethod
    def greet():
        print("Good Evening")
    


person1 = Employee("Harry",28,1300000)
print(person1.name,person1.age)
person1.getInfo() # or Employee.getInfo(person1)