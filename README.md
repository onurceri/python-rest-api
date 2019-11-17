# python-rest-api  
  
![alt text](https://github.com/onurceri/python-rest-api/blob/master/tests.png?raw=true)

Codes that must be run before the "dockore-compose up" command:  
docker-compose run app sh -c "python manage.py makemigrations"  
docker-compose run app sh -c "python manage.py migrate"  

Create superuser:  
docker-compose run app sh -c "python manage.py createsuperuser"  

Run tests and flake8:  
docker-compose run app sh -c "python manage.py test && flake8"  

Postman Collection Link : https://www.getpostman.com/collections/ce537cae53214a1bf59c
