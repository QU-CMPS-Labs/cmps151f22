def digits(n):
    count = 0
    while(n > 0):
        n = n//10
        count+=1
    
    return count

def digits2(n):
    return len(str(n))

    
def main():
    n = int(input("Enter the number to find the number of digits"))
    print("The number of digits in ", n, " is ", digits(n))

main()