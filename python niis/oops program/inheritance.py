class person:
    def display_person(self):
        print("this is a person")

class student:
    def display_student(self):
        print("this is a student")

class Engineering(person, student):
    def display_engineering(self):
        print("this is a engineering student")

e = Engineering()
e.display_person()
e.display_student()
e.display_engineering()


