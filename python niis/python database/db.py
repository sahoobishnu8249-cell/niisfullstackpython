import sqlite3
conn=sqlite3.connect("student.db")
cur=conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS student(
	id INTEGER PRIMARY KEY,
	name TEXT,
	marks INTEGER
)
""")
cur.execute("INSERT INTO student VALUES(1,'Bishnu',85)")
conn.commit()
conn.close()
print("Data inserted successfully")