#  Django rest framework project base

project creation that serves as the basis for developing a REST API using django.
Comenzando  :sparkles:
## requirement to run in project

 1. Python 3.9
 2. docker
 3. docker-compose

## Development environment docker
### Run commands
#### Create docker container local:
```
    make build
    make dev
    make admin
```
#### Run container docker local

    make run


### Make file commands:
```
make dev - install project dependencies and migrate to DB
make run - run the project
make qa - to run pep8, isort and lint
```
## Run in local development environment

	python manage.py makemigrations --settings=config.settings.local
    python manage.py migrate --settings=config.settings.local
    python manage.py runserver 0.0.0.0:8000 --settings=config.settings.local

## Production environment docker

### Run commands
#### Create docker image production:
	docker-compose -f production.yml build

#### Run image docker production
	docker-compose -f production.yml up -d

## PostgreSQL credentials configuration
```
fill postgres credentials in confin/settings/secrets.json
"DB_NAME": "",
"DB_USER": "",
"DB_PASSWORD": "",
"DB_HOST": "",
"DB_PORT": "",
```
