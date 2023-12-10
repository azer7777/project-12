import unittest
from unittest.mock import patch, Mock
from sqlalchemy.orm import Session
from models.db import Customer, Contract, Event
from controllers.manager import Manager


class TestManager(unittest.TestCase):
    def setUp(self):
        self.manager = Manager()

    def test_create_customer_success(self):
        with patch.object(self.manager.session, "add"), patch.object(self.manager.session, "commit"):
            self.manager.create_customer(
                full_name="Customer 1",
                email="Customer_1@example.com",
                phone="123456789",
                company_name="ABC Corp",
                creation_date="2023-01-01",
                last_contact_date="2023-01-15",
                sales_contact="Sales Person",
            )
            self.manager.session.add.assert_called_once()
            self.manager.session.commit.assert_called_once()

    @patch.object(Session, "query")
    def test_get_all_customers(self, mock_query):
        expected_customers = [Customer(full_name="Customer 1")]
        mock_query.return_value.all.return_value = expected_customers

        result = self.manager.get_all_customers()

        self.assertEqual(result, expected_customers)
        mock_query.assert_called_once_with(Customer)

    def test_create_contract_success(self):
        with patch.object(self.manager.session, "query") as mock_query, patch.object(
            self.manager.session, "add"
        ), patch.object(self.manager.session, "commit"):
            mock_customer = Customer(id=1)  # Mocked customer
            mock_query.return_value.filter_by.return_value.first.return_value = mock_customer

            self.manager.create_contract(
                customer_id=1,
                sales_contact="Sales Person",
                total_amount=1000.0,
                amount_remaining=500.0,
                creation_date="2023-01-01",
                contract_status="Active",
            )

            self.manager.session.add.assert_called_once()
            self.manager.session.commit.assert_called_once()

    def test_create_contract_customer_not_found(self):
        with patch.object(self.manager.session, "query") as mock_query:
            mock_query.return_value.filter_by.return_value.first.return_value = None

            with patch("builtins.print") as mock_print:
                self.manager.create_contract(
                    customer_id=1,
                    sales_contact="Sales Person",
                    total_amount=1000.0,
                    amount_remaining=500.0,
                    creation_date="2023-01-01",
                    contract_status="Active",
                )

                mock_print.assert_called_once_with("Customer with ID 1 not found. Operation aborted.")

    @patch.object(Session, "query")
    def test_get_all_contracts(self, mock_query):
        expected_contracts = [Contract(id=1)]
        mock_query.return_value.all.return_value = expected_contracts

        result = self.manager.get_all_contracts()

        self.assertEqual(result, expected_contracts)
        mock_query.assert_called_once_with(Contract)

    def test_create_event_success(self):
        # Create a mock contract for successful scenario
        mock_contract = Mock()
        mock_contract.id = 1
        mock_contract.customer_id = 1
        mock_contract.contract_status = "signed"

        # Mock the session.query method
        with patch.object(self.manager.session, "query") as mock_query:
            mock_query.return_value.filter_by.return_value.first.return_value = mock_contract

            # Mock the session.add method
            with patch.object(self.manager.session, "add") as mock_add:
                with patch.object(self.manager.session, "commit"):
                    self.manager.create_event(
                        event_name="Event 1",
                        contract_id=1,
                        client_name="Client 1",
                        client_contact="Contact 1",
                        event_start_date="2023-01-01",
                        event_end_date="2023-01-02",
                        support_contact="Support Person",
                        location="Location 1",
                        attendees=10,
                        notes="Notes for Event 1",
                        user_full_name="Sales Person",
                    )

                    # Ensure that the add method is called once
                    mock_add.assert_called_once()

    @patch.object(Session, "query")
    def test_get_all_events(self, mock_query):
        expected_events = [Event(id=1), Event(id=2)]
        mock_query.return_value.all.return_value = expected_events

        result = self.manager.get_all_events()

        self.assertEqual(result, expected_events)
        mock_query.assert_called_once_with(Event)
