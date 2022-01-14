## Step 1
1. Create DockerFile.
- Create Django project 
- Create Django App
- Update django settings 
- Create custom Python image using the Official Python3.8 Image
- Create working directory and make it thw present working directory
- Copy Django project to container
- Install project dependencies inside the container
- Create docker compose file that create four services (nginx, django, postgres, and swagger api documentation)

2. Create Models (School and Student)
- School : firstname(max_char = 20), lastname(max_char = 20), identification(max_char=20)
- student: school(foreign_key), name(max_char = 20), max_number_students(int)

## Step2
using modelviewset and modelserializers create the following endpoints
- Endpoint `students/` will return all students (GET) and allow student creation (POST)
- Endpoint `/schools/` will return all schools (GET) and allow school creation (POST)
- Endpoint `/schools/:id` and `/students/:id` will return the object by :id (GET) and allow editing (PUT/PATCH) or deleting (DELETE)
- Student creation will generate a unique identification string (like random hexadecimal or uuid4 or anything of your choice)
- Trying to add a student in a full school (maximum number of student reached) will return a DRF error message

## Step3
1. Add Django Nested Routers library to your project by using Pipenv
2. Design your API according to specifications below:
    - Endpoint /schools/:id/students will return students who belong to school :id (GET)
    - Endpoint /schools/:id/students will allow student creation in the school :id (POST)
    - Your nested endpoint will allow GET/PUT/PATCH/DELETE methods on /schools/:id/students/:id
    - Your nested endpoint will respect the same two last rules of Step 2 too
