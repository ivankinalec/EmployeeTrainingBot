import sqlite3


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def does_he_work(self, employee_id):
        with self.connection:
            result = self.cursor.execute("SELECT employee_id FROM employees WHERE employee_id = ?", (employee_id,)).fetchall()
            first_name = str(self.cursor.execute("SELECT first_name from employees WHERE first_name = ?", (employee_id,)).fetchall())
            #print(len(result))
            return bool(len(result))

    def hello(self, first_name):
        with self.connection:
            result = self.cursor.execute("SELECT middle_name, last_name from employees WHERE employee_id = ?", (first_name,)).fetchone()
            return result

