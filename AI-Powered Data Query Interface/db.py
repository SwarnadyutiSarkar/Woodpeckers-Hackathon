# db.py
from sqlalchemy import create_engine, Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URI = 'sqlite:///clients.db'  # Change this to your database URI
engine = create_engine(DATABASE_URI)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    address = Column(Text)
    created_at = Column(TIMESTAMP)

Base.metadata.create_all(engine)
