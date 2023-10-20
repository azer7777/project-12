from controllers.manager import Manager
from controllers.auth import authenticate, authorize, register_user, modify_user, delete_user

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
                role = authenticate(username, password)
                if role:
                    print(f"Authentication successful. You are logged in as {role}.")
                    if role == "management":
                        self.management_menu(role)
                    elif role == "sales":
                        self.sales_menu(role)
                    else:
                        self.support_menu(role)
                else:
                    print("Authentication failed. Invalid username or password.")
            elif choice == "0":
                print("Exiting the CRM Application. Goodbye!")
                break
            else:
                print("Invalid choice.")

    def management_menu(self, user_role):
        print(f"Menu for {user_role}")
        print("1. Register collaborator")
        print("2. Update collaborator")
        print("3. Delete collaborator")
        print("4. Create Contract")
        print("5. Update Contract")
        print("6. Delete Contract")
        print("7. List All Contracts")
        print("8. List All Events")
        print("9. List All Customers")
        print("0. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter a new username: ")
            password = input("Enter a new password: ")
            role = input("Enter a role (management, sales, or support): ")
            result = register_user(username, password, role)
            print(result)
        elif choice == "2":
            username = input("Enter a username: ")
            password = input("Enter a new password: ")
            result = modify_user(username, password)
            print(result)
        elif choice == "3":
            username = input("Enter a username: ")
            result = delete_user(username, password)
            print(result)            
        elif choice == "4":
            customer_id = int(input("Enter customer ID: "))
            sales_contact = input("Enter sales contact: ")
            total_amount = float(input("Enter total amount: "))
            amount_remaining = float(input("Enter amount remaining: "))
            creation_date = input("Enter creation date (YYYY-MM-DD): ")
            contract_status = input("Enter contract status: ")
            Manager().create_contract(customer_id, sales_contact, total_amount, amount_remaining, creation_date, contract_status)
        elif choice == "5":
            contract_id = int(input("Enter contract ID: "))
            new_status = input("Enter contract new status: ")
            new_amount_remaining = float(input("Enter amount remaining: "))
            Manager().update_contract(contract_id, new_status, new_amount_remaining)
        elif choice == "6":
            contract_id = int(input("Enter contract ID: "))
            Manager().delete_contract(contract_id)
        elif choice == "7":
            Manager().get_all_contracts()
        elif choice == "8":
            Manager().get_all_events()
        elif choice == "9":
            Manager().get_all_customers()      
        elif choice == "0":
            print("Exiting the CRM Application. Goodbye!")
        else:
            print("Invalid choice.")
    
    def sales_menu(self, user_role):
        print(f"Menu for {user_role}")
        print("1. Create Customer")
        print("2. Update Customer")
        print("3. List All Customers")
        print("4. Delete Customer")
        print("5. Create Contract")
        print("6. Update Contract")
        print("7. List All Contracts")
        print("8. Delete Contract")
        print("9. Create Event")
        print("10. Update Event")
        print("11. List All Events")
        print("12. Delete Event")
        print("0. Logout")

    def support_menu(self, user_role):
        print(f"Menu for {user_role}")
        print("1. Create Customer")
        print("2. Update Customer")
        print("3. List All Customers")
        print("4. Delete Customer")
        print("5. Create Contract")
        print("6. Update Contract")
        print("7. List All Contracts")
        print("8. Delete Contract")
        print("9. Create Event")
        print("10. Update Event")
        print("11. List All Events")
        print("12. Delete Event")
        print("0. Logout")

    
