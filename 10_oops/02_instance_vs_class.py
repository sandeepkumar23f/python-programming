class Employee:
    language = "Python" # it is class attribute
    salary = 1000000

person1 = Employee()
person1.language="Javascript" #instance attribute
print(person1.language, person1.salary)

# instance attribute take preferance over the class attribute during assignment and retrival