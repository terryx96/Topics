from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from .base import Base

class Course(Base):
    __tablename__ = 'Course'
    __table_args__ = {'extend_existing': True}

    id = Column(String(10), primary_key = True)
    cross_list = Column(String(6))
    term = Column(String(4))
    level = Column(String(1))
    title = Column(String(20))

    # students = relationship("Student",
    #                         back_populates = "courses")

    # def __init__(self, id, cross_list, term, level, title, students):
    def __init__(self, id, cross_list, term, level, title):
        self.id = id
        self.cross_list = cross_list
        self.term = term
        self.level = level
        self.title = title
        #self.students = students