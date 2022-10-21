def digits(n) :
    count = 0
    while n > 0 :
        n = n // 10
        count += 1
    return count

def main() :
    n = int(input('Enter a number: '))
    print('The number of digits in', n, 'is', digits(n))

main()