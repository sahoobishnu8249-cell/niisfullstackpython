import mysql.connector

# Step 1: Connect to MySQL database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="niss"
)

print("Connected successfully")

# Step 2: Create cursor object
cur = con.cursor()

# Step 3: Execute SELECT query
cur.execute("SELECT * FROM student")

# Step 4: Fetch all rows
rows = cur.fetchall()

# Step 5: Display records
print("\nStudent Records:\n")

for r in rows:
    print("Roll No:", r[0])
    print("Name   :", r[1])
    print("Marks  :", r[2])
    print("-------------------")

# Step 6: Close connection
con.close()