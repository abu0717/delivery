<h1 align="center"> 👋 This is my delivery project</h1>
<h3 align="center">A passionate frontend developer from Uzbekistan</h3>
<h1> Intro </h1>

## Before start pull my files to your lap top.
    git clone git@github.com:abu0717/delivery.git
## And then open your terminal and start creating by env file
      python3 install -m venv .env
## then activate env file.
## And after that start with installing requirements.txt
    pip install -m requirements.txt
## then make a migrations.
    ./manage.py makemigrations

## and after that migrate it.
    ./manage.py migrate

## before runing server create super user in order to open admin panel.
    ./manage.py createsuperuser

## then finally start project.
    ./manage.py runserver

#Then you can open website on your local host.

P.S: The project is not complete. Few endpoints might be out of service.
