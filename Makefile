create_image:
	docker build -t wagyuer:latest .

create_container:
	docker run -d -it --name wagyuer wagyuer:latest /bin/bash

start_container:
	docker start wagyuer

connect_contaienr:
	docker exec -it wagyuer /bin/bash

stop_container:
	docker stop wagyuer

remove_container:
	docker rm wagyuer