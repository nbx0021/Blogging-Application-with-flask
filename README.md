# Blogging-Application-with-flask
# Blogging Application

This is a simple Flask-based blogging application that allows users to create, view, and manage their blog posts. It uses SQLAlchemy for database management and integrates WTForms for form handling.

## Table of Contents

- [Description]
- [Getting Started]
  - [Prerequisites]
  - [Installation]
- [Usage]
- [Contributing]
- [License]

## Description

This Flask application provides a platform for users to create and manage their blog posts. It includes the following features:

- User registration and login.
- Dashboard to view and update user information.
- Ability to create and edit blog posts.

## Getting Started

### Prerequisites

Before you can run this application, make sure you have the following installed:

- Python
- Flask
- Flask-SQLAlchemy,mysql
- WTForms

### Installation

1. Clone the repository to your local machine:

   ```bash
   $ git clone https://github.com/yourusername/yourproject.git
   ```

2. Navigate to the project directory:

   ```bash
   $ cd yourproject
   ```

3. Install the required dependencies using pip:

   ```bash
   $ pip install -r requirements.txt
   ```

4. Configure the database connection by updating the `app.config['SQLALCHEMY_DATABASE_URI']` in `app.py` to your MySQL database URI.

5. Create the database tables by running the following commands:

   ```bash
   $ flask db init
   $ flask db migrate
   $ flask db upgrade
   ```

6. Start the Flask development server:

   ```bash
   $ flask run
   ```

The application should now be running locally. Access it by opening your web browser and navigating to [http://localhost:5000/](http://localhost:5000/).

## Usage

- **Registration:** Users can register with their information, including first name, last name, mobile number, email address, date of birth, city, country, and password.

- **Login:** Registered users can log in using their email address and password.

- **Dashboard:** After logging in, users can view and update their profile information.

- **Main Page:** Users can access the main page, which displays all registered users.

- **Create Blog Post:** Users can create and edit blog posts from their dashboard.

- **About Us:** An about us page with information about the application.

## Contributing

Contributions to this project are welcome! If you'd like to contribute, please follow these guidelines:

1. Fork the project and create a new branch.
2. Make your changes and test them thoroughly.
3. Ensure your code follows the project's coding standards.
4. Create a pull request with a clear description of your changes.
