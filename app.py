from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('create_new_student.html')