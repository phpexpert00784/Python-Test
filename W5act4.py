# Base class
class Person:
    def __init__(self, person_id, name):
        self.person_id = person_id
        self.name = name

    def show_person(self):
        print(f"ID: {self.person_id}, Name: {self.name}")


# Child class of Person
class Student(Person):
    def __init__(self, person_id, name, student_id):
        super().__init__(person_id, name)
        self.student_id = student_id

    def show_student(self):
        self.show_person()
        print(f"Student ID: {self.student_id}")


# Child class of Person
class Staff(Person):
    def __init__(self, person_id, name, staff_id, tax_num):
        super().__init__(person_id, name)
        self.staff_id = staff_id
        self.tax_num = tax_num

    def show_staff(self):
        self.show_person()
        print(f"Staff ID: {self.staff_id}, Tax No: {self.tax_num}")


# Child class of Staff
class General(Staff):
    def __init__(self, person_id, name, staff_id, tax_num, rate_of_pay):
        super().__init__(person_id, name, staff_id, tax_num)
        self.rate_of_pay = rate_of_pay

    def show_general(self):
        self.show_staff()
        print(f"Rate of Pay: {self.rate_of_pay}")


# Child class of Staff
class Academic(Staff):
    def __init__(self, person_id, name, staff_id, tax_num, publications):
        super().__init__(person_id, name, staff_id, tax_num)
        self.publications = publications

    def show_academic(self):
        self.show_staff()
        print(f"Publications: {self.publications}")


# Example usage
student = Student(1, "Rahul", "ST101")
general_staff = General(2, "Anita", "GS201", "TX9988", 35.5)
academic_staff = Academic(3, "Dr. Kumar", "AS301", "TX7766", 12)

student.show_student()
print()

general_staff.show_general()
print()

academic_staff.show_academic()
