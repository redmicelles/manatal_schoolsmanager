# manatal_schoolsmanager

## TASK
## Step 1

The first step focuses on Django setup and models.

1. Create a Django app, with:
    - Use **Postgres** as a database
    - Use **Pipenv** as a Python dependency manager.
    - Environment file (for sensitive information, etc.)
2. Add models to create the following structure:
    - Students have a first name, the last name, and a student identification string (20 characters max for each)
    - Schools have a name (20 char max) and a maximum number of students (any positive integer)
    - Each student object must belong to a school object

## Step 2

This second step focuses on Django Rest Framework (DRF).

Feel free to cover edge cases. (Add a reference to it in your [README.md](http://readme.md/))
We encourage you to use `ModelViewSet` and `ModelSerializer` classes to automatically handle the different API HTTP methods.

1. Add **Django REST framework** library to your project by using Pipenv
2. Enable and use the DRF browsable API for testing things manually.
3. Design your API according to the specifications below (make sure to test and customize your solution) by creating URLs, views, serializers, tests for all your models so that:
    - Endpoint `students/` will return all students (GET) and allow student creation (POST)
    - Endpoint `/schools/` will return all schools (GET) and allow school creation (POST)
    - Endpoint `/schools/:id` and `/students/:id` will return the object by :id (GET) and allow editing (PUT/PATCH) or deleting (DELETE)
    - Student creation will generate a unique identification string (like random hexadecimal or uuid4 or anything of your choice)
    - Trying to add a student in a full school (maximum number of students reached) will return a DRF error message

### References:

- ModelViewSet: [https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset](https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset)
- ModelSerializer: [https://www.django-rest-framework.org/api-guide/serializers/#modelserializer](https://www.django-rest-framework.org/api-guide/serializers/#modelserializer)

## Step 3

This third step focuses on **Django Nested Routers**.

1. Add Django Nested Routers library to your project by using Pipenv
2. Design your API according to the specifications below:
    - Endpoint /schools/:id/students will return students who belong to school :id (GET)
    - Endpoint /schools/:id/students will allow student creation in the school :id (POST)
    - Your nested endpoint will allow GET/PUT/PATCH/DELETE methods on /schools/:id/students/:id
    - Your nested endpoint will respect the same two last rules of Step 2 too

### References:

- drf-nested-routers: [https://github.com/alanjds/drf-nested-routers](https://github.com/alanjds/drf-nested-routers)

# DETAILS
1. All python dependencies for this project can be found in the dependencies directory.
2. Test has write for all models using pytest.
3. The env_file directory contains the enviroments file that hold the environment variables for PostgreSQL and Django.
4. The same endpoints as described in the task above have be preserved for the api.
5. PostgreSQL 12 and above is recommended for this project.

# Deployed Instance
An instance of the deployed is available at:
http://ec2-34-219-90-153.us-west-2.compute.amazonaws.com/schools

http://ec2-34-219-90-153.us-west-2.compute.amazonaws.com/students

all nested endpoints as described in the task are available also in the live deployment.


