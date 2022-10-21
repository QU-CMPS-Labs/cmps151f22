
# def read_file(filename):
#     with open(filename) as file:
#         return file.read()  # read the whole file

# data = read_file('students.txt')
from random import random

counter = 0
with open('students.txt', 'r+') as file:
    data = file.read()
with open('students.txt', 'w') as file:
    count = 1
    for line in data.splitlines():
        if count == 1:
            name = line
        elif count == 2:
            age = int(line)
        elif count == 3:
            count = 0
            score = line
        
            if name == "Hassen":
                age+= 111111
                file.write(name + "\n")
                file.write(str(age) + "\n")
                file.write(score + "\n")
            elif name != "Abdulahi":
                file.write(name + "\n")
                file.write(str(age) + "\n")
                file.write(score + "\n")
            else :
                print("found and deleted record")
                print('{0:10} {1:10} {2:10}'.format(name, age, score))
        
        count += 1

    
    

