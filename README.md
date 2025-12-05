# 🏠 Household Services Platform

**Flask • SQLite • SQLAlchemy • Jinja2 • Bootstrap**

A multi-user household services management platform built using Flask.
The system supports **Admin**, **Customer**, and **Service Professional** roles with dedicated dashboards and permissions.

---

## ⭐ Features

### 🔐 Multi-Role User System

* Separate logins for:

  * **Admin**
  * **Customer**
  * **Service Professional**

### 🧑‍💼 Admin Dashboard

* Approve / reject service professionals
* Manage users and professionals
* View all service requests
* Add / update / delete service categories

### 🧑 Customer Dashboard

* Request household services
* Track request status
* View service history

### 🧑‍🔧 Service Professional Dashboard

* View tasks assigned to them
* **Accept / Reject** customer requests
* **Close completed tasks**
* View work history

### 🛠 Backend

* Flask-based modular architecture
* SQLite database with SQLAlchemy ORM
* Role-based access control
* Secure session management

### 🎨 Frontend

* Jinja2 templating engine
* Responsive UI using Bootstrap

---


---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/household-services-platform.git
cd household-services-platform
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Initialize Database

```bash
python init_db.py
```

### 4️⃣ Run the Application

```bash
python app.py
```

### 5️⃣ Open in Browser

```
http://127.0.0.1:5000
```

---

## 🔮 Future Enhancements

* Email/SMS notifications
* Online payment integration
* Real-time updates using WebSockets
* Mobile-friendly REST API

---


