import tkinter as tk
from tkinter import messagebox
import mysql.connector

# ---------- Database Connection ----------
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="employee"
    )

# ---------- Insert ----------
def insert_data():
    eid = empid_entry.get()
    n = name_entry.get()
    s = salary_entry.get()
    d = dept_entry.get()
    c = city_entry.get()

    if eid == "" or n == "" or s == "" or d == "" or c == "":
        messagebox.showerror("Error", "All fields are required")
        return

    con = get_connection()
    cur = con.cursor()

    sql = "INSERT INTO employee VALUES(%s,%s,%s,%s,%s)"
    cur.execute(sql, (eid, n, s, d, c))

    con.commit()
    con.close()

    messagebox.showinfo("Success", "Employee Record Inserted")

# ---------- Select ----------
def show_data():
    con = get_connection()
    cur = con.cursor()

    cur.execute("SELECT * FROM employee")
    rows = cur.fetchall()

    text_area.delete(1.0, tk.END)

    for r in rows:
        text_area.insert(tk.END, str(r) + "\n")

    con.close()

# ---------- Update ----------
def update_data():
    eid = empid_entry.get()
    n = name_entry.get()
    s = salary_entry.get()
    d = dept_entry.get()
    c = city_entry.get()

    con = get_connection()
    cur = con.cursor()

    sql = "UPDATE employee SET name=%s, salary=%s, dept=%s, city=%s WHERE empid=%s"
    cur.execute(sql, (eid, n, s, d, c,))

    con.commit()
    con.close()

    messagebox.showinfo("Success", "Employee Record Updated")

# ---------- Delete ----------
def delete_data():
    eid = empid_entry.get()

    con = get_connection()
    cur = con.cursor()

    sql = "DELETE FROM employee WHERE empid=%s"
    cur.execute(sql, (eid,))

    con.commit()
    con.close()

    messagebox.showinfo("Success", "Employee Record Deleted")

# ---------- GUI ----------
root = tk.Tk()
root.title("Employee Management System")
root.geometry("500x450")

# Labels
tk.Label(root, text="Employee ID").place(x=50, y=50)
tk.Label(root, text="Name").place(x=50, y=90)
tk.Label(root, text="Salary").place(x=50, y=130)
tk.Label(root, text="Department").place(x=50, y=170)
tk.Label(root, text="City").place(x=50, y=210)

# Entry boxes
empid_entry = tk.Entry(root)
empid_entry.place(x=150, y=50)

name_entry = tk.Entry(root)
name_entry.place(x=150, y=90)

salary_entry = tk.Entry(root)
salary_entry.place(x=150, y=130)

dept_entry = tk.Entry(root)
dept_entry.place(x=150, y=170)

city_entry = tk.Entry(root)
city_entry.place(x=150, y=210)

# Buttons
tk.Button(root, text="Insert", command=insert_data).place(x=50, y=260)
tk.Button(root, text="Show", command=show_data).place(x=120, y=260)
tk.Button(root, text="Update", command=update_data).place(x=190, y=260)
tk.Button(root, text="Delete", command=delete_data).place(x=270, y=260)

# Text area
text_area = tk.Text(root, width=50, height=8)
text_area.place(x=50, y=310)
root.mainloop()