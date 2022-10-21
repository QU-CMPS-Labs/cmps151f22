from multiprocessing.context import SpawnContext

stars = 8
n = stars+1
space = 1

while(space != 0):
    # draw space
    space = stars//2

    for j in range (0, space) :
        print(' ', end= '')

    # display the stars

    for j in range (0, n-stars):
        print('*' , end= '')

    stars-=2
    print('\n')