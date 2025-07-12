from app import create_app
from models.models import db, Advisor, Batch, Student, Subject, Semester
from werkzeug.security import generate_password_hash

app = create_app()

# ============================================================================
# EDIT THESE SECTIONS TO CUSTOMIZE YOUR SYSTEM
# ============================================================================

# ADVISOR LOGIN CREDENTIALS
# Edit these to change advisor usernames and passwords
ADVISORS = [
    {
        "username": "dyana",
        "password": "dyanajames",
        "batch_name": "CSE(AI&ML) 2023-2027"
    },
    {
        "username": "ayisha",
        "password": "ayisha",
        "batch_name": "CSE(AI&ML) 2023-2027"
    },
    {
        "username": "yogadinesh",
        "password": "yogadinesh",
        "batch_name": "CSE(AI&ML) 2023-2027"
    }
]

# SEMESTERS FOR THE BATCH
# Edit these to change semesters for your batch
SEMESTERS = {
    "CSE(AI&ML) 2023-2027": [
        "Semester 5"
    ]
}

# SUBJECTS FOR EACH SEMESTER
# Edit these to change subjects for each semester
# Format: "Subject Code - Subject Name"
SUBJECTS = {
    "Semester 5": [
        "R21UAM501 - Introduction to Neural Networks and Deep Learning Techniques",
        "R21UAM502 - Introduction to Cryptography and Cyber Security",
        "R21UCS503 - Theory of Computation",
        "R21UAM504 - Building Internet of Things",
        "R21CSV505 - Digital Marketing",
        "R21UGM535 - Universal Human Values",
        "- - Open Elective",
        "R21UGS531 - Reasoning and Aptitude",
        "R21UAM507 - Creative Thinking and Innovation",
        "R21UAM508 - Building Internet of Things Laboratory",
        "R21UAM509 - Neural Networks and Deep Learning Laboratory",
        "R21UGS532 - Soft Skills Laboratory",
        "R21UAM862 - AI for Game Programming"
    ]
}

