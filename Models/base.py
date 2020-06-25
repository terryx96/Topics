from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('')
_SessionFactory = sessionmaker(bind=engine)

Base = declarative_base()

# Session Factory code borrowed from
def session_factory():
    Base.metadata.create_all(engine)
    return _SessionFactory()