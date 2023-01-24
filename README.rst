poetry install

# activate pre-commit

pre-commit install

# start server
uvicorn demo.test:app
