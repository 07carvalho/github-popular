activate:
	poetry shell

install/python:
	poetry install

copy/local/envs:
	cp .env.dev .env

run/flask:
	poetry run uvicorn main:app --reload
