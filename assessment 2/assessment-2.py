
n=int(input("Please enter the value of N: "))
sumI=0
sum=0

for i in range(1,n+1):
    sumI+=i
    sum+=sumI/i
    if i==n:
        print(sumI,'/',i, end="")
    else:
        print(sumI,'/',i, "+ ", end="")
print()
print("sum=",sum)
