import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import re


def validate_student_id(student_id):
    return re.match(r"^\d{7}$", student_id)


def validate_date_of_birth(date_of_birth):
    try:
        datetime.strptime(date_of_birth, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def validate_email(email):
    return re.match(r"^\S+@\S+\.\S+$", email)


def validate_phone(phone):
    return re.match(r"^\d{10}$", phone)


def validate_class(year):
    return re.match(r"^\d{4}$", year)


def submit():
    student_id = student_id_entry.get()
    name = name_entry.get()
    date_of_birth = date_of_birth_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    semester = semester_entry.get()
    class_of = class_combobox.get()

    if (
        not validate_student_id(student_id)
        or not validate_date_of_birth(date_of_birth)
        or not validate_email(email)
        or not validate_phone(phone)
        or not validate_class(class_of)
    ):
        messagebox.showerror("Lỗi Input. Vui lòng nhập lại")
        return

    subjects = [subject.get() for subject in subject_vars]

    # You can save the student's data or perform other actions here
    # For now, we'll just print the data
    print("Student ID:", student_id)
    print("Name:", name)
    print("Date of Birth:", date_of_birth)
    print("Email:", email)
    print("Phone:", phone)
    print("Semester:", semester)
    print("Class of:", class_of)
    print("Selected Subjects:", subjects)


def exit_program():
    root.destroy()


root = tk.Tk()
root.title("Đăng ký học phần")

title_label = tk.Label(
    root, text="Phiếu Đăng ký học phần", fg="red", font=("Arial", 16)
)
title_label.grid(row=0, column=0, columnspan=3, pady=10)

#Trường
fields = ["Mã số sinh viên", "Họ tên", "Ngày sinh", "Email", "Số điện thoại", "Học kỳ"]
entries = []

for i, field in enumerate(fields):
    label = tk.Label(root, text=field)
    label.grid(row=i + 1, column=0, padx=10, pady=5, sticky="w")
    entry = tk.Entry(root)
    entry.grid(row=i + 1, column=1, padx=10, pady=5, columnspan=2)
    entries.append(entry)

(
    student_id_entry,
    name_entry,
    date_of_birth_entry,
    email_entry,
    phone_entry,
    semester_entry,
) = entries

#Combobox năm học
class_label = tk.Label(root, text="Năm học")
class_label.grid(row=7, column=0, padx=10, pady=5, sticky="w")
class_values = [str(year) for year in range(2020, 2025)]
class_combobox = ttk.Combobox(root, values=class_values)
class_combobox.grid(row=7, column=1, padx=10, pady=5, columnspan=2)

# Checkbox
subject_vars = [tk.IntVar() for _ in range(4)]
pick_subject_label = tk.Label(root, text="Chọn môn học")
pick_subject_label.grid(
    row=8,
    column=0,
    padx=10,
    pady=5,
)
subject_labels = [
    "Lập trình Python",
    "Lập trình Java",
    "Công nghệ phần mềm",
    "Phát triển ứng dụng Web",
]
subject_checkboxes = []

for i in range(4):
    subject_checkboxes.append(
        tk.Checkbutton(root, text=subject_labels[i], variable=subject_vars[i])
    )
    subject_checkboxes[i].grid(
        row=8 + i, column=1, padx=10, pady=5, sticky="w", columnspan=2
    )


# Buttons
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=12, column=1, pady=10)

exit_button = tk.Button(root, text="Exit", command=exit_program)
exit_button.grid(row=12, column=2, pady=10)

root.mainloop()
