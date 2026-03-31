class programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin


p = programmer("Harry",1200000,862900)
print(p.company,p.name,p.salary,p.pin)
employee = programmer("Sandeep",200000,841506)
print(employee.company,employee.name,employee.salary,employee.pin)