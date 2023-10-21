from sqlalchemy.orm import sessionmaker
from models.db import engine, Customer, Contract, Event
from sqlalchemy import text

class Manager:
    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def create_customer(self, full_name, email, phone, company_name, creation_date, last_contact_date, sales_contact):
        customer = Customer(
            full_name=full_name,
            email=email,
            phone=phone,
            company_name=company_name,
            creation_date=creation_date,
            last_contact_date=last_contact_date,
            sales_contact=sales_contact
        )
        self.session.add(customer)
        self.session.commit()
        print("Customer created successfully.")

    def update_customer(self, customer_id, new_email, new_phone):
        update_query = text("UPDATE customers SET email=:new_email, phone=:new_phone WHERE id=:customer_id")
        self.session.execute(update_query, {"new_email": new_email, "new_phone": new_phone, "customer_id": customer_id})
        self.session.commit()
        print("Customer updated successfully.")

    def get_all_customers(self):
        customers = self.session.query(Customer).all()
        return customers

    def delete_customer(self, customer_id):
        delete_query = text("DELETE FROM customers WHERE id=:customer_id")
        self.session.execute(delete_query, {"customer_id": customer_id})
        self.session.commit()
        print("Customer deleted successfully.")

    def create_contract(self, customer_id, customer_information, commercial_contact, total_amount, amount_remaining, creation_date, contract_status):
        contract = Contract(
            customer_id=customer_id,
            customer_information=customer_information,
            commercial_contact=commercial_contact,
            total_amount=total_amount,
            amount_remaining=amount_remaining,
            creation_date=creation_date,
            contract_status=contract_status
        )
        self.session.add(contract)
        self.session.commit()
        print("Contract created successfully.")

    def update_contract(self, contract_id, new_status, new_amount_remaining):
        update_query = text("UPDATE contracts SET contract_status=:new_status, amount_remaining=:new_amount_remaining WHERE id=:contract_id")
        self.session.execute(update_query, {"new_status": new_status, "new_amount_remaining": new_amount_remaining, "contract_id": contract_id})
        self.session.commit()
        print("Contract updated successfully.")

    def get_all_contracts(self):
        contracts = self.session.query(Contract).all()
        return contracts

    def delete_contract(self, contract_id):
        delete_query = text("DELETE FROM contracts WHERE id=:contract_id")
        self.session.execute(delete_query, {"contract_id": contract_id})
        self.session.commit()
        print("Contract deleted successfully.")

    def create_event(self, event_name, event_id, contract_id, client_name, client_contact, event_start_date, event_end_date,
                     support_contact, location, notes):
        event = Event(
            event_name=event_name,
            event_id=event_id,
            contract_id=contract_id,
            client_name=client_name,
            client_contact=client_contact,
            event_start_date=event_start_date,
            event_end_date=event_end_date,
            support_contact=support_contact,
            location=location,
            notes=notes
        )
        self.session.add(event)
        self.session.commit()
        print("Event created successfully.")

    def update_event(self, event_id, new_support_contact, new_location, new_notes):
        update_query = text("UPDATE events SET support_contact=:new_support_contact, location=:new_location, notes=:new_notes WHERE id=:event_id")
        self.session.execute(update_query, {"new_support_contact": new_support_contact, "new_location": new_location, "new_notes": new_notes, "event_id": event_id})
        self.session.commit()
        print("Event updated successfully.")

    def get_all_events(self):
        events = self.session.query(Event).all()
        return events
    
    def get_events_without_support(self):
        events = self.session.query(Event).filter(Event.support_contact.is_(None)).all()
        return events

    def delete_event(self, event_id):
        delete_query = text("DELETE FROM events WHERE id=:event_id")
        self.session.execute(delete_query, {"event_id": event_id})
        self.session.commit()
        print("Event deleted successfully.")
