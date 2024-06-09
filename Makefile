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
