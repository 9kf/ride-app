STEPS to run the project

1. install docker desktop
2. clone the project and open a terminal on the project root folder
3. run command "docker-compose up -d --build"
4. after the containers are running, run commands:
   - docker-compose exec -it app bash
   - python manage.py migrate
   - python manage.py createsuperuser
5. login with your superuser in localhost:8000/admin
6. access the endpoints
