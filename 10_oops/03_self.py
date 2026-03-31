class Employee:
    language = "Python"
    salary = 1000000
    def getInfo(self):
        print(f"language is {self.language}. The salary is {self.salary}.")

person1 = Employee()
person1.getInfo() # or Employee.getInfo(person1)
# agar hum def getInfo(self) na kre to ye hume 1 argument na hone ka error dega kyonki actually 
# person1.getInfo() hi Employee.getInfo(person1) hota hai so yaha Employee.getInfo(person1) ek argument le raha hai