# STUDENTS FOR THE BATCH
# Edit these lists to change students for your batch
STUDENTS = {
    "CSE(AI&ML) 2023-2027": [
        {"name": "AKASH M", "roll_no": "23AM039", "reg_no": "921723116001"},
        {"name": "AKHILESH S", "roll_no": "23AM012", "reg_no": "921723116002"},
        {"name": "AMRESH S", "roll_no": "23AM053", "reg_no": "921723116003"},
        {"name": "ARAVIND KUMAR R", "roll_no": "23AM049", "reg_no": "921723116004"},
        {"name": "ARIHARAN H", "roll_no": "23AM056", "reg_no": "921723116005"},
        {"name": "BHAVITHRA C", "roll_no": "23AM040", "reg_no": "921723116006"},
        {"name": "BLESSY JADZIA M", "roll_no": "23AM038", "reg_no": "921723116007"},
        {"name": "BOOMITHA B", "roll_no": "23AM061", "reg_no": "921723116008"},
        {"name": "DANIEL PREM KUMAR P", "roll_no": "23AM067", "reg_no": "921723116009"},
        {"name": "DINESH KUMAR S", "roll_no": "23AM015", "reg_no": "921723116010"},
        {"name": "DIVYAPRABHA B S", "roll_no": "23AM035", "reg_no": "921723116011"},
        {"name": "DURGA DEVI R", "roll_no": "23AM059", "reg_no": "921723116012"},
        {"name": "GIRINATH S M", "roll_no": "23AM069", "reg_no": "921723116013"},
        {"name": "GOBULAKSHMI V", "roll_no": "23AM072", "reg_no": "921723116014"},
        {"name": "GUHAN S", "roll_no": "23AM016", "reg_no": "921723116015"},
        {"name": "GURUDANVARSH B P", "roll_no": "23AM019", "reg_no": "921723116016"},
        {"name": "JENITA REBEKKA C", "roll_no": "23AM001", "reg_no": "921723116017"},
        {"name": "JERIN R", "roll_no": "23AM006", "reg_no": "921723116018"},
        {"name": "KARANYA C S", "roll_no": "23AM062", "reg_no": "921723116019"},
        {"name": "KISHORE KANNA S", "roll_no": "23AM051", "reg_no": "921723116020"},
        {"name": "LISY MC NESEY V", "roll_no": "23AM068", "reg_no": "921723116021"},
        {"name": "MADHAN KUMAR B", "roll_no": "23AM004", "reg_no": "921723116022"},
        {"name": "MADHUMITHA M", "roll_no": "23AM037", "reg_no": "921723116023"},
        {"name": "MARNADU M", "roll_no": "23AM044", "reg_no": "921723116024"},
        {"name": "MOHAMED RAAZIM I", "roll_no": "23AM022", "reg_no": "921723116025"},
        {"name": "MOHAMED RAZEEN S", "roll_no": "23AM023", "reg_no": "921723116026"},
        {"name": "MOHAMMED ABDULLAH H", "roll_no": "23AM041", "reg_no": "921723116027"},
        {"name": "MONISHA T", "roll_no": "23AM032", "reg_no": "921723116028"},
        {"name": "MUTHU MANIKANDAN S", "roll_no": "23AM054", "reg_no": "921723116029"},
        {"name": "NIMAS FATHIMA RAHMAN V", "roll_no": "23AM011", "reg_no": "921723116030"},
        {"name": "NITHISH KUMAR M", "roll_no": "23AM028", "reg_no": "921723116031"},
        {"name": "NITHISHBALA P M", "roll_no": "23AM057", "reg_no": "921723116032"},
        {"name": "NITHYASUNDARI S", "roll_no": "23AM045", "reg_no": "921723116033"},
        {"name": "NIVASH S", "roll_no": "23AM013", "reg_no": "921723116034"},
        {"name": "PRAKASH RAJ K", "roll_no": "23AM065", "reg_no": "921723116035"},
        {"name": "PRAKASH T", "roll_no": "23AM043", "reg_no": "921723116036"},
        {"name": "PRAVEEN RAJ S", "roll_no": "23AM034", "reg_no": "921723116037"},
        {"name": "PRAVEENA R", "roll_no": "23AM042", "reg_no": "921723116038"},
        {"name": "PRIYADHARSHINI S", "roll_no": "23AM066", "reg_no": "921723116039"},
        {"name": "RAHUL R", "roll_no": "23AM050", "reg_no": "921723116040"},
        {"name": "RAJANEETHI S", "roll_no": "23AM009", "reg_no": "921723116041"},
        {"name": "RIZWANUL JANNAH S", "roll_no": "23AM060", "reg_no": "921723116042"},
        {"name": "SAM DERIN S", "roll_no": "23AM021", "reg_no": "921723116043"},
        {"name": "SANGAVI G S", "roll_no": "23AM055", "reg_no": "921723116044"},
        {"name": "SANJAY A", "roll_no": "23AM071", "reg_no": "921723116045"},
        {"name": "SANTHIYA B", "roll_no": "23AM017", "reg_no": "921723116046"},
        {"name": "SARAVANAKUMAR P", "roll_no": "23AM046", "reg_no": "921723116047"},
        {"name": "SHEIK ABDULLAH A", "roll_no": "23AM063", "reg_no": "921723116048"},
        {"name": "SHREEHAN M", "roll_no": "23AM064", "reg_no": "921723116049"},
        {"name": "SHYAM SUNDAR B", "roll_no": "23AM048", "reg_no": "921723116050"},
        {"name": "SIVARANJANI S", "roll_no": "23AM058", "reg_no": "921723116051"},
        {"name": "SOUNDHIRAPANDI S", "roll_no": "23AM033", "reg_no": "921723116052"},
        {"name": "SRI DHARSHINI N", "roll_no": "23AM036", "reg_no": "921723116053"},
        {"name": "SUBRAMANIYAN S", "roll_no": "23AM025", "reg_no": "921723116054"},
        {"name": "TAMILMANI A", "roll_no": "23AM031", "reg_no": "921723116055"},
        {"name": "VASUMANI RATHINAM R R", "roll_no": "23AM007", "reg_no": "921723116056"},
        {"name": "VIGNESH S", "roll_no": "23AM003", "reg_no": "921723116057"},
        {"name": "VIGNESH V", "roll_no": "23AM010", "reg_no": "921723116058"},
        {"name": "VINOTH KUMAR R", "roll_no": "23AM052", "reg_no": "921723116059"},
        {"name": "YOGESHWARAN A", "roll_no": "23AM070", "reg_no": "921723116060"}
    ]
}

