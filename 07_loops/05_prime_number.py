n = int(input("Enter your number "))
if(n==0 or n==1):
    print("0 or 1 is neither prime nor composite")
else:

    flag = True
    for i in range(2,n):
        if(n%i) == 0:
            flag = False
            break
    if(flag==True):
        print("Number is prime")
    else:
        print("Number is not prime")