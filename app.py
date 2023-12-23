from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/enroll")
def enroll_student():
    return render_template('create_new_student.html')