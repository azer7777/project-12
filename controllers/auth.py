USERS = {
    "admin": {"password": "admin_password", "role": "management"},
    "salesperson": {"password": "sales_password", "role": "sales"},
    "supportstaff": {"password": "support_password", "role": "support"}
}

def authenticate(username, password):
    user = USERS.get(username)
    if user and user["password"] == password:
        return user["role"]
    return None

def authorize(role, allowed_roles):
    return role in allowed_roles