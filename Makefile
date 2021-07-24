activate:
	poetry shell

install/python:
	poetry install

copy/local/envs:
	cp .env.dev .env

run/fastapi:
	poetry run uvicorn app.main:app --reload

run/tests:
	poetry run pytest

ci: copy/local/envs run/tests
