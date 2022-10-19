from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# 写法1
engine = create_engine("mysql+pymysql://root:123456@host:3306/testsql", echo=True)

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
Session = sessionmaker(bind=engine)
database_session = Session()

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey


class User(Base):
    __tablename__ = "user"
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50))
    password = Column(String(200))
    create_time = Column(DateTime, default=datetime.now)
    role_id = Column(Integer, ForeignKey('role.role_id'))


def save():
    Base.metadata.create_all(engine)


def delete():
    Base.meta.drop_all(engine)


# if __name__ == "__main__":
#     save()
