from Models.base import session_factory
from Models import Course as cr
import random
import string

def create_courses():
    session = session_factory()
    for i in range(10):
        course = random_course()
        session.add(course)
    session.commit()
    session.close()

def random_course():
    letters = string.ascii_lowercase
    section = "".join(random.choice(letters) for i in range(10))
    xlist = "".join(random.choice(letters) for i in range(6))
    term = "".join(random.choice(letters) for i in range(4))
    level = "".join(random.choice(letters) for i in range(1))
    title = "".join(random.choice(letters) for i in range(20))
    return cr.Course(section, xlist, term, level, title, [])

if __name__ == "__main__":


    create_courses()
