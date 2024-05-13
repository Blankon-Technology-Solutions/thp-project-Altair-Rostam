dev:
	poetry run python manage.py runserver
migrate:
	poetry run python manage.py migrate
makemigrations:
	poetry run python manage.py makemigrations
inspect:
	docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' postgresql
compose:
	docker-compose up -d