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

Create an `.env` file
```
make copy/local/envs
```

Start the project
```
make run/flask
```

