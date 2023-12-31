from flask import Flask, redirect, render_template, request
from modules import db_connection
from modules import random_student_id as gen_id

app = Flask(__name__)

connection = db_connection.get_db_connection(app)


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/students", methods=["GET", "POST"])
def show_students():
    students = connection.execute("SELECT * FROM students").fetchall()
    return render_template('students.html', students=students)

@app.route("/internships", methods=["GET", "POST"])
def show_internships():
    internships = connection.execute("SELECT * FROM internships").fetchall()
    return render_template('internships.html', internships=internships)

@app.route("/create_new_student", methods=["GET", "POST"])
def create_new_student():
    return render_template('create_new_student.html')

@app.route("/enroll", methods=["POST"])
def enroll_student():
    student_ID = gen_id.n_len_rand(7)
    last_name = request.form.get("last_name")
    first_name = request.form.get("first_name")
    internship_choice = ''

    connection.execute("INSERT INTO students VALUES(?, ?, ?, ?)", (student_ID, last_name, first_name, internship_choice))
    connection.commit()

    return redirect('/students')

@app.route("/edit", methods=["GET", "POST"])
def edit_student():
    id = request.form.get("id")
    student = connection.execute("SELECT * FROM students WHERE student_ID = ?", (id,)).fetchone()

    return render_template("edit_student.html", student=student) 

@app.route("/update", methods=["GET", "POST"])
def update_student_info():
    student_ID = request.form.get("id")
    internship_choice = request.form.get("internship_choice")

    connection.execute("UPDATE students SET internship_choice = ? WHERE student_id = ?", (internship_choice, student_ID))
    connection.commit()

    return redirect('/students')

@app.route("/delete", methods=["POST"])
def delete_student():
    student_ID = request.form.get("id")

    connection.execute("DELETE FROM students WHERE student_ID = ?", (student_ID,))
    return redirect("/students")

@app.route("/create_new_internship", methods=["POST"])
def create_new_internship():
    location = request.form.get("location")

    connection.execute("INSERT INTO internships (business_name) VALUES(?)", (location,))
    connection.commit()

    return redirect("/internships")

@app.route("/edit_internship", methods=["GET", "POST"])
def edit_internship():
    id = request.form.get("id")
    internship = connection.execute("SELECT * FROM internships WHERE internship_ID = ?", (id,)).fetchone()

    return render_template("edit_internship.html", internship=internship) 

@app.route("/update_internship", methods=["GET", "POST"])
def update_internship_information():
    internship_ID = request.form.get("id")
    location = request.form.get("location")

    connection.execute("UPDATE internships SET business_name = ? WHERE internship_ID = ?", (location, internship_ID))
    connection.commit()

    return redirect("/internships")

@app.route("/delete_internship", methods=["POST"])
def delete_internship():
    internship_ID = request.form.get("id")

    connection.execute("DELETE FROM internships WHERE internship_ID = ?", (internship_ID,))
    return redirect("/internships")
