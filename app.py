import sqlite3
from flask import Flask, render_template

app = Flask(__name__)


def get_db_connection():
    connection = sqlite3.connect("students.db", check_same_thread=False)
    connection.row_factory = sqlite3.Row
    return connection

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/enroll")
def enroll_student():
    return render_template('create_new_student.html')

@app.route("/students")
def show_students():
    connection = get_db_connection()
    students = connection.execute("SELECT * FROM students").fetchall()
    return render_template('students.html', students=students)

@app.route("/internships")
def show_internships():
    connection = get_db_connection()
    internships = connection.execute("SELECT * FROM internships").fetchall()
    return render_template('internships.html', internships=internships)