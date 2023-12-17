# TODO App API Documentation

Welcome to the TodoApp API! This documentation provides details on the available endpoints and how to interact with them.

## Requirements

All the installed packages and their versions are listed in the `requirements.txt` file, which serves as a record of the project dependencies.

### Dependencies:

- Django==5.0
- djangorestframework==3.14.0
- mysqlclient==2.2.1
- pytest==7.4.3

## Getting Started

Follow these steps to get the project up and running on your local machine.

1. Clone the Repository:

    ```bash
      git clone https://github.com/naveenvaz/todoapp.git 
    ```

2. Navigate to the root directory of your Django project using the terminal or command prompt.

    ```bash
    cd /path/to/your/project
    ```

3. Activate the virtual environment:

    - On Windows: `venv\Scripts\activate`
    - On macOS/Linux: `source venv/bin/activate`

4. Install the dependencies from the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

5. Apply migrations:

    ```bash
    python manage.py migrate
    ```

6. Run the server:

    ```bash
    python manage.py runserver
    ```

## Email Configuration

We used Mailtrap Email Delivery Platform to send email to Test. All settings related to Mailtrap are mentioned in the `settings.py` file. Create an account with Mailtrap, select Django in the dropdown, and apply these settings in `settings.py`.

## Table of Contents

1. [Welcome Message](#1-welcome-message)
2. [Register User](#2-register-user)
3. [User Login](#3-user-login)
4. [User Logout](#4-user-logout)
5. [Create Todo Task](#5-create-todo-task)
6. [Update Todo Task](#6-update-todo-task)
7. [Delete Todo Task](#7-delete-todo-task)
8. [Email Reminder Feature](#8-email-reminder-feature)
9. [Running Test Cases](#9-running-test-cases)

### 1) Welcome Message

Upon accessing the local host, a message is returned, welcoming you to TodoApp!

- **API EndPoint:** http://127.0.0.1:8000/
- **Method:** GET

### 2) Register User

We are registering a new user through the API endpoint http://localhost:8000/api/register/ using the POST method. The user details, including the username, password, and email, are provided in the request body. Upon successful registration, the API responds with the created user's username and email, and the status is set to 201 Created.

- **API EndPoint:** http://localhost:8000/api/register/
- **Method:** POST

### 3) User Login

We are performing a user login through the API endpoint http://localhost:8000/api/login/ using the POST method. The user credentials (username and password) are provided in the request body. Upon successful login, the API responds with an authentication token, such as "0e8d90fdd7e8520385a96f0a95f06c3c6254bab9."

- **API EndPoint:** http://localhost:8000/api/login/
- **Method:** POST

### 4) User Logout

We are performing a user logout through the API endpoint http://localhost:8000/api/logout/ using the POST method. The request includes the necessary headers, such as Content-Type and Authorization with the user's authentication token (e.g., Token 0e8d90fdd7e8520385a96f0a95f06c3c6254bab9). Upon successful logout, the API responds with the message "Successfully logged out."

- **API EndPoint:** http://localhost:8000/api/logout/
- **Method:** POST

### 5) Create Todo Task

We are creating a new todo task using the API endpoint http://localhost:8000/api/tasks/create/ with the POST method. The request includes the necessary headers, such as Content-Type and Authorization with the user's authentication token (e.g., Token 0e8d90fdd7e8520385a96f0a95f06c3c6254bab9). The request body contains details of the new task, including the name, description, and deadline. Upon successful creation, the API responds with a status code of 201 Created and provides information about the newly created task, including its unique identifier (id), creation and modification timestamps, task details, and the associated user.

- **API EndPoint:** http://localhost:8000/api/tasks/create/
- **Method:** POST

### 6) Update Todo Task

We are updating an existing todo task using the API endpoint http://localhost:8000/api/tasks/update/1/ with the PUT method. The request includes the necessary headers, such as Content-Type and Authorization with the user's authentication token (e.g., Token b6f2d977e36429d4594a93fa58bffc7eb037164c). The request body contains updated details of the task, including the new name, description, and deadline. Upon successful update, the API responds with a status code of 200 OK and provides information about the modified task, including its unique identifier (id), creation and modification timestamps, updated task details, and the associated user.

- **API EndPoint:** http://localhost:8000/api/tasks/update/id/
- **Method:** PUT

### 7) Delete Todo Task

This API allows you to delete a todo task with id , and upon successful deletion, it returns a message indicating that the todo task was deleted successfully.

- **API EndPoint:** http://localhost:8000/api/tasks/delete/id/
- **Method:** DELETE

### 8) Email Reminder Feature

This Django management command sends email reminders for tasks with deadlines within the next hour, notifying users of the impending task deadline.

#### Explanation:

- The script fetches tasks from the TodoTask model where the deadline is in the future.
- For each task, it calculates the time remaining until the deadline.
- If the time remaining is less than or equal to one hour (3600 seconds), it sends an email reminder to the task owner using a template ('todoapp/reminder_email.html').
- The email subject is customized to include the task name as a reminder.
- After processing all tasks, a success message is displayed in the console.

- **Command to run:** `python manage.py send_task_reminder`

### 9) Running Test Cases

To run all test cases, including those in `test_views` and `test_serializers`, execute the following command:

```bash
pytest
