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
	python manage.py test
	
clean_pycache:
	rm -rf */*/__pycache__

clean_migrate:
	rm -f */*/*/0*.py

