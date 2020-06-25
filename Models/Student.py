from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'

    id = Column(String, primary_key = True)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String)
    email = Column(String)

    # To become many-to-many relationship with Course
    courses = relationship("Course") 