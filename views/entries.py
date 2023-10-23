import datetime


class Entries:
    def get_register_input():
        while True:
            try:
                full_name = input("Enter a full name: ")
                username = input("Enter a username: ")
                password = input("Enter a password: ")
                role = input("Enter a role (management, sales, or support): ")
                if role.lower() not in ["management", "sales", "support"]:
                    raise ValueError("Invalid role. Please enter management, sales, or support.")
                return full_name, username, password, role.lower()
            except ValueError as e:
                print(e)
            except Exception as e:
                print(f"An error occurred: {e}. Please try again.")
                
    def get_user_update_input():
        while True:
            try:
                username = input("Enter a username: ")
                full_name = input("Enter a new full name: ")
                password = input("Enter a new password: ")
                return username, full_name, password
            except Exception as e:
                print(f"An error occurred: {e}. Please try again.")
    
    def get_customer_input():
        while True:
            try:
                full_name = input("Enter full name: ")
                email = input("Enter email: ")
                phone = input("Enter phone number: ")
                company_name = input("Enter company name: ")
                creation_date = Entries.check_date_format("Enter creation date")
                last_contact_date = Entries.check_date_format("Enter last contact date")
                sales_contact = input("Enter sales contact: ")
                return full_name, email, phone, company_name, creation_date, last_contact_date, sales_contact
            except Exception as e:
                print(f"An error occurred: {e}. Please try again.")    
    
    def get_customer_update_input():
        while True:
            try:
                customer_id = int(input("Enter customer ID: "))
                new_email = input("Enter new email: ")
                new_phone = input("Enter new phone: ")
                return customer_id, new_email, new_phone
    
            except ValueError:
                print("Invalid input. Please enter a valid integer for customer ID.")
            except Exception as e:
                print(f"An error occurred: {e}. Please try again.")
        
    def get_contract_input():
        while True:
            try:
                customer_id = int(input("Enter customer ID: "))
                sales_contact = input("Enter sales contact: ")
                total_amount = float(input("Enter total amount: "))
                amount_remaining = float(input("Enter amount remaining: "))
                creation_date = Entries.check_date_format("Enter creation date")
                contract_status = input("Enter contract status: ")
                return customer_id, sales_contact, total_amount, amount_remaining, creation_date, contract_status
            except ValueError:
                print(
                    "Invalid input. Please enter a valid number for customer ID, total amount, and amount remaining."
                )
            except Exception as e:
                print(f"An error occurred: {e}. Please try again.")

    def get_contract_update_input():
        while True:
            try:
                contract_id = int(input("Enter contract ID: "))
                new_status = input("Enter contract new status (or press Enter to keep current status): ")
                if not new_status:
                    new_status = None
                new_amount_remaining_input = input("Enter amount remaining (or press Enter to keep current amount): ")
                if new_amount_remaining_input:
                    new_amount_remaining = float(new_amount_remaining_input)
                else:
                    new_amount_remaining = None
                return contract_id, new_status, new_amount_remaining
            except ValueError:
                print(
                    "Invalid input. Please enter a valid integer for contract ID and a valid number for amount remaining."
                )
            except Exception as e:
                print(f"An error occurred: {e}. Please try again.")
                              
    def get_event_input():
        while True:
            try:
                event_name = input("Enter event name: ")
                event_id = int(input("Enter event ID: "))
                contract_id = int(input("Enter contract ID: "))
                client_name = input("Enter client name: ")
                client_contact = input("Enter client contact: ")
                event_start_date = Entries.check_date_format("Enter event start date")
                event_end_date = Entries.check_date_format("Enter event end date")
                support_contact = input("Enter support contact: ")
                location = input("Enter location: ")
                attendees = int(input("Enter number of attendees: "))
                notes = input("Enter notes: ")
                return event_name, event_id, contract_id, client_name, client_contact, event_start_date, event_end_date, support_contact, location, attendees, notes
            except ValueError:
                print("Invalid input. Please enter valid integers for event ID, contract ID, and number of attendees.")
            except Exception as e:
                print(f"An error occurred: {e}. Please try again.")

    def get_event_update_input(role):
        while True:
            try:
                event_id = int(input("Enter event ID: "))
                new_support_contact = None
                new_location = None
                new_notes = None
                if role == "management":
                    new_support_contact = input("Enter new support contact (or press Enter to keep current support contact): ")
                if role == "support":
                    new_location = input("Enter new location (or press Enter to keep current location): ")
                if role == "support":
                    new_notes = input("Enter new notes (or press Enter to keep current notes): ")
                return event_id, new_support_contact, new_location, new_notes
            except ValueError:
                print("Invalid input. Please enter a valid integer for event ID.")
            except Exception as e:
                print(f"An error occurred: {e}. Please try again.")

    def check_date_format(message):
        date = input(f"{message} (YYYY-MM-DD): ")
        if date != "":
            while True:
                try:
                    date == (datetime.datetime.strptime(date, "%d/%m/%Y")).date()
                    break
                except ValueError:
                    print("    Inccorect date format !")
                    print("    Try again")
                    date = input(f"{message} (YYYY-MM-DD): ")
        return date
