from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from .base import Base

association_table = Table(
    'association', Base.metadata,
    Column('course_id', Integer, ForeignKey('course.id')),
    Column('student_id', Integer, ForeignKey('student.id'))
)

class Course(Base):
    __tablename__ = 'Course'

    id = Column(String(10), primary_key = True)
    cross_list = Column(String(6))
    term = Column(String(4))
    level = Column(String(1))
    title = Column(String(20))

    students = relationship("Student", secondary=association_table)

    def __init__(self, id, cross_list, term, level, title, students):
        self.id = id
        self.cross_list = cross_list
        self.term = term
        self.level = level
        self.title = title
        self.students = students