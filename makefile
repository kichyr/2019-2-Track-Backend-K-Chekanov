up:
	sudo docker-compose up -d

migrate:
	sudo docker-compose run web python /code/manage.py migrate