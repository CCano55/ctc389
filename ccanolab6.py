# Cesar Cano
# Lab 6
# Modifying Python Lists

students = ["Cesar", "Alex", "Sebastien", "Fernando", "Camilo"]

print("Student List")

for i in students:
    print(i)


print("1. Add student to list")
print("2. Modify student name")
print("3. Remove student")

choice = int(input("Choose an option: "))


if choice == 1:

    new_student = input("Enter student name: ")

    students.append(new_student)

    print("New Student List")

    for i in students:
        print(i)


elif choice == 2:

    index = 0

    for i in students:
        print(index, i)
        index = index + 1

    student_index = int(input("Enter the index number you want to change: "))

    new_name = input("Enter the new student name: ")

    students[student_index] = new_name

    print("New Student List")

    for i in students:
        print(i)


elif choice == 3:

    index = 0

    for i in students:
        print(index, i)
        index = index + 1

    student_index = int(input("Enter the index number you want to remove: "))

    students.pop(student_index)

    print("New Student List")

    for i in students:
        print(i)
