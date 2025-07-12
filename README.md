# Attendance Checker System

A modern, responsive Flask-based web application for advisor-driven student attendance management. Features semester and subject management, subject-wise and overall attendance tracking, weekly updates, and Excel export. Built for CSE(AI&ML) 2023-2027, ready for deployment on Render.

## Features

- **Modern UI/UX**: Responsive, attractive dashboard and login pages
- **Advisor Login**: Secure access for advisors to manage their batch
- **Semester & Subject Management**: Add/manage semesters and subjects
- **Subject-wise Attendance**: Track and update attendance per subject, per week
- **Weekly Updates**: Calendar-based week picker for attendance input
- **Export Functionality**: Download Excel reports with subject breakdown
- **Visual Indicators**: Highlights students below 75% attendance
- **Show Password**: Toggle password visibility on login page
- **Ready for Render Deployment**: Easy to deploy on Render.com

## Deployment on Render

1. **Push your code to GitHub**
2. **Create a new Web Service** on [Render.com](https://render.com/)
3. **Connect your GitHub repo** and select it
4. **Set the Start Command**:
   - If using a factory function: `gunicorn app:create_app()`
   - If using a simple app: `gunicorn app:app`
5. **Add environment variables** as needed (e.g., `FLASK_ENV=production`)
6. **(Optional) Add a Persistent Disk** for SQLite database persistence
7. **Deploy!**

See the rest of this README for usage, features, and troubleshooting.

## How to Use the System

### For Advisors

1. **Login**: Use advisor credentials (e.g., username: `advisor1`, password: `password123`)

2. **Manage Subjects**: 
   - Go to "Manage Subjects" to add or remove subjects
   - Each batch can have multiple subjects

3. **Update Weekly Attendance**:
   - Go to "Update Attendance"
   - Select the week number and subject
   - Enter total classes and attended classes for each student
   - Submit to save the attendance data

4. **View Dashboard**:
   - See subject-wise attendance breakdown for all students
   - View overall attendance percentage
   - Identify students with attendance below 75%

5. **Export Data**:
   - Export all students with subject-wise breakdown
   - Export only students with attendance below 75%

## Sample Data

The system comes with sample data including:

### Advisors
- **Advisor 1**: username=`advisor1`, password=`password123` (Computer Science 2024 batch)
- **Advisor 2**: username=`advisor2`, password=`password123` (Information Technology 2024 batch)
- **Advisor 3**: username=`advisor3`, password=`password123` (Information Technology 2024 batch)

### Subjects
**Computer Science 2024:**
- Programming Fundamentals
- Data Structures
- Database Management
- Web Development
- Computer Networks

**Information Technology 2024:**
- Programming Basics
- Database Systems
- Web Technologies
- Network Security
- Software Engineering

### Students
- **Computer Science**: 5 students (CS001-CS005)
- **Information Technology**: 5 students (IT001-IT005)

## Installation and Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Initialize Database**:
   ```bash
   python init_db.py
   ```

3. **Setup Sample Data** (Optional):
   ```bash
   python setup_subject_data.py
   ```

4. **Run the Application**:
   ```bash
   python app.py
   ```

5. **Access the Application**:
   - Open browser and go to `http://localhost:5000`
   - Use the sample credentials provided above

## Database Schema

### Advisor Table
- `id`: Primary key
- `username`: Unique login username
- `password`: Hashed password
- `batch_id`: Foreign key to Batch table

### Student Table
- `id`: Primary key
- `name`: Student's full name
- `roll_no`: Unique roll number
- `batch_id`: Foreign key to Batch table

### Subject Table
- `id`: Primary key
- `name`: Subject name
- `batch_id`: Foreign key to Batch table

### Batch Table
- `id`: Primary key
- `name`: Batch name (e.g., "Computer Science 2024")

### Attendance Table
- `id`: Primary key
- `student_id`: Foreign key to Student table
- `subject_id`: Foreign key to Subject table
- `week_number`: Week number for the attendance record
- `total_classes`: Total classes held in the week
- `attended_classes`: Classes attended by the student

## Workflow

### Weekly Attendance Update Process

1. **Login as Advisor**: Access the system with advisor credentials

2. **Select Subject**: Choose which subject to update attendance for

3. **Enter Week Number**: Specify which week the attendance is for

4. **Input Data**: For each student, enter:
   - Total classes held that week
   - Number of classes the student attended

5. **Submit**: Save the attendance data for that subject and week

6. **Repeat**: Update attendance for other subjects as needed

### Dashboard View

The dashboard shows:
- **Subject-wise breakdown**: Each subject's attendance percentage
- **Overall attendance**: Combined attendance across all subjects
- **Visual indicators**: Red highlighting for students below 75%
- **Detailed stats**: Total classes and attended classes

### Export Features

- **Export All**: Complete attendance report with subject breakdown
- **Export Ineligible**: Only students with overall attendance below 75%

## Security Features

- **Password Hashing**: All passwords are hashed using Werkzeug's security functions
- **Session Management**: Secure session handling for logged-in advisors
- **Access Control**: Advisors can only manage their assigned batch

## File Structure

```
attendance_checker/
├── app.py                 # Main Flask application
├── models/
│   └── models.py         # Database models
├── auth/
│   └── routes.py         # Authentication routes
├── attendance/
│   └── routes.py         # Attendance management routes
├── templates/            # HTML templates
├── static/              # CSS and JavaScript files
├── init_db.py           # Database initialization
├── setup_subject_data.py # Sample data setup
└── requirements.txt     # Python dependencies
```

## Troubleshooting

### Common Issues

1. **Database Errors**: Run `python init_db.py` to recreate the database
2. **Login Issues**: Ensure you're using the correct advisor credentials
3. **Missing Subjects**: Use the "Manage Subjects" page to add subjects

### Reset Database

To start fresh with sample data:
```bash
python setup_subject_data.py
```

This will clear all existing data and create new sample data with subjects and students.

## Key Features Summary

✅ **Advisor-only access** - No student login required  
✅ **Subject management** - Add/remove subjects per batch  
✅ **Weekly updates** - Update attendance by subject and week  
✅ **Subject-wise tracking** - Separate attendance for each subject  
✅ **Overall calculation** - Combined attendance across all subjects  
✅ **Export functionality** - Excel reports with subject breakdown  
✅ **Visual indicators** - Highlight students below 75% attendance  
✅ **Batch management** - Separate batches for different groups 
