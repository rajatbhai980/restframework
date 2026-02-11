DOCKER IS REQUIRED!

build docker image for the django app first 
- docker build -t djangorest . 

run the muilti container yaml file 
- docker compose -f run.yaml up -d 

enter the docker image terminal 
- docker exec -it restframework-django-rest-1 bash 

run the server 
- python manage.py runserver 0.0.0.0:8000