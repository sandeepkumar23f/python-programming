n = int(input("Enter the size of list: "))
a = []
target = int(input("Enter the target element: "))
ans = -1
for i in range(n):
    a.append(int(input("Enter element: ")))

low = 0
hi = n-1

while low<=hi:
    mid = (hi+low)//2
    if a[mid]==target:
        ans = mid
        break
    elif a[mid]<target:
        low = mid+1
    else:
        hi = mid-1
    

print(ans)