# ============================================================================
# DO NOT EDIT BELOW THIS LINE (SYSTEM SETUP CODE)
# ============================================================================

def setup_subject_data():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()
        
        # Create batches and advisors
        batches = {}
        for advisor_data in ADVISORS:
            batch_name = advisor_data["batch_name"]
            
            # Check if batch already exists
            if batch_name not in batches:
                batch = Batch(name=batch_name)
                db.session.add(batch)
                db.session.flush()  # Get the batch ID
                batches[batch_name] = batch
            
            batch = batches[batch_name]
            
            advisor = Advisor(
                username=advisor_data["username"],
                password=generate_password_hash(advisor_data["password"]),
                batch_id=batch.id
            )
            db.session.add(advisor)
        
        db.session.commit()
        
        # Create semesters for each batch
        semesters = {}
        for batch_name, semester_list in SEMESTERS.items():
            batch = batches[batch_name]
            for i, semester_name in enumerate(semester_list):
                # Only semester is active by default
                is_active = True  # All semesters are active since we only have one
                semester = Semester(name=semester_name, batch_id=batch.id, is_active=is_active)
                db.session.add(semester)
                db.session.flush()  # Get the semester ID
                semesters[semester_name] = semester
        
        db.session.commit()
        
        # Create subjects for each semester
        for semester_name, subjects_list in SUBJECTS.items():
            semester = semesters[semester_name]
            for subject_name in subjects_list:
                subject = Subject(name=subject_name, semester_id=semester.id)
                db.session.add(subject)
        
        db.session.commit()
        
        # Create students for each batch
        for batch_name, students_list in STUDENTS.items():
            batch = batches[batch_name]
            for student_data in students_list:
                student = Student(
                    name=student_data["name"],
                    roll_no=student_data["roll_no"],
                    reg_no=student_data["reg_no"],
                    batch_id=batch.id
                )
                db.session.add(student)
        
        db.session.commit()
        
        # Print summary
        print("✅ Semester 5 attendance system setup successfully!")
        print("\n📋 Login Credentials:")
        print("\n👨‍🏫 Advisors:")
        for advisor_data in ADVISORS:
            print(f"  {advisor_data['batch_name']}: username={advisor_data['username']}, password={advisor_data['password']}")
        
        print("\n📚 Semesters Created:")
        for batch_name, semester_list in SEMESTERS.items():
            print(f"\n{batch_name}:")
            for i, semester in enumerate(semester_list):
                status = " (Active)"
                print(f"  - {semester}{status}")
        
        print("\n📖 Subjects Created:")
        for semester_name, subjects_list in SUBJECTS.items():
            print(f"\n{semester_name}:")
            for subject in subjects_list:
                print(f"  - {subject}")
        
        print("\n👨‍🎓 Students:")
        for batch_name, students_list in STUDENTS.items():
            print(f"{batch_name}: {len(students_list)} students")
        
        print("\n🚀 Next Steps:")
        print("1. Login as any advisor")
        print("2. Go to 'Manage Semesters' to add more semesters if needed")
        print("3. Go to 'Manage Subjects' to add subjects to Semester 5")
        print("4. Go to 'Update Attendance' to add weekly attendance by subject")
        print("5. View dashboard to see attendance breakdown")

if __name__ == "__main__":
    setup_subject_data() 