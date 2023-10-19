from controllers.manager import Manager
from controllers.auth import authenticate, authorize, register_user

class Menu:
    def __init__(self):
        self.manager = Manager()

    def auth_menu(self):
        print("Welcome to the CRM Application!")
        while True:
            print("1. Log in")
            print("2. Register")
            print("0. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                role = authenticate(username, password)

                if role:
                    print(f"Authentication successful. You are logged in as {role}.")
                    self.display_menu(role)
                else:
                    print("Authentication failed. Invalid username or password.")
            elif choice == "2":
                username = input("Enter a new username: ")
                password = input("Enter a new password: ")
                role = input("Enter a role (management, sales, or support): ")
                result = register_user(username, password, role)
                print(result)
            elif choice == "0":
                print("Exiting the CRM Application. Goodbye!")
                break
            else:
                print("Invalid choice.")

    def display_menu(self, user_role):
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
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            if authorize(user_role, ["management", "sales"]):
                pass
            else:
                print("Permission denied.")
        elif choice == "2":
            if authorize(user_role, ["management", "sales"]):
                pass
            else:
                print("Permission denied.")
        elif choice == "3":
            pass
        elif choice == "4":
            if authorize(user_role, ["management"]):
                pass
            else:
                print("Permission denied.")
        elif choice == "5":
            if authorize(user_role, ["management", "sales"]):
                pass
            else:
                print("Permission denied.")
        elif choice == "6":
            pass
        elif choice == "0":
            print("Exiting the CRM Application. Goodbye!")
        else:
            print("Invalid choice.")


    
