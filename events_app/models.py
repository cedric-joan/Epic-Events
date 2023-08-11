from sqlalchemy import create_engine, Column, Integer, String, Date, Float, ForeignKey, Boolean, Text
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
    sales_contact = Column(ForeignKey("usermanager.id"))

    def __repr__(self):
        return f"{self.first_name} {self.email} {self.phone_number}"


class Contract(Base):
    __tablename__ = "contract"

    id = Column(Integer, primary_key=True)
    client_id = Column(ForeignKey("client.id"))
    sales_contact_id = Column(Integer)
    total_amount = Column(Float)
    remaining_amount = Column(Float)
    date_created = Column(Date)
    contract_status = Column(Boolean)

    def __repr__(self):
        return f"{self.client_id} {self.date_created} {self.contract_status}"


class Event(Base):
    __tablename__ = "event"

    id = Column(Integer, primary_key=True)
    title = Column(String(25))
    contract_id = Column(ForeignKey("contract.id"))
    client_name = Column(String(20))
    client_contact = Column(String(20))
    event_date_start = Column(Date)
    event_date_end = Column(Date)
    support_contact = Column(String(25))
    location = Column(String(25))
    attendees = Column(Integer)
    notes = Column(String(300))

    def __repr__(self):
        return f"{self.title} {self.event_date_end} {self.location}"
    
Base.metadata.create_all(engine)