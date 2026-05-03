import tkinter as tk
from tkinter import messagebox
import mysql.connector

# ---------- Database Connection ----------
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="niss"
    )

# ---------- Insert ----------
def insert_data():
    r = rollno_entry.get()
    n = name_entry.get()
    m = marks_entry.get()

    con = get_connection()
    cur = con.cursor()

    sql = "INSERT INTO student VALUES(%s,%s,%s)"
    cur.execute(sql,(r,n,m))

    con.commit()
    con.close()

    messagebox.showinfo("Success","Record Inserted")

# ---------- Select ----------
def show_data():
    con = get_connection()
    cur = con.cursor()

    cur.execute("SELECT * FROM student")

    rows = cur.fetchall()

    text_area.delete(1.0, tk.END)

    for r in rows:
        text_area.insert(tk.END,str(r)+"\n")

    con.close()

# ---------- Update ----------
def update_data():
    r = rollno_entry.get()
    n = name_entry.get()
    m = marks_entry.get()

    con = get_connection()
    cur = con.cursor()

    sql = "UPDATE student SET name=%s, marks=%s WHERE rollno=%s"
    cur.execute(sql,(n,m,r))

    con.commit()
    con.close()

    messagebox.showinfo("Success","Record Updated")

# ---------- Delete ----------
def delete_data():
    r = rollno_entry.get()

    con = get_connection()
    cur = con.cursor()

    sql = "DELETE FROM student WHERE rollno=%s"
    cur.execute(sql,(r,))

    con.commit()
    con.close()

    messagebox.showinfo("Success","Record Deleted")

# ---------- GUI ----------
root = tk.Tk()
root.title("Student Management System")
root.geometry("500x400")

# Labels
tk.Label(root,text="Roll No").place(x=50,y=50)
tk.Label(root,text="Name").place(x=50,y=90)
tk.Label(root,text="Marks").place(x=50,y=130)

# Entry boxes
rollno_entry = tk.Entry(root)
rollno_entry.place(x=150,y=50)

name_entry = tk.Entry(root)
name_entry.place(x=150,y=90)

marks_entry = tk.Entry(root)
marks_entry.place(x=150,y=130)

# Buttons
tk.Button(root,text="Insert",command=insert_data).place(x=50,y=180)

tk.Button(root,text="Show",command=show_data).place(x=120,y=180)

tk.Button(root,text="Update",command=update_data).place(x=190,y=180)

tk.Button(root,text="Delete",command=delete_data).place(x=270,y=180)

# Text area
text_area = tk.Text(root,width=50,height=10)
text_area.place(x=50,y=230)

root.mainloop()