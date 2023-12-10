from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class User(Base):
    """
    Represents a user in the CRM system.

    Attributes:
        id (int): The unique identifier for the user.
        full_name (str): The full name of the user.
        username (str): The unique username for login.
        password (str): The password associated with the user.
        role (str): The role of the user within the system (e.g., 'management', 'sales', 'support').
    """

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)


class Customer(Base):
    """
    Represents a customer in the CRM system.

    Attributes:
        id (int): The unique identifier for the customer.
        full_name (str): The full name of the customer.
        email (str): The email address of the customer.
        phone (str): The phone number of the customer.
        company_name (str): The name of the customer's company.
        creation_date (str): The date when the customer was created.
        last_contact_date (str): The date of the last contact with the customer.
        sales_contact (str): The salesperson in charge of the customer.
        contracts (relationship): Relationship to associated contracts.
    """

    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=True)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    company_name = Column(String, nullable=True)
    creation_date = Column(String, nullable=True)
    last_contact_date = Column(String, nullable=True)
    sales_contact = Column(String, nullable=True)
    contracts = relationship("Contract", back_populates="customer")


class Contract(Base):
    """
    Represents a contract in the CRM system.

    Attributes:
        id (int): The unique identifier for the contract.
        customer_id (int): The ID of the associated customer.
        sales_contact (str): The salesperson associated with the contract.
        total_amount (str): The total amount of the contract.
        amount_remaining (str): The remaining amount to be paid.
        creation_date (str): The date when the contract was created.
        contract_status (str): The status of the contract.
        customer (relationship): Relationship to the associated customer.
        events (relationship): Relationship to associated events.
    """

    __tablename__ = "contracts"
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    sales_contact = Column(String, nullable=True)
    total_amount = Column(String, nullable=True)
    amount_remaining = Column(String, nullable=True)
    creation_date = Column(String, nullable=True)
    contract_status = Column(String, nullable=True)
    customer = relationship("Customer", back_populates="contracts")
    events = relationship("Event", back_populates="contract")


class Event(Base):
    """
    Represents an event in the CRM system.

    Attributes:
        id (int): The unique identifier for the event.
        event_name (str): The name of the event.
        contract_id (int): The ID of the associated contract.
        client_name (str): The name of the client associated with the event.
        client_contact (str): The contact information of the client.
        event_start_date (str): The start date of the event.
        event_end_date (str): The end date of the event.
        support_contact (str): The support contact for the event.
        location (str): The location of the event.
        attendees (str): The number of attendees for the event.
        notes (str): Additional notes for the event.
        contract (relationship): Relationship to the associated contract.
    """

    __tablename__ = "events"
    id = Column(Integer, primary_key=True)
    event_name = Column(String, nullable=True)
    contract_id = Column(Integer, ForeignKey("contracts.id"), nullable=False)
    client_name = Column(String, nullable=True)
    client_contact = Column(String, nullable=True)
    event_start_date = Column(String, nullable=True)
    event_end_date = Column(String, nullable=True)
    support_contact = Column(String, nullable=True)
    location = Column(String, nullable=True)
    attendees = Column(String, nullable=True)
    notes = Column(String, nullable=True)
    contract = relationship("Contract", back_populates="events")


# Create an SQLite database in memory
engine = create_engine("sqlite:///crm.db")
# Create the tables in the database
Base.metadata.create_all(engine)
