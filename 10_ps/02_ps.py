class Calculator:
    def __init__(self,n):
        self.n = n
    def square(self):
        print(f"The square is {self.n*self.n}")
    def cube(self):
        print(f"The Cube is {self.n*self.n*self.n}")
    def squareRoot(self):
        print(f"The square root is {self.n**1/2}")

n = Calculator(4)
n.square()
n.cube()
n.squareRoot()