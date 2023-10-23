from sqlalchemy.orm import sessionmaker
from models.db import engine, User


Session = sessionmaker(bind=engine)
session = Session()

def register_user(full_name, username, password, role):
    existing_user = session.query(User).filter_by(username=username).first()
    if existing_user:
        return "Username already exists. Please choose another username."
    new_user = User(full_name=full_name, username=username, password=password, role=role)
    session.add(new_user)
    session.commit()
    return "User registered successfully. User can now log in with the new account credentials."


def update_user(new_full_name, username, new_password):
    user = session.query(User).filter_by(username=username).first()
    if user:
        user.password = new_password
        user.full_name = new_full_name
        session.commit()
        return "User updated successfully."
    return "User not found."


def delete_user(username):
    user = session.query(User).filter_by(username=username).first()
    if user:
        session.delete(user)
        session.commit()
        return "User deleted successfully."
    else:
        return "User not found."



def authenticate(username, password):
    user = session.query(User).filter_by(username=username, password=password).first()
    if user:
        return user.role
    return None



def authorize(role, allowed_roles):
    return role in allowed_roles