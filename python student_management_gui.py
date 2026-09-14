import tkinter as tk
from tkinter import messagebox


# ---------- Core Logic (same ideas as the console version) ----------

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks


students = []


def save_to_file():
    with open("students.txt", "w") as f:
        for s in students:
            f.write(f"{s.name},{s.roll_no},{s.marks}\n")


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
    except FileNotFoundError:
        pass  # no file yet, that's fine


# ---------- GUI Functions (triggered by button clicks) ----------

def refresh_listbox():
    """Clears and redraws the listbox to match the current `students` list."""
    listbox.delete(0, tk.END)
    for s in students:
        listbox.insert(tk.END, f"{s.roll_no} | {s.name} | {s.marks}")


def add_student_gui():
    name = name_entry.get()
    roll_no = roll_entry.get()
    marks = marks_entry.get()

    if not name or not roll_no or not marks:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    try:
        roll_no = int(roll_no)
        marks = int(marks)
    except ValueError:
        messagebox.showerror("Error", "Roll number and marks must be numbers.")
        return

    students.append(Student(name, roll_no, marks))
    save_to_file()
    refresh_listbox()
    clear_entries()


def delete_student_gui():
    selected = listbox.curselection()  # returns a tuple of selected indices
    if not selected:
        messagebox.showerror("Error", "Select a student from the list first.")
        return

    index = selected[0]
    del students[index]
    save_to_file()
    refresh_listbox()


def search_student_gui():
    roll_no = roll_entry.get()
    if not roll_no:
        messagebox.showerror("Error", "Enter a roll number to search.")
        return

    try:
        roll_no = int(roll_no)
    except ValueError:
        messagebox.showerror("Error", "Roll number must be a number.")
        return

    for s in students:
        if s.roll_no == roll_no:
            messagebox.showinfo("Found", f"Name: {s.name}\nRoll No: {s.roll_no}\nMarks: {s.marks}")
            return
    messagebox.showinfo("Not Found", "No student with that roll number.")


def clear_entries():
    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)
    marks_entry.delete(0, tk.END)


# ---------- Build the Window ----------

window = tk.Tk()
window.title("Student Management System")
window.geometry("420x450")

# Input fields
tk.Label(window, text="Name").grid(row=0, column=0, padx=10, pady=5, sticky="w")
name_entry = tk.Entry(window, width=25)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(window, text="Roll No").grid(row=1, column=0, padx=10, pady=5, sticky="w")
roll_entry = tk.Entry(window, width=25)
roll_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(window, text="Marks").grid(row=2, column=0, padx=10, pady=5, sticky="w")
marks_entry = tk.Entry(window, width=25)
marks_entry.grid(row=2, column=1, padx=10, pady=5)

# Buttons
tk.Button(window, text="Add Student", width=15, command=add_student_gui).grid(row=3, column=0, padx=10, pady=10)
tk.Button(window, text="Search by Roll No", width=15, command=search_student_gui).grid(row=3, column=1, padx=10, pady=10)
tk.Button(window, text="Delete Selected", width=15, command=delete_student_gui).grid(row=4, column=0, padx=10, pady=5)
tk.Button(window, text="Clear Fields", width=15, command=clear_entries).grid(row=4, column=1, padx=10, pady=5)

# Listbox to show all students
tk.Label(window, text="All Students (click one to select for delete)").grid(row=5, column=0, columnspan=2, pady=(15, 0))
listbox = tk.Listbox(window, width=50, height=12)
listbox.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Load existing data and show it when the app opens
load_from_file()
refresh_listbox()

window.mainloop()
