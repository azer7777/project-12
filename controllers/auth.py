from sqlalchemy.orm import sessionmaker
from models.db import engine, User


Session = sessionmaker(bind=engine)
session = Session()

def register_user(username, password, role):
    existing_user = session.query(User).filter_by(username=username).first()
    if existing_user:
        return "Username already exists. Please choose another username."
    new_user = User(username=username, password=password, role=role)
    session.add(new_user)
    session.commit()
    return "User registered successfully. User can now log in with the new account credentials."


def modify_user(username, new_password):
    user = session.query(User).filter_by(username=username).first()
    if user:
        user.password = new_password
        session.commit()
        return "Password updated successfully."
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