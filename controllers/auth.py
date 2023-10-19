USERS = {
    "admin": {"password": "admin_password", "role": "management"},
    "salesperson": {"password": "sales_password", "role": "sales"},
    "supportstaff": {"password": "support_password", "role": "support"}
}

def register_user(username, password, role):
    if username in USERS:
        return "Username already exists. Please choose another username."
    USERS[username] = {"password": password, "role": role}
    return "User registered successfully. You can now log in with your new account credentials."

def authenticate(username, password):
    user = USERS.get(username)
    if user and user["password"] == password:
        return user["role"]
    return None

def authorize(role, allowed_roles):
    return role in allowed_roles