from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("postgresql+psycopg2://joan:admin@localhost:5432/EPIC", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Client(Base):
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(20))
    last_name = Column(String(20))
    email = Column(String(25), nullable=False)
    phone_number = Column(Integer)
    compagny_name = Column(String(25))
    date_created = Column(Date)
    date_updated = Column(Date)
    sales_contact = Column(Integer)

    def __repr__(self):
        return f"{self.first_name} {self.email} {self.phone_number}"

Base.metadata.create_all(engine)