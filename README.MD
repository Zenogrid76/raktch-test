# Raktch Technology & Software - Backend Developer Test Project

## 📋 Overview

This is a comprehensive backend development test project for **Raktch Technology & Software**. The application demonstrates modern web development practices using Django REST framework with JWT authentication, PostgreSQL database integration, and a clean, intuitive user interface.

### 🎯 Purpose
The project showcases proficiency in:
- **Backend Development** with Django
- **Database Management** with PostgreSQL
- **Authentication Systems** using JWT tokens
- **RESTful API Design** principles
- **Frontend Integration** with HTML templates

## ✨ Key Features

### 🔐 Authentication & Security
- **JWT-based Authentication** for secure API access
- User registration and login system
- Token-based session management
- Password validation and security enforcement

### 👥 Employee Management
- **Complete CRUD Operations** for employee records
- Employee profile management with detailed information
- Department assignment and tracking
- Achievement assignment system

### 🏢 Department Management
- Create and manage organizational departments
- Assign employees to specific departments
- Department-based employee filtering and organization

### 🏆 Achievement System
- Create and manage employee achievements
- **Multiple achievements per employee** support
- Track employee accomplishments and milestones

### 🎨 User Interface
- Clean, responsive dashboard interface
- Intuitive navigation and user experience
- Error handling with user-friendly messages
- Mobile-responsive design


## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- PostgreSQL 12 or higher
- Git

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Zenogrid76/raktch-test.git
   cd raktch-test
   ```

2. **Set Up Virtual Environment**
   ```bash
   # Create virtual environment
   python -m venv env
   
   # Activate virtual environment
   # On Windows:
   .\env\Scripts\Activate
   
   # On macOS/Linux:
   source env/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Configuration**
   
   Create a PostgreSQL database using pgAdmin or command line:
   ```sql
   CREATE DATABASE your_database_name;
   ```
   
   Create a `.env` file in the project root directory:
   ```env
   DB_NAME=your_database_name
   DB_USER=your_username
   DB_PASSWORD=your_password
   DB_HOST=localhost
   DB_PORT=5432
   ```

5. **Database Migration**
   ```bash
   python manage.py migrate
   ```


6. **Start Development Server**
   ```bash
   python manage.py runserver
   ```

7. **Access the Application**
   
   Follow the Link or Open your browser and navigate to: `http://127.0.0.1:8000/`

## 📖 Usage Guide

### Getting Started

1. **Registration**
   - Click the **"Register"** button on the homepage
   - Create an account with a secure password
   - Password must include numbers, uppercase, and lowercase letters

2. **Login**
   - Use your registered credentials to log in
   - JWT token will be automatically managed for your session

3. **Dashboard Navigation**
   - Access the main dashboard after successful login
   - Navigate between different sections using the menu

### Managing Departments

1. Navigate to the **Departments** section
2. Click **"Add Department"** to create new departments
3. Provide department name and description
4. Save to add the department to the system

### Managing Employees

1. **Prerequisites**: Ensure at least one department exists
2. Navigate to the **Employees** section
3. Click **"Add Employee"** to create new employee records
4. Fill in employee details:
   - Personal information (name, email, phone)
   - Department assignment
   - Employment details
5. Save to add the employee to the system

### Managing Achievements

1. Navigate to the **Achievements** section
2. Click **"Add Achievement"** to create new achievements
3. Provide achievement name and description
4. Save to add the achievement to the system

### Editing and Deleting Records

- **Edit**: Click the edit icon next to any record to modify details
- **Delete**: Click the delete icon to remove records (with confirmation)


## 🔧 Configuration

### Environment Variables

Create a `.env` file with the following variables:

```env
# Database Configuration
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432

# Django Configuration (Optional)
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```


## 🐛 Troubleshooting

### Common Issues

1. **Database Connection Error**
   - Verify PostgreSQL is running
   - Check database credentials in `.env` file
   - Ensure database exists

2. **Migration Issues**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Static Files Not Loading**
   ```bash
   python manage.py collectstatic
   ```

4. **Port Already in Use**
   ```bash
   python manage.py runserver 8001
   ```


## 📄 License

This project is created for evaluation purposes for Raktch Technology & Software.

**Note**: This project demonstrates backend development capabilities and is intended for evaluation purposes by Raktch Technology & Software.