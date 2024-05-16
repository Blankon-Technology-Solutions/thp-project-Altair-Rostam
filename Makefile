.PHONY: dev,dev-compose,migrate,makemigrations,showmigrations,createsuperuser,format,test,cov,cov-report,fix,format,ff,inspect,run

dev:
	docker-compose -f docker-compose.dev.yml up -d
	poetry run python manage.py runserver
dev-compose:
	docker-compose -f docker-compose.dev.yml up -d
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
cov:
	poetry run pytest --cov=.
cov-report:
	poetry run pytest --cov=. --cov-report=json
fix:
	ruff --fix --exit-non-zero-on-fix . || True
format:
	ruff format .
ff:
	ruff --fix --exit-non-zero-on-fix . || True
	ruff format .


CONTAINER_NAME=postgresql-dev
inspect:
	docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' ${CONTAINER_NAME}
run:
	docker-compose build
	docker-compose up -d