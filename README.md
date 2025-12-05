# Household-Services-Platform
Household Services Platform
Flask • SQLite • SQLAlchemy • Jinja2 • Bootstrap

A multi-user household services management platform built with Flask.
The system supports Admin, Customer, and Service Professional roles, each with their own dashboards and permissions.

🚀 Features
🔐 Multi-Role Authentication

Separate login system for:

Admin

Customer

Service Professional

👤 Admin Panel

Approve or reject new service professionals

Manage users and professionals

View all service requests

Full CRUD operations for service categories

🧑‍🔧 Service Professional Dashboard

View service requests assigned to them

Accept / Reject pending service tasks

Mark tasks as completed

View work history and status updates

🧑 Customer Panel

Browse and request household services

Track request status (Pending / Accepted / Rejected / Completed)

View history of previous service requests

🛠️ Backend Architecture

Flask-based MVC structure

SQLite + SQLAlchemy ORM

Role-based access control

Secure session handling

🎨 Frontend

Dynamic UI using Jinja2 templating

Responsive pages built with Bootstrap


🏃‍♂️ How to Run

Clone the repo:

git clone https://github.com/yourusername/household-services-platform.git
cd household-services-platform


Install dependencies:

pip install -r requirements.txt


Initialize the database:

python init_db.py


Start the server:

python app.py


Open in browser:
http://127.0.0.1:5000


📝 Future Enhancements

JWT-based API for mobile apps

Payment integration

Email notifications

Real-time updates using WebSockets
