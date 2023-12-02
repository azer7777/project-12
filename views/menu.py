from controllers.manager import Manager
from controllers.auth import authenticate, register_user, update_user, delete_user
from views.entries import Entries

class Menu:
    def __init__(self):
        self.manager = Manager()

    def auth_menu(self):
        print("Welcome to the CRM Application!")
        while True:
            print("1. Log in")
            print("0. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                user_full_name, role = authenticate(username, password)
                if role:
                    print(f"Authentication successful. You are logged in as {role}.")
                    if role == "management":
                        self.management_menu(role, user_full_name)
                    elif role == "sales":
                        self.sales_menu(role, user_full_name)
                    else:
                        self.support_menu(role, user_full_name)
                else:
                    print("Authentication failed. Invalid username or password.")
            elif choice == "0":
                print("Exiting the CRM Application. Goodbye!")
                break
            else:
                print("Invalid choice.")

    def management_menu(self, role, user_full_name):
        while True:
            print(f"Menu for {role}, collaborator: {user_full_name}")
            choice = input(
            """
                1. Accounts menu              2. Create Contract        3. Update Contract 
                4. Delete Contract            5. List All Contracts     6. List All Events
                7. Events Without Support     8. Update Event           9. List All Customers
                0. Logout
                
                                             Choose an option : """
            )
            if choice == "1":
                self.manage_accounts_menu(role, user_full_name)
                break
            elif choice == "2":
                customer_id, sales_contact, total_amount, amount_remaining, creation_date, contract_status = Entries.get_contract_input()
                self.manager.create_contract(customer_id, sales_contact, total_amount, amount_remaining, creation_date, contract_status)
            elif choice == "3":
                contract_id, new_sales_contact, new_total_amount, new_amount_remaining, new_contract_status = Entries.get_contract_update_input(role)
                self.manager.update_contract(contract_id, new_sales_contact, new_total_amount, new_amount_remaining, new_contract_status, role, "")
            elif choice == "4":
                contract_id = input("Enter contract ID: ")
                self.manager.delete_contract(contract_id)
            elif choice == "5":
                contracts = self.manager.get_all_contracts()
                self.manager.display_contracts(contracts)               
            elif choice == "6":
                events = self.manager.get_all_events()
                self.manager.display_events(events)
            elif choice == "7":
                events = self.manager.get_events_without_support()
                self.manager.display_events(events)
            elif choice == "8":
                event_id, new_event_name, new_client_name, new_client_contact, new_event_start_date, new_event_end_date, new_support_contact, new_location, new_attendees, new_notes = Entries.get_event_update_input(role)
                self.manager.update_event(event_id, new_event_name, new_client_name, new_client_contact, new_event_start_date, new_event_end_date, new_support_contact, new_location, new_attendees, new_notes, role, "")
            elif choice == "9":
                customers = self.manager.get_all_customers()
                self.manager.display_customers(customers)      
            elif choice == "0":
                print("Logged Out")
                break
            else:
                print("Invalid choice.")
               
    def sales_menu(self, role, user_full_name):
        while True:
            print(f"Menu for {role}, collaborator: {user_full_name}")
            choice = input(
            """
                1. Create Customer          2. Update Customer        3. Update Contract
                4. Create Event             5. List All Contracts     6. List unsigned or not fully paid contracts 
                7. List All Events          8. List All Customers     0. Logout  
                
                                             Choose an option : """
            )
            if choice == "1":
                full_name, email, phone, company_name, creation_date, last_contact_date = Entries.get_customer_input()
                self.manager.create_customer(full_name, email, phone, company_name, creation_date, last_contact_date, sales_contact=user_full_name)
            elif choice == "2":
                customer_id, new_full_name, new_email, new_phone, new_company_name, new_last_contact_date = Entries.get_customer_update_input()
                self.manager.update_customer(customer_id, new_full_name, new_email, new_phone, new_company_name, new_last_contact_date, user_full_name)
            elif choice == "3":
                contract_id, new_sales_contact, new_total_amount, new_amount_remaining, new_contract_status = Entries.get_contract_update_input(role)
                self.manager.update_contract(contract_id, new_sales_contact, new_total_amount, new_amount_remaining, new_contract_status, role, user_full_name)
            elif choice == "4":
                event_name, contract_id, client_name, client_contact, event_start_date, event_end_date, support_contact, location, attendees, notes = Entries.get_event_input()
                self.manager.create_event(event_name, contract_id, client_name, client_contact, event_start_date, event_end_date, support_contact, location, attendees, notes, user_full_name) 
            elif choice == "5":
                contracts = self.manager.get_all_contracts()
                self.manager.display_contracts(contracts) 
            elif choice == "6":
                contracts = self.manager.get_unsigned_or_not_fully_paid_contracts()
                self.manager.display_contracts(contracts) 
            elif choice == "7":
                events = self.manager.get_all_events()
                self.manager.display_events(events)
            elif choice == "8":
                customers = self.manager.get_all_customers() 
                self.manager.display_customers(customers)                             
            elif choice == "0":
                print("Logged Out")
                break
            else:
                print("Invalid choice.")       

    def support_menu(self, role, user_full_name):
        while True:
            print(f"Menu for {role}, collaborator: {user_full_name}")
            choice = input(
            """
                1. Update Event             2. List All Customers      3. List All Contracts
                4. List All Events          5. List assigned events    0. Logout  
                
                                             Choose an option : """
            )
            if choice == "1":
                event_id, new_event_name, new_client_name, new_client_contact, new_event_start_date, new_event_end_date, new_support_contact, new_location, new_attendees, new_notes = Entries.get_event_update_input(role)
                self.manager.update_event(event_id, new_event_name, new_client_name, new_client_contact, new_event_start_date, new_event_end_date, new_support_contact, new_location, new_attendees, new_notes, role, user_full_name)
            elif choice == "2":
                customers = self.manager.get_all_customers()
                self.manager.display_customers(customers) 
            elif choice == "3":
                contracts = self.manager.get_all_contracts()
                self.manager.display_contracts(contracts)
            elif choice == "4":
                events = self.manager.get_all_events()
                self.manager.display_events(events) 
            elif choice == "5":
                events = self.manager.get_events_for_support_user(user_full_name)
                self.manager.display_events(events)                              
            elif choice == "0":
                print("Logged Out")
                break
            else:
                print("Invalid choice.")


    def manage_accounts_menu(self, role, user_full_name):
        while True:
            print("Account Menu")
            choice = input(
            """
                1. Register collaborator    2. Update collaborator    3. Delete collaborator
                4. Management menu
                
                                             Choose an option : """
            )
            if choice == "1":
                full_name, username, password, role = Entries.get_register_input()
                result = register_user(full_name, username, password, role)
                print(result)
            elif choice == "2":
                username, full_name, password = Entries.get_user_update_input()
                result = update_user(username, full_name, password)
                print(result)
            elif choice == "3":
                username = input("Enter a username: ")
                result = delete_user(username)
                print(result)
            elif choice == "4":
                self.management_menu(role, user_full_name)
                break
            else:
                print("Invalid choice.")                         
