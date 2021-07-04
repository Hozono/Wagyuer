# Docker
create_image:
	docker build -t wagyuer:latest .

create_container:
	docker run -d -it --name wagyuer wagyuer:latest /bin/bash

start_container:
	docker start wagyuer

stop_container:
	docker stop wagyuer

connect_contaienr:
	docker exec -it wagyuer /bin/bash
	
remove_container:
	docker rm wagyuer

# Django
run:
	poetry run python manage.py runserver

dumpdata:
	poetry run python manage.py dumpdata auth.User --indent 2 --format=yaml > wagyuer/fixtures/user.yaml

loaddata:
	poetry run python manage.py loaddata  wagyuer/fixtures/user.yaml

migrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate
