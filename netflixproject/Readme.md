# Django Netflix Clone
This is a clone of the popular video streaming site Netflix. Built using Django

## Requirements
The user can perform the following functions:

- A user can sigup for an account
- A user can login and logout
- A user can view the different movies and Tv shows that are available.
- A user can view a description Of the movie and its current rating.
- A user can create a profile for a kid or an old person
- A user can watch any episode or movie thar are avaliable.


## Installation
The application requires the following installations to operate:
- pip
- django-allauth
- django


## Technologies Used
- python 3.11.4
- django 4.2.2

## SUMMARY OVERFLOW
***
The following is a basic workflow that you can use as a quick reference for developing a Django Project.

### Setup
- Within a new directory, create and activate a virtualenv.
- Install Django.
- Create your project:
```django-admin.py startproject```
- Create a new app: ```python manage.py startapp```
- Add your app to the INSTALLED_APPS tuple.

#### Add Basic URLs and Views
- Map your Project’s urls.py file to the new app.
- In your App directory, create a urls.py file to define your App’s URLs.
- Add views, associated with the URLs, in your App’s views.py; make sure they return a HttpResponse object. Depending on the situation, you may also need to query the model (database) to get the required data back requested by the end user.

### Templates and Static Files
- Create a templates and static directory within your project root.
- Update settings.py to include the paths to your templates.
- Add a template (HTML file) to the templates directory. Within that file, you can include the static file with - ```{% load static %}```
- Update the views.py file as necessary.

### Models and Databases
- Update the database engine to settings.py (if necessary, as it defaults to SQLite).
- Create and apply a new migration.
- Create a super user.
- Add an admin.py file in each App that you want access to in the Admin.
- Create your models for each App.
- Create and apply a new migration. (Do this whenever you make any change to a model).

### Forms
- Create a forms.py file at the App to define form-related classes; define your ModelForm classes here.
- Add or update a view for handling the form logic - e.g., displaying the form, saving the form data, alerting the user about validation errors, etc.
- Add or update a template to display the form.
- Add a urlpattern in the App’s urls.py file for the new view.

### User Registration

- Create a UserForm
- Add a view for creating a new user.
- Add a template to display the form.
- Add a urlpattern for the new view.

### User Login
- Add a view for handling user credentials.
- Create a template to display a login form.
- Add a urlpattern for the new view.

### Setup the template structure
-  Find the common parts of each page (i.e., header, sidebar, footer).
-  Add these parts to a base template
-  Create specific. templates that inherent from the base template.


## How to run this application

### Steps

To run this application on your laptop, run this command from your terminal:

`python manage.py runserver`


Copy paste the URL link to your web browser

`Starting development server at http://127.0.0.1:8000/`

## How to run the admin interface

While the application is running on your local computer, go tho this url: http://127.0.0.1:8000/admin/
username : allanto
password : allanto


Created By: Aryatwijuka  Allan
Gmail: allankleinz22@gmail.com
