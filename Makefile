PORT ?= 8000

install:
	poetry install --no-dev

start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager:app

lint:
	poetry run flake8 task_manager --exclude migrations

# build:
# 	./build.sh

.PHONY: dev trans compile migrate test reset_db clean

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
