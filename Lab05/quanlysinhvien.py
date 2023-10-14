from ast import Str
# from debugpy import connect
import pyodbc

#2
connectionString = ''' DRIVER={SQL Server};
SERVER=.;DATABASE=QLSinhVien;Trusted_Connection=yes;'''


def get_connection():
    conn = pyodbc.connect(connectionString)
    return conn


def close_connection(conn):
    if conn:
        conn.close()


def get_all_class():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = "SELECT * FROM Lop"
        cursor.execute(select_query)
        records = cursor.fetchall()
        print(f"Danh sách lớp là: ")
        for row in records:
            print("*"*50)
            print("Mã lớp: ", row[0])
            print("Tên lớp: ", row[1])
        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã xảy ra lỗi! Lỗi >> ", error)


def get_all_sinh_vien():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM SinhVien")
        records = cursor.fetchall()
        print("Danh sách tất cả sinh viên là: ")
        print(f"Mã số\t\tHọ tên\t\t\t\t\tMã lớp")
        for row in records:
            print(f"{row[0]}\t\t{row[1]}\t\t\t\t\t {row[2]}")
    except (Exception, pyodbc.Error) as error:
        print("Đã xảy ra lỗi! Lỗi >> ", error)


def get_sv_by_class():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT sv.ID, sv.HoTen, l.TenLop FROM SinhVien sv, Lop l WHERE l.ID = sv.MaLop")
        records = cursor.fetchall()
        print("Danh sách tất cả sinh viên là: ")
        for row in records:
            print(f"{row[0]}\t{row[1]}\t{row[2]}")
    except (Exception, pyodbc.Error) as error:
        print("lỗi >> ", error)

# 3
def get_class_by_id(class_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Lop WHERE ID = ?", (class_id))
        records = cursor.fetchone()
        print(f"Thông tin lớp có id = {class_id} là: ")
        print("Mã lớp: ", records[0])
        print("Tên lớp: ", records[1])
        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("lỗi >> ", error)

# Viết hàm hiển thị thông tin sinh viên theo mã sinh viên
def get_sv_by_id(sv_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM SinhVien WHERE ID = ?", (sv_id))
        records = cursor.fetchone()
        print(f"Thông tin sinh viên có id = {sv_id} là: ")
        print("Mã sinh viên: ", records[0])
        print("Tên sinh viên: ", records[1])
        print("Mã lớp: ", records[2])
        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("lỗi >> ", error)

# Hiển thị danh sách sinh viên theo lớp (khi biết mã lớp/tên lớp)
def get_sv_by_class(lop):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT sv.ID, sv.HoTen, l.TenLop FROM SinhVien sv, Lop l WHERE l.ID = sv.MaLop AND l.ID = ?", (lop))
        records = cursor.fetchall()
        print(f"Lớp có mã = {lop} là: ")
        for row in records:
            print(f"{row[0]}\t{row[1]}\t\t{row[2]}")
        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("lỗi >> ", error)


# Tìm kiếm thông tin sinh viên theo tên và lớp, ví dụ như hình sau
def find_students(maLop: int, ten: Str):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT sv.ID, sv.HoTen, l.TenLop FROM SinhVien sv, Lop l WHERE l.ID = sv.MaLop AND l.ID = ? AND sv.HoTen LIKE ?", (maLop, f'%{ten}'))
        records = cursor.fetchall()
        print(f"Lớp có mã lớp = {maLop} và Tên = {ten} là: ")
        for row in records:
            print(f"{row[0]}\t{row[1]}\t\t{row[2]}")
        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("lỗi >> ", error)


# get_all_class()
# get_all_sinh_vien()
# get_sv_by_class()
# get_class_by_id(1)
# get_sv_by_id(2)
# get_sv_by_class(3)
find_students(3, 'Trung')