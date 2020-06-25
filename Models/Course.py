from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from base import Base

class Course(Base):
    __tablename__ = 'Course'

    id = Column(String, primary_key = True)
    cross_list = Column(String)
    term = Column(String)
    level = Column(String)
    title = Column(String)

    # To become many-to-many relationship with Student
    students = relationship("Student")

    def __init__(self, id, cross_list, term, level, title, students):
        self.id = id,
        self.cross_list = cross_list,
        self.term = term,
        self.level = level,
        self.title = title,
        self.students = students