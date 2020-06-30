from Models.base import session_factory
from Models.Course import Course
from Models.Student import Student

def create_student(student):
    session = session_factory()
    session.add(student)
    session.commit()
    session.close()

def get_student_by_id(id):
    session = session_factory()
    student = session.query(Student).get(id)
    session.close()
    return student 

def update_student():
    session = session_factory()
    session.close()

def delete_student(id):
    session = session_factory()
    session.query(Student)\
        .filter(Student.id == id)\
        .delete(synchronize_session='fetch')
    session.commit()
    session.close()
