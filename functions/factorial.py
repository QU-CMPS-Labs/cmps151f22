from importlib.machinery import FrozenImporter

def fact(n) :
    if n == 0 :
        return 1
    else :
        return n * fact(n-1)

def main() :
    y = 0
    for i in range(1,3) :
        y+=i/fact(i)
        if(i < 2):
            print(' ' ,i, '/' ,i+1, '!', end= ' +')
        else:
            print(' ' ,i, '/' ,i+1, '!', end= ' = ')

     
    print('\ny = ', y)

main()