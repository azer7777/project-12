class Entries:
    def get_contract_input():
        while True:
            try:
                customer_id = int(input("Enter customer ID: "))
                sales_contact = input("Enter sales contact: ")
                total_amount = float(input("Enter total amount: "))
                amount_remaining = float(input("Enter amount remaining: "))
                creation_date = input("Enter creation date (YYYY-MM-DD): ")
                contract_status = input("Enter contract status: ")
                return customer_id, sales_contact, total_amount, amount_remaining, creation_date, contract_status
            except ValueError:
                print(
                    "Invalid input. Please enter a valid number for customer ID, total amount, and amount remaining."
                )
            except Exception as e:
                print(f"An error occurred: {e}. Please try again.")

    def get_register_input():
        while True:
            try:
                username = input("Enter a new username: ")
                password = input("Enter a new password: ")
                role = input("Enter a role (management, sales, or support): ")
                if role.lower() not in ["management", "sales", "support"]:
                    raise ValueError("Invalid role. Please enter management, sales, or support.")
                return username, password, role.lower()
            except ValueError as e:
                print(e)
            except Exception as e:
                print(f"An error occurred: {e}. Please try again.")

    def get_contract_update_input():
        while True:
            try:
                contract_id = int(input("Enter contract ID: "))
                new_status = input("Enter contract new status: ")
                new_amount_remaining = float(input("Enter amount remaining: "))
                return contract_id, new_status, new_amount_remaining
            except ValueError:
                print(
                    "Invalid input. Please enter a valid integer for contract ID and a valid number for amount remaining."
                )
            except Exception as e:
                print(f"An error occurred: {e}. Please try again.")
