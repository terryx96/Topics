from Models.base import session_factory
from Models.Course import Course
from Models.Student import Student
from sqlalchemy import exc

class Repository():

    def __init__(self):
        pass

    def create_student(self, student):
        session = session_factory()
        session.add(student)
        session.commit()
        session.close()

    def get_student_by_id(self, id):
        session = session_factory()
        student = session.query(Student).get(id)
        session.close()
        return student 

    def update_student(self, newStudent):
        session = session_factory()
        student = session.query(Student).get(newStudent.id)
        student.update(newStudent)
        try:
            session.add(student)
            session.commit()
        except exc.IntegrityError:
            session.rollback()
        session.close()

    def delete_student(self, id):
        session = session_factory()
        session.query(Student)\
            .filter(Student.id == id)\
            .delete(synchronize_session='fetch')
        session.commit()
        session.close()

    def create_course(self, course):
        session = session_factory()
        session.add(course)
        session.commit()
        session.close()

    def get_course_by_id(self, id):
        session = session_factory()
        course = session.query(Course).get(id)
        session.close()
        return course 

    def update_course(self, newCourse):
        session = session_factory()
        course = session.query(Course).get(newCourse.id)
        course.update(newCourse)
        try:
            session.add(course)
            session.commit()
        except exc.IntegrityError:
            session.rollback()
        session.close()

    def delete_course(self, id):
        session = session_factory()
        session.query(Course)\
            .filter(Course.id == id)\
            .delete(synchronize_session='fetch')
        session.commit()
        session.close()
