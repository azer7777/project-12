from controllers.auth import authenticate

class Menu():
    def auth_menu(self):
        print("Welcome to the CRM Application!")
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        role = authenticate(username, password)

        if role:
            print(f"Authentication successful. You are logged in as {role}.")
            self.main_menu(role)
        else:
            print("Authentication failed. Invalid username or password.")

    def main_menu(self, user_role):
        print(f"Menu for {user_role}")
        if user_role == "management":
            pass
        elif user_role == "sales":
            pass
        elif user_role == "support":
            pass
        else:
            print("Invalid user role.")
    
