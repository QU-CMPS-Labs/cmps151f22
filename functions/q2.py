def power(x, y):
    mul = 1
    for i in range(y):
        mul *= x
    return mul

print(power(2,3))