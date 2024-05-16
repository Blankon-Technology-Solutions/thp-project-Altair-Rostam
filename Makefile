.PHONY: dev,migrate,makemigrations,showmigrations,createsuperuser,format,fix,inspect,compose

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
test:
	poetry run pytest -s -vv --show-capture=no
coverage:
	poetry run pytest --cov=.
report:
	poetry run pytest --cov=. --cov-report html
fix:
	ruff --fix --exit-non-zero-on-fix . || True
format:
	ruff format .

CONTAINER_NAME=postgresql
inspect:
	docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' ${CONTAINER_NAME}
compose:
	docker-compose up -d
run:
	docker-compose build
	docker-compose up -d