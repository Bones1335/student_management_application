CREATE TABLE internships (internship_ID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, business_name TEXT NOT NULL);
CREATE TABLE students (student_ID INTEGER PRIMARY KEY UNIQUE NOT NULL, last_name TEXT NOT NULL, first_name TEXT NOT NULL, internship_choice NUMERIC REFERENCES internship (internship_ID));
