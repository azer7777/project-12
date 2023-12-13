import pytest
from unittest.mock import MagicMock, patch
from controllers.auth import register_user, update_user, delete_user, authenticate, authorize


@pytest.fixture
def db_session():
    # Use a MagicMock for the database session
    return MagicMock()


def test_register_user(db_session):
    with patch("controllers.auth.session", db_session):
        result = register_user("Test User", "test_user", "password123", "management")
        assert "Username already exists" in result


def test_update_user(db_session):
    with patch("controllers.auth.session", db_session):
        # update the user
        result = update_user("test_user", "Test User Jr.", "new_password")
        assert "User updated successfully" in result


def test_delete_user(db_session):
    with patch("controllers.auth.session", db_session):
        # delete the user
        result = delete_user("test_user")
        assert "User deleted successfully" in result


def test_authenticate(db_session):
    # Create a MagicMock for the User object
    user_mock = MagicMock(full_name="Test User", role="management")
    # Set the password to a hashed value (replace this with the actual hash)
    user_mock.password = b'$2b$12$the_actual_hash_here'
    db_session.query().filter_by().first.return_value = user_mock

    with patch("controllers.auth.session", db_session):
        # Mock bcrypt.checkpw to always return True
        with patch("controllers.auth.bcrypt.checkpw", return_value=True):
            # authenticate the user
            full_name, role = authenticate("test_user", "password123")
            assert full_name == "Test User"
            assert role == "management"


def test_authorize(db_session):
    with patch("controllers.auth.session", db_session):
        # authorize the user
        result = authorize("management", ["management", "sales"])
        assert result is True
