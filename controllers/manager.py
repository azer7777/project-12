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