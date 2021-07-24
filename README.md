# github-popular

## Tech Stack Used
#### Python 3.8
- Python is a modern, powerful and popular programming language.

#### FastAPI 0.67.0
- FastAPI is a modern, fast (high-performance), web framework for building APIs.

#### aiohttp 3.7.4
- Asynchronous HTTP Client/Server for asyncio and Python. One of the fastest libs for http requests.

#### Docker
- Docker use OS-level virtualization to deliver software in packages called containers.

#### Poetry 1.1.6
- Poetry is a tool for dependency management and packaging in Python.

#### Pytest
- A flexible and powerful lib used to automated tests

#### GitHub Actions
- Used to CI process

## Initialization

### Using Docker Compose
Create an `.env` file
```
make copy/local/envs
```

Add a valid personal access token in the `.env` file:
```
GITHUB_PERSONAL_ACCESS_TOKEN=<token>
```

In root project, run:
```
docker-compose up --build
```

### Running manually
Create a new Poetry Shell
```
make activate
```

Install all dependencies
```
make install/python
```

Add a valid personal access token:
```
export GITHUB_PERSONAL_ACCESS_TOKEN=<token>
```

Start the project
```
make run/fastapi
```


## Health Checking
Make a request to:
- [http://localhost:8000/healthz](http://localhost:8000/healthz)


## Docs
Check the API documentation in:
- [http://localhost:8000/docs](http://localhost:8000/docs)

Also, take a look in a live example in:
- [http://localhost:8000/github/repos/pytest-dev/pytest/popularity](http://localhost:8000/github/repos/pytest-dev/pytest/popularity)


## Testing
With Poetry environment active, run:
```
make run/tests
```


## Developing and contributing
Before start coding, enable the git hooks:
```
pre-commit install
```
