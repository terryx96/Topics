from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Student(Base):
    __tablename__ = 'student'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key = True)
    first_name = Column(String(6))
    last_name = Column(String(7))
    program = Column(String(5))
    username = Column(String(10))
    email = Column(String(20))

    def __init__(self, id, first_name, last_name, program, username, email):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.program = program
        self.username = username
        self.email = email
    
    def update(self, student):
        self.first_name = student.first_name
        self.last_name = student.last_name
        self.program = student.program
        self.username = student.username
        self.email = student.email

    def __str__(self):
        return "%s %s %s %s %s %s" % (self.id, self.first_name, self.last_name, self.program, self.username, self.email)