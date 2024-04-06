# Photoshare

This project is implemented by following the tutorial uploaded by <a href="https://www.youtube.com/@DennisIvy">Dennis Ivy</a>. The tutorial can be found <a href="https://www.youtube.com/watch?v=sSquD2u5Ie0">here.</a>
The goal was to learn how to handle images in `django` and cofigure `static` files for a django project.

# Functionality of the Project

The following functionality are provided by the project.

- Upload image
- View image by category
- User Registration
- User Login

## Structure of Project

The project is structured as follows:

- `photoshare/` -> contains the core configurations of the project
- `photos/` -> contains the CRUD functionality of the application

## Run the project

Follow the following steps to run the project successfully:

### 1. Create a virtual environment:

`python -m venv env`

### 2. Activate the virtual envrironment:

> On Windows: venv\scripts\activate

> on Linux/Max: source venv/Scripts/activate

### 3. Install Necessary packages

`pip install -r requirements.txt`

### 4. Run migrations

`python manage.py migrate`

### 5. Run project

`python manage.py runserver`
