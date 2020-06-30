from sqlalchemy import Column, Integer, String
from .base import Base

class Course(Base):
    __tablename__ = 'course'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key = True)
    section = Column(String(10))
    cross_list = Column(String(6))
    term = Column(String(4))
    level = Column(String(1))
    title = Column(String(20))

    def __init__(self, id, section, cross_list, term, level, title):
        self.id = id
        self.section = section
        self.cross_list = cross_list
        self.term = term
        self.level = level
        self.title = title

    def __str__(self):
        return "%s %s %s %s %s %s" % (self.id, self.section, self.cross_list, self.term, self.level, self.title)