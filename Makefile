.PHONY: dev,migrate,makemigrations,showmigrations,createsuperuser,format,inspect,compose

dev:
	poetry run python manage.py runserver
migrate:
	poetry run python manage.py migrate
makemigrations:
	poetry run python manage.py makemigrations
showmigrations:
	poetry run python manage.py showmigrations
createsuperuser:
	poetry run python manage.py createsuperuser
format:
	ruff --fix --exit-non-zero-on-fix . || True
inspect:
	docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' postgresql
compose:
	docker-compose up -d