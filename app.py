import sqlite3
from flask import Flask, redirect, render_template, request
from modules import random_student_id as gen_id

app = Flask(__name__)


def get_db_connection():
    connection = sqlite3.connect("students.db", check_same_thread=False)
    connection.row_factory = sqlite3.Row
    return connection

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/students", methods=["GET", "POST"])
def show_students():
    connection = get_db_connection()
    students = connection.execute("SELECT * FROM students").fetchall()
    return render_template('students.html', students=students)

@app.route("/internships", methods=["GET", "POST"])
def show_internships():
    connection = get_db_connection()
    internships = connection.execute("SELECT * FROM internships").fetchall()
    return render_template('internships.html', internships=internships)

@app.route("/create_new_student", methods=["GET", "POST"])
def create_new_student():
    return render_template('create_new_student.html')

@app.route("/enroll", methods=["POST"])
def enroll_student():
    connection = get_db_connection()

    student_ID = gen_id.n_len_rand(7)
    last_name = request.form.get("last_name")
    first_name = request.form.get("first_name")
    internship_choice = ''

    connection.execute("INSERT INTO students VALUES(?, ?, ?, ?)", (student_ID, last_name, first_name, internship_choice))
    connection.commit()

    return redirect('/students')
    