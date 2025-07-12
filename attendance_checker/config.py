import os

class Config:
    SECRET_KEY = 'h8snZ2_NNi1ARAyMywELq1pNzNTC1I7riSzTRomgTQg'
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'instance', 'attendance.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
