# Including commands
run-django-server:
	poetry run task server localhost:8000

run-quasar:
	yarn quasar dev

run-serve-mkdocs:
	poetry run task serve-mkdocs

.PHONY: clear
clear:
	poetry run task clear

.PHONY: createadmin
createadmin:
	poetry run task createsuperuser

.PHONY: migrate
migrate:
	poetry run task migrate

.PHONY: makemigrations
makemigrations:
	poetry run task makemigrations

# Primary commands
.PHONY: install
install:
	poetry run pip install -U setuptools
	poetry install --no-root
	yarn
	poetry run task initconfig --debug
	@make migrate

.PHONY: install-prod
install-prod:
	poetry install --no-root
	yarn
	poetry run task initconfig

.PHONY: run
run:
	@make -j 3 run-serve-mkdocs run-django-server run-quasar

.PHONY: build
build:
	yarn build
	poetry run task collectstatic
	@make migrate

.PHONY: deploy
deploy:
	@make build
	sudo systemctl restart gunicorn
	sudo systemctl restart nginx

.PHONY: docker-run
docker-run:
	poetry run task dockervolumes
	docker-compose up
