# f = open("text.txt")
# lines = f.readlines()
# print(lines,type(lines))
# f.close()

f = open("text.txt")
line = f.readline()
while line != "":
    print(line)
    line = f.readline()

f.close()