roll = {} # empty dictinory

marks = {
    "Harry": 100,
    "Monu": 34,
    "Donu": 23,
    0: "Marry"
}
print(marks, type(marks))
print(marks["Harry"])
print(marks[0])

# methods in dictinories
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Harry": 99})
print(marks)
marks.update({"Renuka": 100}) # if not available in the dictinory then it will add it
print(marks)
print(marks.get("Shinika"))
print(marks.get("Harry2")) # it will give None as output
print(marks["Harry2"]) # it will throw an error
print(marks.__len__())