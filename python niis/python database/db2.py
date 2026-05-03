import sqlite3
conn=sqlite3.connect("student.db")
cur=conn.cursor()
cur.execute("SELECT * FROM student")
rows=cur.fetchall()
for r in rows:
	print(r)
conn.close()