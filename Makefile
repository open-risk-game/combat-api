up:
	docker-compose up -d

run: 
	python app.py

test:
	pytest

build:
	docker build -t combat-api .

dev-run:
	adev runserver .

install: install-test
	pip install -r requirments

install-test: pip install -r requirements-test
