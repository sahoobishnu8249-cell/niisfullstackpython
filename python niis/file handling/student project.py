import pickle
import os

# Student Class
class Student:
    def __init__(self, roll, name, mark):
        self.roll = roll
        self.name = name
        self.mark = mark

    def input_data(self):
        self.roll = int(input("Enter Roll: "))
        self.name = input("Enter Name: ")
        self.mark = int(input("Enter Mark: "))

    def show(self):
        print(self.roll, self.name, self.mark)

    def get_roll(self):
        return self.roll


# Add Student
def add_student():
    f = open("student.dat","ab")

    s = Student(0,"",0)
    s.input_data()

    pickle.dump(s,f)
    f.close()

    print("Record Added Successfully")


# Display All Students
def display_all():
    try:
        f = open("student.dat","rb")

        print("\nStudent List")
        print("Roll  Name  Mark")

        while True:
            s = pickle.load(f)
            s.show()

    except EOFError:
        f.close()

    except FileNotFoundError:
        print("File not found")


# Search Student
def search_student():
    r = int(input("Enter roll to search: "))

    found = False

    try:
        f = open("student.dat","rb")

        while True:
            s = pickle.load(f)

            if s.get_roll() == r:
                print("Record Found")
                s.show()
                found = True
                break

    except EOFError:
        f.close()

    if not found:
        print("Record not found")


# Update Student
def update_student():
    r = int(input("Enter roll to update: "))

    found = False

    f = open("student.dat","rb")
    temp = open("temp.dat","wb")

    try:
        while True:
            s = pickle.load(f)

            if s.get_roll() == r:
                print("Enter new data")
                s.input_data()
                found = True

            pickle.dump(s,temp)

    except EOFError:
        f.close()
        temp.close()

    os.remove("student.dat")
    os.rename("temp.dat","student.dat")

    if found:
        print("Record Updated")
    else:
        print("Record not found")


# Delete Student
def delete_student():
    r = int(input("Enter roll to delete: "))

    found = False

    f = open("student.dat","rb")
    temp = open("temp.dat","wb")

    try:
        while True:
            s = pickle.load(f)

            if s.get_roll() != r:
                pickle.dump(s,temp)
            else:
                found = True

    except EOFError:
        f.close()
        temp.close()

    os.remove("student.dat")
    os.rename("temp.dat","student.dat")

    if found:
        print("Record Deleted")
    else:
        print("Record not found")


# Menu
while True:

    print("\n----- Student Management System -----")
    print("1. Add Student")
    print("2. Display All")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        add_student()

    elif ch == 2:
        display_all()

    elif ch == 3:
        search_student()

    elif ch == 4:
        update_student()

    elif ch == 5:
        delete_student()

    elif ch == 6:
        print("Program End")
        break

    else:
        print("Invalid Choice")