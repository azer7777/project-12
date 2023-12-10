from sqlalchemy.orm import sessionmaker
from models.db import engine, Customer, Contract, Event
from sqlalchemy import text
from tabulate import tabulate


class Manager:
    """
    Represents the Manager controller in the CRM application.

    """

    def __init__(self):
        """
        Initializes a new Manager instance.

        Attributes:
            session: The database session used for CRUD operations.
        """
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def create_customer(self, full_name, email, phone, company_name, creation_date, last_contact_date, sales_contact):
        """
        Creates a new customer in the CRM system.

        Args:
            full_name (str): The full name of the customer.
            email (str): The email address of the customer.
            phone (str): The phone number of the customer.
            company_name (str): The name of the customer's company.
            creation_date (str): The date when the customer was created.
            last_contact_date (str): The date of the last contact with the customer.
            sales_contact (str): The salesperson in charge of the customer.
        """
        try:
            customer = Customer(
                full_name=full_name,
                email=email,
                phone=phone,
                company_name=company_name,
                creation_date=creation_date,
                last_contact_date=last_contact_date,
                sales_contact=sales_contact,
            )
            self.session.add(customer)
            self.session.commit()
            print("Customer created successfully.")
        except Exception as e:
            self.session.rollback()
            print(f"An error occurred: {e}")

    def update_customer(
        self, customer_id, new_full_name, new_email, new_phone, new_company_name, new_last_contact_date, user_full_name
    ):
        """
        Updates an existing customer in the CRM system.

        Args:
            customer_id (int): The ID of the customer to be updated.
            new_full_name (str): The new full name of the customer.
            new_email (str): The new email address of the customer.
            new_phone (str): The new phone number of the customer.
            new_company_name (str): The new name of the customer's company.
            new_last_contact_date (str): The new date of the last contact with the customer.
            user_full_name (str): The full name of the user initiating the update.
        """
        existing_customer = (
            self.session.query(Customer).filter_by(id=customer_id, sales_contact=user_full_name).first()
        )
        if existing_customer:
            update_dict = {
                "full_name": new_full_name,
                "email": new_email,
                "phone": new_phone,
                "company_name": new_company_name,
                "last_contact_date": new_last_contact_date,
            }
            update_dict = {key: value for key, value in update_dict.items() if value != ""}
            if update_dict:
                set_clause = ", ".join([f"{key}=:new_{key}" for key in update_dict.keys()])
                update_query = text(f"UPDATE customers SET {set_clause} WHERE id=:customer_id")
                self.session.execute(
                    update_query,
                    {**{f"new_{key}": value for key, value in update_dict.items()}, "customer_id": customer_id},
                )
                self.session.commit()
                print("Customer updated successfully.")
            else:
                print("Event updated successfully.")
        else:
            print("Customer not found or you are not in charge. Update operation aborted.")

    def get_all_customers(self):
        """
        Retrieves all customers in the CRM system.

        Returns:
            list: A list of Customer objects representing all customers.
        """
        customers = self.session.query(Customer).all()
        return customers

    def delete_customer(self, customer_id):
        """
        Deletes an existing customer from the CRM system.

        Args:
            customer_id (int): The ID of the customer to be deleted.
        """
        existing_customer = self.session.query(Customer).filter_by(id=customer_id).first()
        if existing_customer:
            delete_query = text("DELETE FROM customers WHERE id=:customer_id")
            self.session.execute(delete_query, {"customer_id": customer_id})
            self.session.commit()
            print("Customer deleted successfully.")
        else:
            print("Customer not found. Delete operation aborted.")

    def create_contract(
        self, customer_id, sales_contact, total_amount, amount_remaining, creation_date, contract_status
    ):
        """
        Creates a new contract in the CRM system.

        Args:
            customer_id (int): The ID of the customer associated with the contract.
            sales_contact (str): The salesperson responsible for the contract.
            total_amount (str): The total amount of the contract.
            amount_remaining (str): The remaining amount to be paid in the contract.
            creation_date (str): The date when the contract was created.
            contract_status (str): The status of the contract (e.g., signed, unsigned).

        Raises:
            Exception: If an error occurs during the creation process.
        """
        try:
            customer = self.session.query(Customer).filter_by(id=customer_id).first()
            if customer:
                contract = Contract(
                    customer=customer,
                    sales_contact=sales_contact,
                    total_amount=total_amount,
                    amount_remaining=amount_remaining,
                    creation_date=creation_date,
                    contract_status=contract_status,
                )
                self.session.add(contract)
                self.session.commit()
                print("Contract created successfully.")
            else:
                print(f"Customer with ID {customer_id} not found. Operation aborted.")
        except Exception as e:
            self.session.rollback()
            print(f"An error occurred: {e}")

    def update_contract(
        self,
        contract_id,
        new_sales_contact,
        new_total_amount,
        new_amount_remaining,
        new_contract_status,
        role,
        user_full_name,
    ):
        """
        Updates an existing contract in the CRM system.

        Args:
            contract_id (int): The ID of the contract to be updated.
            new_sales_contact (str): The new salesperson responsible for the contract.
            new_total_amount (str): The new total amount of the contract.
            new_amount_remaining (str): The new remaining amount to be paid in the contract.
            new_contract_status (str): The new status of the contract (e.g., signed, unsigned).
            role (str): The role of the user initiating the update.
            user_full_name (str): The full name of the user initiating the update.

        Raises:
            Exception: If an error occurs during the update process.
        """
        if role == "management":
            existing_contract = self.session.query(Contract).filter_by(id=contract_id).first()
        else:
            existing_contract = (
                self.session.query(Contract).filter_by(id=contract_id, sales_contact=user_full_name).first()
            )
        if existing_contract:
            update_dict = {
                "sales_contact": new_sales_contact,
                "total_amount": new_total_amount,
                "amount_remaining": new_amount_remaining,
                "contract_status": new_contract_status,
            }
            update_dict = {key: value for key, value in update_dict.items() if value != ""}
            if update_dict:
                set_clause = ", ".join([f"{key}=:new_{key}" for key in update_dict.keys()])
                update_query = text(f"UPDATE contracts SET {set_clause} WHERE id=:contract_id")
                self.session.execute(
                    update_query,
                    {**{f"new_{key}": value for key, value in update_dict.items()}, "contract_id": contract_id},
                )
                self.session.commit()
                print("Contract updated successfully.")
            else:
                print("Contract updated successfully.")
        else:
            print("Contract not found. Update operation aborted.")

    def get_all_contracts(self):
        """
        Retrieves all contracts in the CRM system.

        Returns:
            list: A list of Contract objects representing all contracts.
        """
        contracts = self.session.query(Contract).all()
        return contracts

    def get_unsigned_or_not_fully_paid_contracts(self):
        """
        Retrieves contracts that are unsigned or not fully paid.

        Returns:
            list: A list of Contract objects representing unsigned or not fully paid contracts.
        """
        contracts = (
            self.session.query(Contract)
            .filter((Contract.contract_status != "signed") | (Contract.amount_remaining > 0))
            .all()
        )
        return contracts

    def delete_contract(self, contract_id):
        """
        Deletes an existing contract from the CRM system.

        Args:
            contract_id (int): The ID of the contract to be deleted.

        Raises:
            Exception: If an error occurs during the deletion process.
        """
        existing_contract = self.session.query(Contract).filter_by(id=contract_id).first()
        if existing_contract:
            delete_query = text("DELETE FROM contracts WHERE id=:contract_id")
            self.session.execute(delete_query, {"contract_id": contract_id})
            self.session.commit()
            print("Contract deleted successfully.")
        else:
            print("Contract not found. Delete operation aborted.")

    def create_event(
        self,
        event_name,
        contract_id,
        client_name,
        client_contact,
        event_start_date,
        event_end_date,
        support_contact,
        location,
        attendees,
        notes,
        user_full_name,
    ):
        """
        Creates a new event in the CRM system.

        Args:
            event_name (str): The name of the event.
            contract_id (int): The ID of the associated contract.
            client_name (str): The name of the client for the event.
            client_contact (str): The contact information for the client.
            event_start_date (str): The start date of the event.
            event_end_date (str): The end date of the event.
            support_contact (str): The support contact assigned to the event.
            location (str): The location of the event.
            attendees (str): The list of attendees for the event.
            notes (str): Additional notes for the event.
            user_full_name (str): The full name of the user creating the event.

        Raises:
            Exception: If an error occurs during the creation process.
        """
        try:
            contract = self.session.query(Contract).filter_by(id=contract_id, contract_status="signed").first()
            customer = (
                self.session.query(Customer).filter_by(id=contract.customer_id, sales_contact=user_full_name).first()
            )
            if contract and customer:
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
                    notes=notes,
                )
                self.session.add(event)
                self.session.commit()
                print("Event created successfully.")
            else:
                print(
                    f"Contract with ID {contract_id} not found or not ready or you dont have access. Operation aborted."
                )
        except Exception as e:
            self.session.rollback()
            print(f"An error occurred: {e}")

    def update_event(
        self,
        event_id,
        new_event_name,
        new_client_name,
        new_client_contact,
        new_event_start_date,
        new_event_end_date,
        new_support_contact,
        new_location,
        new_attendees,
        new_notes,
        role,
        user_full_name,
    ):
        """
        Updates an existing event in the CRM system.

        Args:
            event_id (int): The ID of the event to be updated.
            new_event_name (str): The new name of the event.
            new_client_name (str): The new name of the client for the event.
            new_client_contact (str): The new contact information for the client.
            new_event_start_date (str): The new start date of the event.
            new_event_end_date (str): The new end date of the event.
            new_support_contact (str): The new support contact assigned to the event.
            new_location (str): The new location of the event.
            new_attendees (str): The new list of attendees for the event.
            new_notes (str): The new additional notes for the event.
            role (str): The role of the user initiating the update.
            user_full_name (str): The full name of the user initiating the update.

        Raises:
            Exception: If an error occurs during the update process.
        """
        if role == "management":
            existing_event = self.session.query(Event).filter_by(id=event_id).first()
        else:
            existing_event = self.session.query(Event).filter_by(id=event_id, support_contact=user_full_name).first()
        if existing_event:
            update_dict = {
                "event_name": new_event_name,
                "client_name": new_client_name,
                "client_contact": new_client_contact,
                "event_start_date": new_event_start_date,
                "event_end_date": new_event_end_date,
                "support_contact": new_support_contact,
                "location": new_location,
                "attendees": new_attendees,
                "notes": new_notes,
            }
            # Remove empty string values from the update_dict
            update_dict = {key: value for key, value in update_dict.items() if value != ""}
            if update_dict:
                # Prepare the SET part of the SQL query dynamically based on non-empty values
                set_clause = ", ".join([f"{key}=:new_{key}" for key in update_dict.keys()])
                update_query = text(f"UPDATE events SET {set_clause} WHERE id=:event_id")
                # Execute the update query with non-empty values
                self.session.execute(
                    update_query, {**{f"new_{key}": value for key, value in update_dict.items()}, "event_id": event_id}
                )
                self.session.commit()
                print("Event updated successfully.")
            else:
                print("Event updated successfully.")
        else:
            print("Event not found. Update operation aborted.")

    def get_all_events(self):
        """
        Retrieves all events in the CRM system.

        Returns:
            List[Event]: A list of all events.
        """
        events = self.session.query(Event).all()
        return events

    def get_events_without_support(self):
        """
        Retrieves events without assigned support contacts.

        Returns:
            List[Event]: A list of events without support contacts.
        """
        events = self.session.query(Event).filter(Event.support_contact.is_(None)).all()
        return events

    def get_events_for_support_user(self, support_contact):
        """
        Retrieves events assigned to a specific support contact.

        Args:
            support_contact (str): The support contact's name.

        Returns:
            List[Event]: A list of events assigned to the support contact.
        """
        events = self.session.query(Event).filter_by(support_contact=support_contact).all()
        return events

    def delete_event(self, event_id):
        """
        Deletes an existing event from the CRM system.

        Args:
            event_id (int): The ID of the event to be deleted.

        Raises:
            Exception: If an error occurs during the deletion process.
        """
        existing_event = self.session.query(Event).filter_by(id=event_id).first()
        if existing_event:
            delete_query = text("DELETE FROM events WHERE id=:event_id")
            self.session.execute(delete_query, {"event_id": event_id})
            self.session.commit()
            print("Event deleted successfully.")
        else:
            print("Event not found. Update operation aborted.")

    def display_customers(self, customers):
        """
        Displays customer information in a formatted table.

        Args:
            customers (List[Customer]): A list of customer objects.

        Returns:
            None
        """
        if customers:
            headers = [
                "ID",
                "Full Name",
                "Email",
                "Phone",
                "Company Name",
                "Creation Date",
                "Last Contact Date",
                "Sales Contact",
            ]
            table = [
                [
                    customer.id,
                    customer.full_name,
                    customer.email,
                    customer.phone,
                    customer.company_name,
                    customer.creation_date,
                    customer.last_contact_date,
                    customer.sales_contact,
                ]
                for customer in customers
            ]
            print(tabulate(table, headers=headers, tablefmt="pretty"))
        else:
            print("No customers found in the database.")

    def display_contracts(self, contracts):
        """
        Displays contract information in a formatted table.

        Args:
            contracts (List[Contract]): A list of contract objects.

        Returns:
            None
        """
        if contracts:
            headers = [
                "ID",
                "Customer ID",
                "Customer Information",
                "Sales Contact",
                "Total Amount",
                "Amount Remaining",
                "Creation Date",
                "Contract Status",
            ]
            table = []
            for contract in contracts:
                customer = self.session.query(Customer).filter_by(id=contract.customer_id).first()
                if customer:
                    customer_info = f"Name:{customer.full_name}\nEmail:{customer.email}\nPhone:{customer.phone}\n"
                else:
                    customer_info = "Customer not found"
                table.append(
                    [
                        contract.id,
                        contract.customer_id,
                        customer_info,
                        contract.sales_contact,
                        contract.total_amount,
                        contract.amount_remaining,
                        contract.creation_date,
                        contract.contract_status,
                    ]
                )
            print(tabulate(table, headers=headers, tablefmt="pretty"))
        else:
            print("No contracts found in the database.")

    def display_events(self, events):
        """
        Displays event information in a formatted table.

        Args:
            events (List[Event]): A list of event objects.

        Returns:
            None
        """
        if events:
            headers = [
                "ID",
                "Event Name",
                "Contract ID",
                "Client Name",
                "Client Contact",
                "Event Start Date",
                "Event End Date",
                "Support Contact",
                "Location",
                "Attendees",
                "Notes",
            ]
            table = [
                [
                    event.id,
                    event.event_name,
                    event.contract_id,
                    event.client_name,
                    event.client_contact,
                    event.event_start_date,
                    event.event_end_date,
                    event.support_contact,
                    event.location,
                    event.attendees,
                    event.notes,
                ]
                for event in events
            ]
            print(tabulate(table, headers=headers, tablefmt="pretty"))
        else:
            print("No events found in the database.")
