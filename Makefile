up:
	docker-compose up -d

run: 
	python app.py

test:
	pytest

dev-run:
	adev runserver .

install: install-test
	pip install -r requirments

install-test: pip install -r requirements-test
