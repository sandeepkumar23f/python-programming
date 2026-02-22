f = open("text.txt") # by default open("text.txt") performs the reads operation but if we add open("text.txt","w") then it will for write
data = f.read()
print(data)
f.close()