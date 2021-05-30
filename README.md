# Globant Coding assessment
This is Git repo for the Globant code assessment

1.  Create virtual env by running the following  
        python -m venv < virtual environment name >  
2.  Activate your virtual environment.
        run < virtual environment name >/Scripts/activate.bat
3. This should add < virtual environment name > to your prompt.
4.  Create local copy of the project.
    Note: Code is in main branch.
5.  Run pip install -r requirements.txt
6.  Goto Django project folder where manage.py is situated.
7.  Run the following commands
    * set environment variable for API_KEY=< API Key >
    * python manage.py makemigrations
    * python manage.py migrate
    * python manage.py createcachetable
    * python manage.py runserver
