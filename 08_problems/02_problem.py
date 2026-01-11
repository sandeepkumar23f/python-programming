# convert celcius to fahrenhite
# c/5 = (f-32)/9
def f_to_c(f):
    return 5*(f-32)/9


f = int(input("Enter fahrenhite temprature: "))
print(f"{round(f_to_c(f),2)} Degree C")