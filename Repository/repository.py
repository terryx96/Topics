from Models.base import session_factory
from Models.Course import Course

def get_all_courses():
    session = session_factory()
    courses_query = session.query(Course)
    session.close()
    return courses_query.all()
