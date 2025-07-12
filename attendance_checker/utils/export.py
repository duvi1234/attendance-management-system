import pandas as pd
import io
from flask import send_file
from models.models import Attendance, Student
from sqlalchemy import func

def calculate_attendance_for_students(students):
    """Calculate attendance % for each student."""
    data = []
    for student in students:
        records = Attendance.query.filter_by(student_id=student.id).all()
        total = sum(r.total_classes for r in records)
        attended = sum(r.attended_classes for r in records)
        percentage = round((attended / total) * 100, 2) if total > 0 else 0

        data.append({
            'Name': student.name,
            'Roll No': student.roll_no,
            'Total Classes': total,
            'Attended Classes': attended,
            'Percentage': percentage
        })
    return data

def export_all_students(students):
    """Export all students' attendance data to Excel."""
    data = calculate_attendance_for_students(students)
    df = pd.DataFrame(data)
    
    output = io.BytesIO()
    df.to_excel(output, index=False)
    output.seek(0)
    return send_file(output, download_name='all_students.xlsx', as_attachment=True)

def export_ineligible_students(students, min_percentage=75):
    """Export students with less than 75% attendance to Excel."""
    all_data = calculate_attendance_for_students(students)
    ineligible_data = [s for s in all_data if s['Percentage'] < min_percentage]
    
    df = pd.DataFrame(ineligible_data)
    output = io.BytesIO()
    df.to_excel(output, index=False)
    output.seek(0)
    return send_file(output, download_name='ineligible_students.xlsx', as_attachment=True)
