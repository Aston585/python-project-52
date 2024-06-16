.PHONY: dev trans compile migrate test clean_pycache clean_migrate

build:
	./build.sh

install:
	poetry install

PORT ?= 8000
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi

lint:
	poetry run flake8 task_manager --exclude migrations

dev:
	python manage.py runserver
	
trans:
	python manage.py makemessages -l ru
	
compile:	
	python manage.py compilemessages
	
migrate:
	python manage.py makemigrations
	python manage.py migrate
	
test:
	poetry run python3 manage.py test
	
test-coverage:
	poetry run coverage run manage.py test
	poetry run coverage report --include=task_manager/* --omit=task_manager/settings.py
	poetry run coverage xml --include=task_manager/* --omit=task_manager/settings.py

clean_pycache:
	rm -rf */*/__pycache__

clean_migrate:
	rm -f */*/*/0*.py

