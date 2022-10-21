from pip import main


def stars(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print('*', end='')
        print('')

def main():
    n = int(input('Enter a number: '))
    stars(n)

main()
    