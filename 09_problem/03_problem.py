import os
def generateTable(n):
    os.makedirs("table",exist_ok=True)
    table = ""
    for i in range(1,11):
        table += f"{n} X {i} = {n*i}\n"
        with open(f"table/table_{n}", "w") as f:
            f.write(table)


for i in range(2,21): # i need the table from 2 to 20 so i taken the 21
    generateTable(i)
