from Models.base import session_factory
from Models.Course import Course

def get_all_courses():
    session = session_factory()
    courses_query = session.query(Course)
    session.close()
    return courses_query.all()

def create_student():
    session = session_factory()
    session.close()
    return 

def get_student_by_id(id):
    session = session_factory()
    session.close()
    return 

def update_student():
    session = session_factory()
    session.close()

def delete_student():
    session = session_factory()
    session.close()
