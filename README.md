To test this project you need instal the "install_requirements.txt"



Then, to test the project, clone this repo and write your terminal step by step:

cd payments_app

pipenv install

pipenv shell

flask run


Then, in a new terminal:

cd payments_app

cd application/test

pytest test.py
