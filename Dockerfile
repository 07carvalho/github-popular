FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VERSION=1.1.6
RUN pip install --upgrade pip
RUN mkdir /code
WORKDIR /code
RUN pip install "poetry==$POETRY_VERSION"
COPY pyproject.toml poetry.lock /code/
RUN poetry install --no-dev
RUN poetry export -f requirements.txt --output requirements.txt
RUN pip install -r requirements.txt
COPY . /code/
COPY .env.dev ./code/.env
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000" , "--reload"]
