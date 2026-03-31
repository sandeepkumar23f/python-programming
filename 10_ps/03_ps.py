class Demo:
    a = 4

o = Demo()
print(o.a)
o.a = 0
print(o.a)
print(Demo.a) # output will be 4 so it does not change the class attribute