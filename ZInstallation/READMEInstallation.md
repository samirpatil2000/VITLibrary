# VIT College Library
College Library
## WebSite Live At 
https://curiosityishere.pythonanywhere.com

# Installation to our django project

[![Python Version](https://img.shields.io/badge/python-3.8-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-3.2-brightgreen.svg)](https://djangoproject.com)



## Running the Project Locally

* First, clone the repository to your local machine:

```bash
git clone http://github.com/samirpatil2000/VITLibrary/
```
* Create & Activate Virtual Environment For Windows

```bash
py -m venv env
.\env\Scripts\activate
```

* Create & Activate Virtual Environment For MacOs/Linux

```bash
python3 -m venv env
source env/bin/activate
```


* Install the requirements:

```bash
pip install -r requirements.txt
```


* Create the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

* Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.


