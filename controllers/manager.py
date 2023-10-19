from sqlalchemy.orm import sessionmaker
from models.db import engine, Customer, Contract, Event

class Manager:
    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def create_customer(self, full_name, email, phone, company_name, creation_date, last_contact_date, sales_contact):
        customer = Customer(full_name=full_name, email=email, phone=phone, company_name=company_name,
                            creation_date=creation_date, last_contact_date=last_contact_date, sales_contact=sales_contact)
        self.session.add(customer)
        self.session.commit()
        print("Customer created successfully.")

    def update_customer(self, customer_id, new_email, new_phone):
        customer = self.session.query(Customer).filter(Customer.id == customer_id).first()
        if customer:
            customer.email = new_email
            customer.phone = new_phone
            self.session.commit()
            print("Customer updated successfully.")
        else:
            print("Customer not found.")

    def get_all_customers(self):
        customers = self.session.query(Customer).all()
        return customers

    def delete_customer(self, customer_id):
        customer = self.session.query(Customer).filter(Customer.id == customer_id).first()
        if customer:
            self.session.delete(customer)
            self.session.commit()
            print("Customer deleted successfully.")
        else:
            print("Customer not found.")

    def create_contract(self, customer_id, sales_contact, total_amount, amount_remaining, creation_date, contract_status):
        contract = Contract(customer_id=customer_id, sales_contact=sales_contact, total_amount=total_amount,
                            amount_remaining=amount_remaining, creation_date=creation_date, contract_status=contract_status)
        self.session.add(contract)
        self.session.commit()
        print("Contract created successfully.")

    def update_contract(self, contract_id, new_status, new_amount_remaining):
        contract = self.session.query(Contract).filter(Contract.id == contract_id).first()
        if contract:
            contract.contract_status = new_status
            contract.amount_remaining = new_amount_remaining
            self.session.commit()
            print("Contract updated successfully.")
        else:
            print("Contract not found.")

    def get_all_contracts(self):
        contracts = self.session.query(Contract).all()
        return contracts

    def delete_contract(self, contract_id):
        contract = self.session.query(Contract).filter(Contract.id == contract_id).first()
        if contract:
            self.session.delete(contract)
            self.session.commit()
            print("Contract deleted successfully.")
        else:
            print("Contract not found.")

    def create_event(self, event_name, event_id, contract_id, client_name, client_contact, event_start_date, event_end_date,
                     support_contact, location, notes):
        event = Event(event_name=event_name, event_id=event_id, contract_id=contract_id, client_name=client_name,
                      client_contact=client_contact, event_start_date=event_start_date, event_end_date=event_end_date,
                      support_contact=support_contact, location=location, notes=notes)
        self.session.add(event)
        self.session.commit()
        print("Event created successfully.")

    def update_event(self, event_id, new_support_contact, new_location, new_notes):
        event = self.session.query(Event).filter(Event.id == event_id).first()
        if event:
            event.support_contact = new_support_contact
            event.location = new_location
            event.notes = new_notes
            self.session.commit()
            print("Event updated successfully.")
        else:
            print("Event not found.")

    def get_all_events(self):
        events = self.session.query(Event).all()
        return events

    def delete_event(self, event_id):
        event = self.session.query(Event).filter(Event.id == event_id).first()
        if event:
            self.session.delete(event)
            self.session.commit()
            print("Event deleted successfully.")
        else:
            print("Event not found.")
