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
