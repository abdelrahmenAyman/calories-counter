# calories-counter

## How to run:
  1. Create virtual environment using virtualenv or any similar tool.
  2. run 'pip install -r requirements.txt'.
  3. run 'python manage.py migrate' to create database.
  4. run 'python manage.py runserver' to start server.
  5. visit localhost:8000/ to browse through API.

## API urls:
  - login: /auth/login/
  - register: /auth/register/
  - logout: /auth/register/
  - add food item: /add-food-item/
  - retrieve user info: /auth/users/[pk]/
 
