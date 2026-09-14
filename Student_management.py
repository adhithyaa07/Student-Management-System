class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print(f"Roll No: {self.roll_no} | Name: {self.name} | Marks: {self.marks}")


students = []


def add_student(name, roll_no, marks):
    new_student = Student(name, roll_no, marks)
    students.append(new_student)
    print("Student added successfully!")


def display_all():
    if not students:
        print("No students found.")
        return
    for s in students:
        s.display()


def search_student(roll_no):
    for s in students:
        if s.roll_no == roll_no:
            s.display()
            return
    print("Student not found.")


def delete_student(roll_no):
    for s in students:
        if s.roll_no == roll_no:
            students.remove(s)
            print("Student deleted.")
            return
    print("Student not found.")


def save_to_file():
    with open("students.txt", "w") as f:
        for s in students:
            f.write(f"{s.name},{s.roll_no},{s.marks}\n")
    print("Data saved successfully!")


def load_from_file():
    students.clear()
    try:
        with open("students.txt", "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                name, roll_no, marks = line.split(",")
                students.append(Student(name, int(roll_no), int(marks)))
        print("Data loaded successfully!")
    except FileNotFoundError:
        print("No saved data found. Starting fresh.")


def main():
    load_from_file()
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            roll_no = int(input("Enter roll number: "))
            marks = int(input("Enter marks: "))
            add_student(name, roll_no, marks)

        elif choice == "2":
            display_all()

        elif choice == "3":
            roll_no = int(input("Enter roll number to search: "))
            search_student(roll_no)

        elif choice == "4":
            roll_no = int(input("Enter roll number to delete: "))
            delete_student(roll_no)

        elif choice == "5":
            save_to_file()
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
