# Student Record System using Python

students = []

def add_student():
    print("\n--- Add Student ---")
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    course = input("Enter Student Course: ")

    student = {"ID": student_id, "Name": name, "Age": age, "Course": course}
    students.append(student)
    print("Student added successfully!\n")

def display_students():
    print("\n--- Display All Students ---")
    if not students:
        print("No records found.\n")
    else:
        for student in students:
            print(f"ID: {student['ID']}, Name: {student['Name']}, Age: {student['Age']}, Course: {student['Course']}")
        print()

def search_student():
    print("\n--- Search Student ---")
    student_id = input("Enter Student ID to search: ")
    for student in students:
        if student["ID"] == student_id:
            print(f"Found: ID: {student['ID']}, Name: {student['Name']}, Age: {student['Age']}, Course: {student['Course']}\n")
            return
    print("Student not found.\n")

def update_student():
    print("\n--- Update Student ---")
    student_id = input("Enter Student ID to update: ")
    for student in students:
        if student["ID"] == student_id:
            print("Enter new details (leave blank to keep current value):")
            name = input(f"Name ({student['Name']}): ") or student['Name']
            age = input(f"Age ({student['Age']}): ") or student['Age']
            course = input(f"Course ({student['Course']}): ") or student['Course']

            student["Name"] = name
            student["Age"] = age
            student["Course"] = course
            print("Student record updated successfully!\n")
            return
    print("Student not found.\n")

def main():
    while True:
        print("===== Student Record System =====")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student by ID")
        print("4. Update Student Record")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
