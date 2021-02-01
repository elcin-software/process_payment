To test this project you need to install these:
aniso8601
click
Flask
Flask-RESTful
Flask-SQLAlchemy
itsdangerous
Jinja2
MarkupSafe
pytz
six
SQLAlchemy
Werkzeug
appdirs==1.4.4
attrs==20.3.0
beautifulsoup4==4.9.3
soupsieve==2.1
toml==0.10.2
urllib3==1.26.2
virtualenv==20.4.0
virtualenv-clone==0.5.4
waitress==1.4.4
WebOb==1.8.6
WebTest==2.0.35
certifi==2020.12.5
chardet==4.0.0
click==7.1.2
distlib==0.3.1
environ==1.0
environs==9.3.0
filelock==3.0.12
idna==2.10
iniconfig==1.1.1
marshmallow==3.10.0
packaging==20.8
pipenv==2020.11.15
pluggy==0.13.1
py==1.9.0
pyparsing==2.4.7
pytest==6.1.2
python-dotenv==0.15.0
requests==2.25.1

Then, to test the project, clone this repo and write your terminal step by step:
cd payments_app
pipenv install
pipenv shell
flask run

Then, in a new terminal:
cd payments_app
cd application/test
pytest test.py
