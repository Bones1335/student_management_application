# Student Management Application

## MVP Functionality

### Students

- CREATE new students using the 'New Student' tab. Only First and Last names are inputable for the moment. The 7-digit student ID is generated automatically once the new student is created. The internship choice will be blank upon initial creation.
- READ full list of students from the students.db SQLite database.
- UPDATE using the 'Edit' button next to each individual student to update a student's internship choice with the internship ID. Student names cannot currently be changed.
- DELETE all records of an existing student.

### Internships

- CREATE new internship location with the business name. A unique code is automatically generated for each created business. Currently doesn't have any other business information.
- READ full list of internships with their unique codes displayed from the internships table of the students.db SQLite database.
- UPDATE a business' name with the 'Edit' button.
- DELETE all records of an existing business. Note that doing so will create numerical holes in the list of internship locations due to each unique code and the autoincrement feature of the database.

## Set-up

- Clone the repository with `git clone` and run the following code in your terminal to test the application in a virtual environment for Python:

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask run
```

- Once in the app, you should be able to add, view, update, and remove students and internships.
