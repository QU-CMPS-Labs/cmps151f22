def isPrime(n):
    if n == 1:
        return False
    else:
        for x in range(2, n):
            if n % x == 0:
                return False
        return True

def main():
    n = int(input('Enter a number: '))
    if isPrime(n):
        print(n, 'is prime')
    else:
        print(n, 'is not prime')

main()