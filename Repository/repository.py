from Models.base import session_factory
from Models.Course import Course
from Models.Student import Student
from sqlalchemy import exc

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

def update_student(newStudent):
    session = session_factory()
    student = session.query(Student).get(newStudent.id)
    student.update(newStudent)
    try:
        session.add(student)
        session.commit()
    except exc.IntegrityError:
        session.rollback()
    session.close()

def delete_student(id):
    session = session_factory()
    session.query(Student)\
        .filter(Student.id == id)\
        .delete(synchronize_session='fetch')
    session.commit()
    session.close()

def create_course(course):
    session = session_factory()
    session.add(course)
    session.commit()
    session.close()

def get_course_by_id(id):
    session = session_factory()
    course = session.query(Course).get(id)
    session.close()
    return course 

def update_course(newCourse):
    session = session_factory()
    course = session.query(Course).get(newCourse.id)
    course.update(newCourse)
    try:
        session.add(course)
        session.commit()
    except exc.IntegrityError:
        session.rollback()
    session.close()
