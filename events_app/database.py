from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("postgresql+psycopg2://joan:admin@localhost:5432/EPIC", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()