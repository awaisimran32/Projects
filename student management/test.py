student = {'Awais': 915, 'Taha': 811}


def add_students(name, grade):
    student[name] = grade
    print(f"Added {name} with grade {grade}")


def update_student(name, grade):
    if name in student:
        student[name] = grade
        print(f"{name}'s marks are updated to {grade}.")
    else:
        print("Name not found")


def delete_student(name):
    if name in student:
        del student[name]
        print(f"{name} is deleted")
    else:
        print(f"Student {name} not found")


def display_all_students():
    if student:
        for name, grade in student.items():
            print(f"{name}: {grade}")
    else:
        print("No students found")


def main():
    while True:
        print("\n1) Add Student "
              "\n2) Update Student Grade"
              "\n3) Delete Student"
              "\n4) View Students"
              "\n5) Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 5.")
            continue

        if choice == 1:
            name = input("Enter Student Name: ")
            grade = int(input("Enter Student Grade: "))
            add_students(name, grade)
        elif choice == 2:
            name = input("Enter Student Name: ")
            grade = int(input("Enter new grade: "))
            update_student(name, grade)
        elif choice == 3:
            name = input("Enter Student Name: ")
            delete_student(name)
        elif choice == 4:
            display_all_students()
        elif choice == 5:
            print("Closing the program...")
            break
        else:
            print("Please select from the given choices.")


# Run the main function for interactive input
main()
