import os

class Config:
    SECRET_KEY = 'your-secret-key'
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'instance', 'attendance.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
