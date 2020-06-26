from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from .base import Base

association_table = Table(
    'association', Base.metadata,
    Column('course_id', Integer, ForeignKey('course.id')),
    Column('student_id', Integer, ForeignKey('student.id'))
)

class Student(Base):
    __tablename__ = 'student'

    id = Column(String(10), primary_key = True)
    first_name = Column(String(6))
    last_name = Column(String(7))
    program = Column(String(5))
    username = Column(String(10))
    email = Column(String(20))

    courses = relationship("Course", secondary=association_table) 
    
    def __init__(self, id, first_name, last_name, program, username, courses):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.program = program
        self.username = username
        self.courses = courses