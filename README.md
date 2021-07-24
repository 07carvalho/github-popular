# github-popular
This RESTful API uses the official GitHub REST API to check if a repository is popular or not.

This application follows the `factory` pattern, defining bounds per business logic. This architecture allows the application to grow in number of modules easily to maintain and read.

The GitHub service main logic remains in two files in `github` module:
- `clients.py` keeps the requests to GitHub API.
- `services.py` holds the application business logic, like the method that evaluate whether the provided GitHub repository is popular or not.

This project also follows the SOLID and Clean Code principles.

### Performance
Once one of the evaluation criteria is that the `repo_popularity` request should respond within 0.5 second, I did many tests to improve the results.

My first shot was with a Django/Django Rest Framework stack, which gave me a request responding with 600-700 milliseconds (quite bad).

So I tried FastAPI with a combination of http requests packages, finally remaining with `aiohttp`, which brings better results in a series of requests tests:

| # Request | Result (ms) |
|:---------:|:-----------:|
|     1     |     540     |
|     2     |     521     |
|     3     |     524     |
|     4     |     484     |
|     5     |     472     |
|     6     |     532     |
|     7     |     494     |
|     8     |     493     |
|     9     |     482     |
|     10    |     513     |
| **AVG Time** |   **505**   |

Although the average time is not within expectations, this stack gives a clue to achieve a better performance

#### Future improvements
- [ ] Add cache to avoid hit the GitHub API in each request;
- [ ] Go deep in `aiohttp` to improve usage and mock the requests properly;
- [ ] Test another http requests packages;
- [ ] Deploy the application in a web server;


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
