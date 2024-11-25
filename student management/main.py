
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
        print("1) Add Student ")
        print("2) Update Student Grade")
        print("3) Delete Student")
        print("4) View Students")
        print("5) Exit")
        choice = int(input("Enter your choice: "))
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
main()