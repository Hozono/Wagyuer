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
dumpdata:
	python manage.py dumpdata auth.User --indent 2 --format=json > wagyuer/fixtures/user.json

loaddata:
	python manage.py loaddata  wagyuer/fixtures/user.json
