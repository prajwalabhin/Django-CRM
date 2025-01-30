# Django Customer Relationship Management (CRM)

## Overview
This is a **Django and MySQL-based Customer Relationship Management (CRM)** that allows users to register, log in, and manage customer data efficiently. This provides features for **adding, updating, and deleting customer records**, ensuring secure access and user management.

## Features
- **User Authentication**: Secure registration and login system using Django's built-in authentication.
- **Customer Management**: Add, update, and delete customer records with ease.
- **Admin Dashboard**: Manage users and customer data through Django's admin panel.
- **Database Integration**: Uses MySQL for efficient and scalable data storage.

## Tech Stack
- **Backend**: Django (Python)
- **Database**: MySQL
- **Frontend**: HTML, CSS, Bootstrap (within Django templates)

## Project Structure
```
dcrm/                # Root directory
│── dcrm/            # Project folder (contains settings, urls, wsgi, asgi, etc.)
│── website/         # Django app folder (handles CRM functionalities)
│   │── templates/   # HTML files for frontend
│   │── static/      # Static files (CSS, JS, images) (to be created manually)
│   │── views.py     # Handles user requests
│   │── models.py    # Defines database models
│   │── urls.py      # Routes URLs to views
│── manage.py        # Django project management script
│── requirements.txt # Dependencies for the project
│── vercel.json      # Configuration for deployment
```

## Installation and Setup
1. **Clone the Repository**
   ```sh
   git clone https://github.com/prajwalabhin/Django-CRM
   cd dcrm
   ```

2. **Set up a Virtual Environment**
   ```sh
   python -m venv virt
   source virt/bin/activate  # On Windows: virt\Scripts\activate
   ```

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configure MySQL Database**
   - Update `DATABASES` settings in `settings.py` with your MySQL credentials.

5. **Run Migrations**
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a Superuser for Admin Access**
   ```sh
   python manage.py createsuperuser
   ```
   - Enter a username, email, and password.

7. **Run the Development Server**
   ```sh
   python manage.py runserver
   ```
   - Open `http://127.0.0.1:8000/` in your browser.

## Usage
- **Admin Panel**: Access via `/admin` to manage users and customer data.
- **User Registration**: New users can register via the registration form.
- **Login & Logout**: Users can securely log in and manage their data.
  
 ##

 ![Image](https://github.com/user-attachments/assets/7ae31668-da15-4d65-86fb-af0adda5f039)
![Image](https://github.com/user-attachments/assets/a7fedd02-dbb0-4be1-af4a-f6632f271639)
![Image](https://github.com/user-attachments/assets/6b9c64ef-9944-4c2a-825e-03822d1bfa62)
![Image](https://github.com/user-attachments/assets/a45fc707-2b07-4f45-87e4-2c0b069e2753)
![Image](https://github.com/user-attachments/assets/6d5f18b0-41a0-4256-b380-4151cd9318e5)
![Image](https://github.com/user-attachments/assets/80050de9-407e-48ee-b7eb-976d605d29e1)
  
  
