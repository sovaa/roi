from functools import wraps

from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy import create_engine

DeclarativeBase = declarative_base()


def with_session(view_func):
    @wraps(view_func)
    def wrapped(*args, **kwargs):
        session = DatabaseRdbms.db.Session()
        try:
            kwargs['session'] = session
            return view_func(*args, **kwargs)
        except:
            session.rollback()
            raise
        finally:
            DatabaseRdbms.db.Session.remove()
    return wrapped


class Database(object):
    def __init__(self):
        self.engine = self.db_connect()
        self.create_tables(self.engine)
        session_factory = sessionmaker(bind=self.engine)
        self.Session = scoped_session(session_factory)

    def db_connect(self):
        return create_engine('sqlite:///sqlalchemy_roi.db')

    def truncate(self):
        DeclarativeBase.metadata.drop_all(self.engine)

    def create_tables(self, engine):
        DeclarativeBase.metadata.create_all(engine)


class DatabaseRdbms(object):
    db = None

    def __init__(self):
        DatabaseRdbms.db = Database()


class Investment(DeclarativeBase):
    __tablename__ = 'investment'

    id = Column(Integer, autoincrement=True, primary_key=True)
    tag = Column(String)
    amount = Column(Float)
    cost = Column(Float)
    currency = Column(String(3))
    timestamp = Column(DateTime)

    def __repr__(self):
        return '<Investment[%s] %s [amount=%s, cost=%s, currency=%s, timestamp=%s]>' % (
            self.id,
            self.tag,
            self.amount,
            self.cost,
            self.currency,
            str(self.timestamp)
        )