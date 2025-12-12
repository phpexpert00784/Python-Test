import sqlite3

class SchoolDB:
    """OOP class to manage database creation, insertion, and queries."""

    def __init__(self, db_name="school.db"):
        # Connect to SQLite DB (creates file if not exists)
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """Create all tables needed for the school database."""
        self.cursor.executescript("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT UNIQUE NOT NULL,
            title TEXT
        );

        CREATE TABLE IF NOT EXISTS enrollments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            course_id INTEGER,
            FOREIGN KEY(student_id) REFERENCES students(id),
            FOREIGN KEY(course_id) REFERENCES courses(id)
        );

        CREATE TABLE IF NOT EXISTS teaching_assignments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            teacher_id INTEGER,
            course_id INTEGER,
            FOREIGN KEY(teacher_id) REFERENCES teachers(id),
            FOREIGN KEY(course_id) REFERENCES courses(id)
        );
        """)
        self.conn.commit()

    def add_student(self, name):
        """Insert a student into the database."""
        self.cursor.execute("INSERT INTO students(name) VALUES (?)", (name,))
        self.conn.commit()
        return self.cursor.lastrowid

    def add_teacher(self, name):
        """Insert a teacher."""
        self.cursor.execute("INSERT INTO teachers(name) VALUES (?)", (name,))
        self.conn.commit()
        return self.cursor.lastrowid

    def add_course(self, code, title):
        """Insert a course."""
        self.cursor.execute(
            "INSERT OR IGNORE INTO courses(code, title) VALUES (?, ?)",
            (code, title)
        )
        self.conn.commit()
        # Fetch ID
        self.cursor.execute("SELECT id FROM courses WHERE code=?", (code,))
        return self.cursor.fetchone()[0]

    def enroll(self, student_id, course_id):
        """Enroll a student in a course."""
        self.cursor.execute(
            "INSERT INTO enrollments(student_id, course_id) VALUES (?, ?)",
            (student_id, course_id)
        )
        self.conn.commit()

    def assign_teacher(self, teacher_id, course_id):
        """Assign a teacher to teach a course."""
        self.cursor.execute(
            "INSERT INTO teaching_assignments(teacher_id, course_id) VALUES (?, ?)",
            (teacher_id, course_id)
        )
        self.conn.commit()

    def count_students_in_course(self, course_code):
        """Return number of students enrolled in a course (MSE800)."""
        self.cursor.execute("""
            SELECT COUNT(DISTINCT students.id)
            FROM students
            JOIN enrollments ON enrollments.student_id = students.id
            JOIN courses ON courses.id = enrollments.course_id
            WHERE courses.code = ?
        """, (course_code,))
        return self.cursor.fetchone()[0]

    def teachers_for_course(self, course_code):
        """Return teacher names for a course (MSE801)."""
        self.cursor.execute("""
            SELECT DISTINCT teachers.name
            FROM teachers
            JOIN teaching_assignments 
                  ON teaching_assignments.teacher_id = teachers.id
            JOIN courses 
                  ON courses.id = teaching_assignments.course_id
            WHERE courses.code = ?
        """, (course_code,))
        return [name[0] for name in self.cursor.fetchall()]

    def close(self):
        self.conn.close()


# -----------------------------
# Main program demonstrating use
# -----------------------------

if __name__ == "__main__":
    db = SchoolDB()

    # Insert sample courses
    mse800 = db.add_course("MSE800", "Advanced Materials I")
    mse801 = db.add_course("MSE801", "Advanced Materials II")

    # Insert teachers
    t1 = db.add_teacher("Dr. John")
    t2 = db.add_teacher("Prof. Alex")

    # Assign teachers to MSE801
    db.assign_teacher(t1, mse801)
    db.assign_teacher(t2, mse801)

    # Students
    s1 = db.add_student("Happy Singh")
    s2 = db.add_student("Shampy Singh")
    s3 = db.add_student("Chotu Patel")

    # Enroll students to MSE800
    db.enroll(s1, mse800)
    db.enroll(s2, mse800)
    db.enroll(s3, mse800)

    # Run required queries
    print("Students enrolled in MSE800:", db.count_students_in_course("MSE800"))
    print("Teachers teaching MSE801:", db.teachers_for_course("MSE801"))

    db.close()
