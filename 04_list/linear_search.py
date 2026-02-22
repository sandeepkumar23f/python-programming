a = [2,1,4,3,5,6,8,7]
n = a.__len__()
ans = 0
target = int(input("Enter target"))
for i in range(n):
    if(a[i] == target):
        ans = i
        break


print(ans)