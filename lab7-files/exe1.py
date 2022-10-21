# this will add new student to the exiting list
# you must open the file for appending
def add_student() :
    print('Add Student')
    print('-----------------')
    name = input("Enter Student id: ")
    age = input("Enter Student Name: ")
    score = input("Enter Student Grade: ") 
    with open('students.txt', 'a') as file:
        file.write(name + '\n')
        file.write(age + '\n')
        file.write(score + '\n')

def display_students():
    print('Students')
    print('-----------------')
    with open('students.txt') as file:

        # Helps in displaying it in a tabular format
        print('{0:10} {1:10} {2:10}'.format('Name', 'Age', 'Score'))
        print('---------------------------------')
        while True:
            name = file.readline().strip()
            age = file.readline().strip()
            score = file.readline().strip()
            
            # This will tell us if we have reached the end of the file
            if  not name:
                break
            
            # Helps in displaying it in a tabular format
            print('{0:10} {1:10} {2:10}'.format(name, age, score))
        print('\n')

def display_average() :
    print('Display Average')
    print('-----------------')

    with open('students.txt') as file:
        total = 0
        count = 0
        while True:
            name = file.readline()
            age = file.readline()
            score = file.readline()
            
            if not name or not age or not score:
                break
            total += int(score)
            count += 1
        print('Average is ', total / count)

def display_top() :
    print('Display Top')
    print('-----------------')
    
    with open('students.txt') as file:
        top_name = ''
        top_age = ''
        top_score = 0
        print('Name', ' ' , 'Age', ' ' , 'Score')
        while True:
            name = file.readline().strip()
            age = file.readline().strip()
            score = file.readline().strip()
            
            if  not name:
                break
            if int(score) > top_score:
                top_name = name
                top_age = int(age)
                top_score = int(score)
        
        print(top_name, ' ' , top_age, ' ' , top_score)
        print('\n')

def delete_student():
    print('Delete Student')
    print('-----------------')
    name_to_delete = input("Enter Student name: ")
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
            
                if name != name_to_delete:
                    file.write(name + "\n")
                    file.write(str(age) + "\n")
                    file.write(score + "\n")
                else :
                    print("found and deleted record")
                    print('{0:10} {1:10} {2:10}'.format(name, age, score))
        
        count += 1

def update_student():
    print('Delete Student')
    print('-----------------')
    name_to_update = input("Enter Student name: ")
    with open('students.txt', 'r+') as file:
        data = file.read()
    found = False
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
            
                if name == name_to_update:
                     name = input("Enter new name: ")
                     score = input("Enter new score Score: ")
                     age = input("Enter new age: ")
                     Found = True

                file.write(name + "\n")
                file.write(str(age) + "\n")
                file.write(score + "\n")
        count += 1
    if not found:
        print("Student not found")
    else :
        print("Student updated")

def read_file(filename):
    with open(filename) as file:
        return file.read()  # read the whole file

def write_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

def search_student():
    wanted_student = input("enter the name")
    with open('students.txt') as file:
        while True:
            name = file.readline()
            age = file.readline()
            score = file.readline()
            
            if not name or not age or not score:
                break
            if name == wanted_student:
                return name, age, score
    return "Student not found"

def menu() :
    print('1. Add Student')
    print('2. Display Students')
    print('3. Display Average')
    print('4. Display Top')
    print('5. Delete Student')
    print('6. Search Student')
    print('7. Update Student')
    print('8. Exit')


def main():
    print('Student Management System')
    print('-----------------')
    
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            display_average()
        elif choice == '4':
            display_top()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            search_student()
        elif choice == '7':
            update_student()
        elif choice == '8':
            break

main()
