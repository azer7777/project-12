# project-12

# CRM App

CRM App is a customer relationship management system designed to help businesses manage their interactions with current and future customers. It provides a centralized platform for managing customer data, contracts, and events.

## Features

User Authentication: Secure user authentication system with role-based access control.
Customer Management: Add and update customer information including full name, email, phone, and company name.
Contract Management: Create and manage contracts associated with customers. Track contract status, total amount, and remaining amount.
Event Management: Organize events related to contracts. Track event name, start/end date, client information, support contact, location, attendees, and notes.

## Technologies Used

Python: Backend logic and database management.

SQLAlchemy: Object-Relational Mapping (ORM) for working with databases.

SQLite: Lightweight and easy-to-set-up database.

Sentry: Error monitoring and reporting tool.

## Installation

1. Clone the repository:
````
git clone https://github.com/azer7777/Project-12.git
````
2. Create a virtual environment and activate it:
````
python -m venv venv 
source venv/bin/activate  # On Windows: venv\Scripts\activate
````
3. Install dependencies:
````
pip install -r requirements.txt
````
4. Run the Application:
````
python main.py
````
## Tests and reports

1. Running Tests with pytest:
````
pytest
````
To generate an HTML report:
````
pytest --html=pytest_report.html
````
2. Generating Code Coverage Report:
````
coverage run -m pytest
````
Generate the coverage report:
````
coverage html
````
Access the HTML coverage report in the htmlcov directory.

## Usage
````
username : user1
password: user
````
Access the application through the command line interface using the credentials provided.
Use the menu options to manage users, customers, contracts, and events.
Ensure proper authentication for accessing sensitive features.
