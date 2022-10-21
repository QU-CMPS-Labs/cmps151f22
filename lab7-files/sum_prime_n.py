n = int(input("Enter the value of n: "))
sum = 0
for i in range(2, n):
    is_prime = True
    
    for j in range(2, i):
        if (i % j) == 0:
            is_prime = False
            break
    
    if is_prime:
        sum += i
        print(i)

print("Sum of prime numbers is", sum)