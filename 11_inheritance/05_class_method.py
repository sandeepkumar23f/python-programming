class Employee:
    a = 1
    @classmethod # by the help of it it will print the class attribute
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 45
e.show()