# BlogApp
This project is being just to save my learning in DRF environment

Setup Instructions :
(1) Navigate into the choice of your directory and clone the project.

(2) After Cloning, make a virtual Environment for the project using :
    
    python3 -m venv env
    
    # After Creation of virutal environment activate it.
    source env/bin/activate
    # Or you can directly add virtual as the python Interpretor in PyCharm.
    
(3) After this add django and djangorestframework using :
  
    pip3 install django
    pip3 install djangorestframework

(4) After installing django and djangorestframework, move into th project directory in this case :
    
    cd blog_project
    # Run Migrations
    python3 manage.py makemigrations blog_app
    python3 manange.py migrate
(5) Finally, create a superuser using :

    python3 manage.py createsuperuser
(6) After creation of superuser, run :

    python3 manage.py runserver

Thank You!
    
