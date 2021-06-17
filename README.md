
#  Django rest framework project base  :sparkles:  
  
Project creation that serves as the basis for developing a REST API using Django.  

## Requirement to run in project  
  
 1. Python 3.9  
 2. docker  
 3. docker-compose  
 
 

## Environment variable setting
:card_file_box: **Create in the main directory the following directories and files** 
```
.envs -> path
├── .local -> path
│   ├── .django ->file
│   └── .postgres -> file
└── .production -> path
    ├── .django -> file
    └── .postgres -> file
```
:wrench:**Add variables to .django file**

    # General  
    # ------------------------------------------------------------------------------  
    # DJANGO_READ_DOT_ENV_FILE=True  
    DJANGO_SETTINGS_MODULE=config.settings.local  
    DJANGO_SECRET_KEY=pECTwjeSoe09wnKSZB6shxi417E5khhVWH5cqaTKg4JuoQtlaLguB7bIeXp5yrGe  
    DJANGO_ADMIN_URL=admin/  
    DJANGO_ALLOWED_HOSTS=localhost,0.0.0.0,127.0.0.1  
      
    # Security  
    # ------------------------------------------------------------------------------  
    # TIP: better off using DNS, however, redirect is OK too  
    DJANGO_SECURE_SSL_REDIRECT=False  
      
    # Email  
    # ------------------------------------------------------------------------------  
    DJANGO_SERVER_EMAIL=django.core.mail.backends.console.EmailBackend  
    EMAIL_HOST=  
    EMAIL_HOST_USER=  
    EMAIL_HOST_PASSWORD=  
    EMAIL_PORT=444  
    EMAIL_USE_TLS=True  
    DEFAULT_FROM_EMAIL=  
    DEFAULT_CONTACT_EMAIL=  
    DJANGO_EMAIL_BACKEND=10  
      
    # Gunicorn  
    # ------------------------------------------------------------------------------  
    WEB_CONCURRENCY=4  
      
    # Sentry  
    # ------------------------------------------------------------------------------  
    SENTRY_DSN=  
     
    # Secure  
    # ------------------------------------------------------------------------------  
    DJANGO_SECURE_SSL_REDIRECT=False  
    SESSION_COOKIE_SECURE=True  
    CSRF_COOKIE_SECURE=True  
    DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS=True  
    DJANGO_SECURE_HSTS_PRELOAD=True  
    DJANGO_SECURE_CONTENT_TYPE_NOSNIFF=True  
      
    # ADMINS  
    ADMINS_LIST=("""name""", "exemple@email.com")  
      
    # Corsheaders  
    # ------------------------------------------------------------------------------  
    CORS_ALLOWED_ORIGINS=http://localhost:8080,http://127.0.0.1:9000,http://localhost:3000  
    CORS_ORIGIN_WHITELIST=http://localhost:8080,http://127.0.0.1:9000,http://localhost:3000  
    CSRF_TRUSTED_ORIGINS=localhost:8080  
      
    # Config url extra  
    # ------------------------------------------------------------------------------  
    URL_TOKE_SEND_ACCOUNT=http://localhost:8000  
    URL_TOKE_SEND_RESET_PASSWORD=http://localhost:8000
:wrench:**Add variables to .postgres file**

    # PostgreSQL  
    # ------------------------------------------------------------------------------  
    POSTGRES_HOST=postgres  
    POSTGRES_PORT=5432  
    POSTGRES_DB=apps  
    POSTGRES_USER=postgres  
    POSTGRES_PASSWORD=Password

 
 
## Development environment docker  <img src="https://img.icons8.com/fluent/50/000000/docker.png"/>
 
### Run commands  
#### Create docker container local:  

   
     make build 
     make dev 
     make admin
     

#### Run container docker local  
  

     make run 

 
  
### Make file commands:  
 

    make dev - install project dependencies and migrate to DB  
    make run - run the project  
    make qa - to run pep8, isort and lint  

## Run in local development environment  
  

     python manage.py makemigrations --settings=config.settings.local 
     python manage.py migrate --settings=config.settings.local 
     python manage.py runserver 0.0.0.0:8000 --settings=config.settings.local 

 
## Production environment docker <img src="https://img.icons8.com/fluent/50/000000/docker.png"/>  
  
### Run commands  
#### Create docker image production:  

     docker-compose -f production.yml build 

 
#### Run image docker production  

     docker-compose -f production.yml up -d  
