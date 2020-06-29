from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from .base import Base

# association_table = Table(
#     'association', Base.metadata, 
#     Column('course_id', String(10), ForeignKey('course.id')),
#     Column('student_id', String(10), ForeignKey('student.id')),
#     __table_args__ = {'extend_existing': True}
# )

class Student(Base):
    __tablename__ = 'student'
    __table_args__ = {'extend_existing': True}

    id = Column(String(10), primary_key = True)
    first_name = Column(String(6))
    last_name = Column(String(7))
    program = Column(String(5))
    username = Column(String(10))
    email = Column(String(20))

    #courses = relationship("Course", 
    #                        secondary=association_table,
    #                       back_populates = "students") 
    
    #def __init__(self, id, first_name, last_name, program, username, email, courses):
    def __init__(self, id, first_name, last_name, program, username, email):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.program = program
        self.username = username
        self.email = email
    #    self.courses = courses