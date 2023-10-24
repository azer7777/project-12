from sqlalchemy.orm import sessionmaker
from models.db import engine, Customer, Contract, Event
from sqlalchemy import text
from tabulate import tabulate

class Manager:
    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def create_customer(self, full_name, email, phone, company_name, creation_date, last_contact_date, sales_contact):
        try:
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
        except Exception as e:
            self.session.rollback()
            print(f"An error occurred: {e}")

    def update_customer(self, customer_id, new_email, new_phone, user_full_name):
        existing_customer = self.session.query(Customer).filter_by(id=customer_id, sales_contact=user_full_name).first()
        if existing_customer:
            update_query = text("UPDATE customers SET email=:new_email, phone=:new_phone WHERE id=:customer_id")
            self.session.execute(update_query, {"new_email": new_email, "new_phone": new_phone, "customer_id": customer_id})
            self.session.commit()
            print("Customer updated successfully.")
        else:
            print("Customer not found. Update operation aborted.")

    def get_all_customers(self):
        customers = self.session.query(Customer).all()
        return customers

            
    def delete_customer(self, customer_id):
        existing_customer = self.session.query(Customer).filter_by(id=customer_id).first()
        if existing_customer:
            delete_query = text("DELETE FROM customers WHERE id=:customer_id")
            self.session.execute(delete_query, {"customer_id": customer_id})
            self.session.commit()
            print("Customer deleted successfully.")
        else:
            print("Customer not found. Delete operation aborted.")
            
    def create_contract(self, customer_id, sales_contact, total_amount, amount_remaining, creation_date, contract_status):
        try:
            customer = self.session.query(Customer).filter_by(id=customer_id).first()
            if customer:
                contract = Contract(
                    customer=customer,
                    sales_contact=sales_contact,
                    total_amount=total_amount,
                    amount_remaining=amount_remaining,
                    creation_date=creation_date,
                    contract_status=contract_status
                )
                self.session.add(contract)
                self.session.commit()
                print("Contract created successfully.")
            else:
                print(f"Customer with ID {customer_id} not found. operation aborted.")
        except Exception as e:
            self.session.rollback()
            print(f"An error occurred: {e}")
    
    def update_contract(self, contract_id, new_status, new_amount_remaining):
        existing_contract = self.session.query(Contract).filter_by(id=contract_id).first()
        if existing_contract:
            update_query = text("UPDATE contracts SET contract_status=:new_status, amount_remaining=:new_amount_remaining WHERE id=:contract_id")
            self.session.execute(update_query, {"new_status": new_status, "new_amount_remaining": new_amount_remaining, "contract_id": contract_id})
            self.session.commit()
            print("Contract updated successfully.")
        else:
            print("Contract not found. Update operation aborted.")

    def update_contract_for_sales(self, contract_id, new_status, new_amount_remaining, user_name):
        existing_contract = self.session.query(Contract).filter_by(id=contract_id, commercial_contact=user_name).first()
        if existing_contract:
            update_query = text("UPDATE contracts SET contract_status=:new_status, amount_remaining=:new_amount_remaining WHERE id=:contract_id")
            self.session.execute(update_query, {"new_status": new_status, "new_amount_remaining": new_amount_remaining, "contract_id": contract_id})
            self.session.commit()
            print("Contract updated successfully.")
        else:
            print("Contract not found. Update operation aborted.")

    def get_all_contracts(self):
        contracts = self.session.query(Contract).all()
        return contracts
    
    def get_unsigned_or_not_fully_paid_contracts(self):
        contracts = self.session.query(Contract).filter(
            (Contract.contract_status != "signed") | (Contract.amount_remaining > 0)
        ).all()
        return contracts

    def delete_contract(self, contract_id):
        existing_contract = self.session.query(Contract).filter_by(id=contract_id).first()
        if existing_contract:
            delete_query = text("DELETE FROM contracts WHERE id=:contract_id")
            self.session.execute(delete_query, {"contract_id": contract_id})
            self.session.commit()
            print("Contract deleted successfully.")
        else:
            print("Contract not found. Delete operation aborted.")

    def create_event(self, event_name, contract_id, client_name, client_contact, event_start_date, event_end_date,
                     support_contact, location, attendees, notes):
        try:
            contract = self.session.query(Contract).filter_by(id=contract_id).first()
            if contract:
                event = Event(
                    event_name=event_name,
                    contract_id=contract_id,
                    client_name=client_name,
                    client_contact=client_contact,
                    event_start_date=event_start_date,
                    event_end_date=event_end_date,
                    support_contact=support_contact,
                    location=location,
                    attendees=attendees,
                    notes=notes
                )
                self.session.add(event)
                self.session.commit()
                print("Event created successfully.")
            else:
                print(f"Contract with ID {contract_id} not found. operation aborted.")
        except Exception as e:
            self.session.rollback()
            print(f"An error occurred: {e}")

    def update_event(self, event_id, new_support_contact, new_location, new_notes, role, user_full_name):
        if role == "management":
            existing_event = self.session.query(Event).filter_by(id=event_id).first()
        else:
            existing_event = self.session.query(Event).filter_by(id=event_id, support_contact=user_full_name).first()

        if existing_event:
            update_query = text("UPDATE events SET support_contact=:new_support_contact, location=:new_location, notes=:new_notes WHERE id=:event_id")
            self.session.execute(update_query, {"new_support_contact": new_support_contact, "new_location": new_location, "new_notes": new_notes, "event_id": event_id})
            self.session.commit()
            print("Event updated successfully.")
        else:
            print("Event not found. Update operation aborted.")

    def get_all_events(self):
        events = self.session.query(Event).all()
        return events
    
    def get_events_without_support(self):
        events = self.session.query(Event).filter(Event.support_contact.is_(None)).all()
        return events

    def get_events_for_support_user(self, support_contact):
        events = self.session.query(Event).filter_by(support_contact=support_contact).all()
        return events

    def delete_event(self, event_id):
        existing_event = self.session.query(Event).filter_by(id=event_id).first()
        if existing_event:
            delete_query = text("DELETE FROM events WHERE id=:event_id")
            self.session.execute(delete_query, {"event_id": event_id})
            self.session.commit()
            print("Event deleted successfully.")
        else:
            print("Event not found. Update operation aborted.")

    def display_customers(self, customers):
        if customers:
            headers = ["ID", "Full Name", "Email", "Phone", "Company Name", "Creation Date", "Last Contact Date", "Sales Contact"]
            table = [
                [customer.id, customer.full_name, customer.email, customer.phone, customer.company_name,
                 customer.creation_date, customer.last_contact_date, customer.sales_contact] for customer in customers
            ]
            print(tabulate(table, headers=headers, tablefmt="pretty"))
        else:
            print("No customers found in the database.")
            
    def display_contracts(self, contracts):
        if contracts:
            headers = ["ID", "Customer ID", "Sales Contact", "Total Amount", "Amount Remaining", "Creation Date", "Contract Status"]
            table = [
                [contract.id, contract.customer_id, contract.sales_contact, contract.total_amount, 
                 contract.amount_remaining, contract.creation_date, contract.contract_status] for contract in contracts
            ]
            print(tabulate(table, headers=headers, tablefmt="pretty"))
        else:
            print("No contracts found in the database.")        

    def display_events(self, events):
        if events:
            headers = ["ID", "Event Name", "Contract ID", "Client Name", "Client Contact", 
                       "Event Start Date", "Event End Date", "Support Contact", 
                       "Location", "Attendees", "Notes"]
            table = [
                [event.id, event.event_name, event.contract_id, event.client_name, 
                 event.client_contact, event.event_start_date, event.event_end_date, 
                 event.support_contact, event.location, event.attendees, event.notes] 
                for event in events
            ]
            print(tabulate(table, headers=headers, tablefmt="pretty"))
        else:
            print("No events found in the database.")     
