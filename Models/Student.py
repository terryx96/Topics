from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from base import Base

class Student(Base):
    __tablename__ = 'student'

    id = Column(String, primary_key = True)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String)
    email = Column(String)

    # To become many-to-many relationship with Course
    courses = relationship("Course") 
    
    def __init__(self, id, first_name, last_name, username, courses):
        self.id = id,
        self.first_name = first_name,
        self.last_name = last_name,
        self.username = username,
        self.courses = courses