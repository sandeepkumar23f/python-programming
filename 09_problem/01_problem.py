f = open("poem.txt")
content = f.read()

if("twincle" in content):
    print("Twincle is present in your text")
f.close()