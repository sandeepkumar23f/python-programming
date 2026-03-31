class Employee:
    age = 21 # it is class attribute
    salary = 1000000

person1 = Employee()
person1.name="sandeep"
print(person1.name, person1.age, person1.salary)

person = Employee()
person.name="Rohan" # it is object or instance attribute
print(person.age,person.name, person.salary)

# here name is an object attribute and age and salary is class attribute