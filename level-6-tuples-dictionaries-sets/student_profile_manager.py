"""
Practice 1: Student Profile Manager

Store:
Name
Age
Branch
City

in a tuple.

Print:
Complete tuple
First value
Last value

"""



def add_student(students):
    name = input("Enter your name: ")

    for student in students:
        if student["name"].lower() == name.lower():
            print("Student already exists.")
            return

    age = int(input("Enter your age: "))
    branch = input("Enter your branch: ")

    student = {
        "name": name,
        "age" : age,
        "branch": branch
    }

    students.append(student)
    print("Student added successfully...")



def search_student(students):
    if len(students) == 0:
        print("No students found!")
        return
    
    else:
        name = input("Enter student name: ")

        for student in students:
            if student["name"].lower() == name.lower():
                print("\nStudent found")
                print("Name: ", student["name"])
                print("Age: ", student["age"])
                print("Branch: ", student["branch"])
                return
        else:
            print("Student not found!")



def update_student(students):
    if len(students) == 0:
        print("No students found!")
        return
    
    else:
        name = input("Enter student name: ")

        for student in students:
            if student["name"].lower() == name.lower():
                print("Current details: ")
                print(student)

                print("Please update the datails.")
                student["age"] = int(input("Enter new age: "))
                student["branch"] = input("Enter new branch: ")

                print("Student details updated successfully...")
                return

        else:
            print("Student not found")



def delete_student(students):
    if len(students) == 0:
        print("No students found!")
        return
    
    else:
        name = input("Enter student name: ")

        for student in students:
            if student["name"].lower() == name.lower():
                students.remove(student)
                print("Student deleted successfully!")
                return
            
        else:
            print("Student not found")



def show_students(students):
    if len(students) == 0:
        print("No students found!")
        return
    
    else:
        print("\n--- Students list ---\n")

        for i, student in enumerate(students, 1):
            print(f"\nStudent {i}: ")
            print("Name: ", student["name"])
            print("Age:", student["age"])
            print("Branch:", student["branch"])



def main():
    students = []

    while True:
        print("==== Student Profile Manager ====\n")
        print("1. Add Student\n2. Search Student\n3. Update Student\n4. Delete Student\n5. Show All Students\n6. Exit\n")

        try:
            choice = int(input("Select operation (1-6): "))

        except ValueError:
            print("Please enter numbers only! ")
            continue


        if choice == 1:
            add_student(students)

        elif choice == 2:
            search_student(students)

        elif choice == 3:
            update_student(students)

        elif choice == 4:
            delete_student(students)

        elif choice == 5:
            show_students(students)

        elif choice == 6:
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


main()