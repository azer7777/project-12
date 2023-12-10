from sqlalchemy.orm import sessionmaker
from models.db import engine, User

Session = sessionmaker(bind=engine)
session = Session()


def register_user(full_name, username, password, role):
    """
    Registers a new user in the system.

    Args:
        full_name (str): The full name of the user.
        username (str): The username for authentication.
        password (str): The password for authentication.
        role (str): The role assigned to the user.

    Returns:
        str: A message indicating the result of the registration process.
    """
    existing_user = session.query(User).filter_by(username=username).first()
    if existing_user:
        return "Username already exists. Please choose another username."
    new_user = User(full_name=full_name, username=username, password=password, role=role)
    session.add(new_user)
    session.commit()
    return "User registered successfully. The new user can now log in with the credentials."


def update_user(username, new_full_name, new_password):
    """
    Updates the information of an existing user.

    Args:
        username (str): The username of the user to be updated.
        new_full_name (str): The new full name for the user.
        new_password (str): The new password for the user.

    Returns:
        str: A message indicating the result of the update operation.
    """
    user = session.query(User).filter_by(username=username).first()
    if user:
        user.full_name = new_full_name
        user.password = new_password
        session.commit()
        return "User updated successfully."
    return "User not found."


def delete_user(username):
    """
    Deletes an existing user from the system.

    Args:
        username (str): The username of the user to be deleted.

    Returns:
        str: A message indicating the result of the delete operation.
    """
    user = session.query(User).filter_by(username=username).first()
    if user:
        session.delete(user)
        session.commit()
        return "User deleted successfully."
    else:
        return "User not found. Delete operation aborted."


def authenticate(username, password):
    """
    Authenticates a user based on the provided username and password.

    Args:
        username (str): The username for authentication.
        password (str): The password for authentication.

    Returns:
        Tuple[str, str]: A tuple containing the full name and role of the authenticated user.
    """
    user = session.query(User).filter_by(username=username, password=password).first()
    if user:
        return user.full_name, user.role
    return None, None


def authorize(role, allowed_roles):
    """
    Authorizes a user based on their role.

    Args:
        role (str): The role of the user.
        allowed_roles (List[str]): A list of roles that are allowed.

    Returns:
        bool: True if the user's role is in the list of allowed roles, False otherwise.
    """
    return role in allowed_roles
