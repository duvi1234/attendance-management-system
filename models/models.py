from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Advisor table: login credentials + linked batch
class Advisor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)  # hashed password
    batch_id = db.Column(db.Integer, db.ForeignKey('batch.id'), nullable=False)

# Batch table: groups of students
class Batch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    # relationships
    students = db.relationship('Student', backref='batch', lazy=True)
    advisors = db.relationship('Advisor', backref='batch', lazy=True)
    semesters = db.relationship('Semester', backref='batch', lazy=True)

# Semester table: to manage different semesters
class Semester(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # e.g., "Semester 1", "Semester 2"
    batch_id = db.Column(db.Integer, db.ForeignKey('batch.id'), nullable=False)
    is_active = db.Column(db.Boolean, default=True)  # to mark current semester
    
    # relationships
    subjects = db.relationship('Subject', backref='semester', lazy=True)

# Subject table
class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    semester_id = db.Column(db.Integer, db.ForeignKey('semester.id'), nullable=False)
    
    # relationships
    attendances = db.relationship('Attendance', backref='subject', lazy=True)

# Student table
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    roll_no = db.Column(db.String(20), unique=True, nullable=False)
    reg_no = db.Column(db.String(20), unique=True, nullable=False)  # Registration number
    batch_id = db.Column(db.Integer, db.ForeignKey('batch.id'), nullable=False)

    # relationships
    attendances = db.relationship('Attendance', backref='student', lazy=True)

# Weekly attendance table with subject-wise tracking
class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    week_number = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=True)  # New field for actual date
    total_classes = db.Column(db.Integer, nullable=False)
    attended_classes = db.Column(db.Integer, nullable=False)
