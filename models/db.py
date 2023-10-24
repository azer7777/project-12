from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone = Column(String, nullable=True)
    company_name = Column(String, nullable=True)
    creation_date = Column(String, nullable=True)
    last_contact_date = Column(String, nullable=True)
    sales_contact = Column(String, nullable=True)
    contracts = relationship('Contract', back_populates='customer')

class Contract(Base):
    __tablename__ = 'contracts'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    sales_contact = Column(String, nullable=True)
    total_amount = Column(String, nullable=True)
    amount_remaining = Column(String, nullable=True)
    creation_date = Column(String, nullable=True)
    contract_status = Column(String, nullable=True)
    customer = relationship('Customer', back_populates='contracts')
    events = relationship('Event', back_populates='contract')

class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True) 
    event_name = Column(String, nullable=True)   
    contract_id = Column(Integer, ForeignKey('contracts.id'), nullable=False)
    client_name = Column(String, nullable=True)
    client_contact = Column(String, nullable=True)
    event_start_date = Column(String, nullable=True)
    event_end_date = Column(String, nullable=True)
    support_contact = Column(String, nullable=True)
    location = Column(String, nullable=True)
    attendees = Column(String, nullable=True)
    notes = Column(String, nullable=True)
    contract = relationship('Contract', back_populates='events')

# Create an SQLite database in memory
engine = create_engine('sqlite:///crm.db')
# Create the tables in the database
Base.metadata.create_all(engine)


