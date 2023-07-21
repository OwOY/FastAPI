from sqlalchemy import Column, VARCHAR, create_engine
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker


engine = create_engine('db_url')
def create_session():
    try:
        session_factory = scoped_session(sessionmaker(bind=engine))
        session = session_factory()
        yield session
    except:
        raise Exception('Database connection error')

base = declarative_base(bind=engine)

class Test(base):
    __tablename__ = 'test'
    id = Column(VARCHAR(32), primary_key=True)
    foo = Column(VARCHAR(32))
    bar = Column(VARCHAR(32), nullable=False)
    