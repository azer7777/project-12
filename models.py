from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone = Column(String)
    company_name = Column(String)
    creation_date = Column(Date, nullable=False)
    last_contact_date = Column(Date)
    sales_contact = Column(String)
    contracts = relationship('Contract', back_populates='customer')

class Contract(Base):
    __tablename__ = 'contracts'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    sales_contact = Column(String, nullable=False)
    total_amount = Column(Float, nullable=False)
    amount_remaining = Column(Float, nullable=False)
    creation_date = Column(Date, nullable=False)
    contract_status = Column(String, nullable=False)
    customer = relationship('Customer', back_populates='contracts')
    events = relationship('Event', back_populates='contract')

class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    event_name = Column(String, nullable=False)
    event_id = Column(String, nullable=False)
    contract_id = Column(Integer, ForeignKey('contracts.id'), nullable=False)
    client_name = Column(String, nullable=False)
    client_contact = Column(String, nullable=False)
    event_start_date = Column(Date, nullable=False)
    event_end_date = Column(Date, nullable=False)
    support_contact = Column(String, nullable=False)
    location = Column(String, nullable=False)
    notes = Column(String)
    contract = relationship('Contract', back_populates='events')

# Create an SQLite database in memory
engine = create_engine('sqlite:///crm.db')

# Create the tables in the database
Base.metadata.create_all(engine)


