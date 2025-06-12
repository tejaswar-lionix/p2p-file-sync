build:
	docker build -t p2p-sync .

test:
	pytest -q

run:
	python manage.py runserver 0.0.0.0:8000
