n = int(input("Enter the number "))
flag = True
if n == 0:
    print("Your number is neither prime nor composite")
else:
    for i in range(2,n):
        if n % i == 0:
            flag=False
    

if flag == True:
    print("Your number is prime")
else:
    print("Your number is composite")